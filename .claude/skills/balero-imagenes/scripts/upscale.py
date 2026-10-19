#!/usr/bin/env python3
"""Aumenta a 800 px (x4) una ilustración 3D de 200 px con Real-ESRGAN, sin GPU.

Preparación (una vez):  python3 -m venv env && . env/bin/activate && pip install realesrgan-ncnn-py pillow
                        y en Ubuntu:  apt-get install -y libomp5
Uso:  python3 upscale.py entrada.png salida.png
Después, recortar con cutout.sh y, si el objeto es blanco, cerrar huecos del alfa (ver references/ilustraciones-3d.md).
"""
import sys
from PIL import Image
from realesrgan_ncnn_py import Realesrgan

up = Realesrgan(gpuid=-1, model=3)  # 3 = realesrgan-x4plus
up.process_pil(Image.open(sys.argv[1]).convert("RGB")).save(sys.argv[2])
