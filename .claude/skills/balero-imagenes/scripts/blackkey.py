import sys, numpy as np, warnings
warnings.filterwarnings("ignore")
from PIL import Image
from scipy import ndimage as ndi
from skimage import morphology, filters, measure
from realesrgan_ncnn_py import Realesrgan
src,dst=sys.argv[1],sys.argv[2]
up=Realesrgan(gpuid=-1, model=3)
im=up.process_pil(Image.open(src).convert("RGB"))
a=np.array(im).astype(float)
mx=a.max(axis=2)
m=mx>34
m=morphology.binary_opening(m,morphology.disk(2))
m=morphology.binary_closing(m,morphology.disk(6))
m=ndi.binary_fill_holes(m)
lab=measure.label(m); s=np.bincount(lab.ravel()); s[0]=0
m=(s>=0.01*s.max())[lab]
# borde suave: mezcla entre el umbral duro y la luminancia
soft=np.clip((mx-14)/40,0,1)
alpha=np.maximum(filters.gaussian(m.astype(float),1.0)*np.clip((mx-8)/30,0,1)*1.0, 0)
alpha=np.where(ndi.binary_erosion(m,iterations=4),1.0,alpha)
Image.fromarray(np.dstack([a,alpha*255]).astype("uint8"),"RGBA").save(dst)
print("ok",dst)
