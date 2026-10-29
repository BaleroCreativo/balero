import math, sys, os
from playwright.sync_api import sync_playwright
SP=sys.argv[1]; HTML=sys.argv[2]; OUT=sys.argv[3]
FPS=30; DUR=5.0; N=int(FPS*DUR)
os.makedirs(OUT,exist_ok=True)
def clamp(x): return max(0.0,min(1.0,x))
def seg(t,a,b): return clamp((t-a)/(b-a))
def eo(x): return 1-(1-x)**3
def eb(x):  # ease-out-back suave
    c1=1.2; c3=c1+1; return 1+c3*(x-1)**3+c1*(x-1)**2
JS="""
(t)=>{
 const L=[...document.querySelectorAll('.layer')];
 const ill=document.querySelector('.ill');
 const set=(el,o)=>{ if(o.op!==undefined) el.style.opacity=o.op; if(o.tf!==undefined) el.style.transform=o.tf; if(o.cp!==undefined) el.style.clipPath=o.cp; };
 return 0;
}
"""
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1440})
    pg.goto('file://'+HTML); pg.wait_for_timeout(800)
    pg.evaluate("document.fonts.ready")
    pg.evaluate("""()=>{window.__L=[...document.querySelectorAll('.layer')];window.__I=document.querySelector('.ill');window.__S=document.querySelector('.slide');window.__base=window.__I.style.transform;}""")
    for f in range(N):
        t=f/FPS
        def tx(a,b,dy=44):
            e=eo(seg(t,a,b)); return e, dy*(1-e)
        st=[]
        # capas: 0 fino,1 NUEVO SITIO,2 WEB PARA,3 marker,4 DESLIZA
        e0,d0=tx(0.2,0.75); e1,d1=tx(0.5,1.05); e2,d2=tx(0.7,1.25)
        em=eo(seg(t,1.25,1.85))
        ed=eo(seg(t,3.0,3.5))
        pulse=0 if t<3.5 else 10*math.sin((t-3.5)*2*math.pi*1.4)**2
        lap=eb(seg(t,1.5,2.7)); lap_dy=620*(1-lap)
        fl=0 if t<2.7 else 7*math.sin((t-2.7)*2*math.pi*0.55)*min(1,(t-2.7))
        zoom=1+0.03*seg(t,0,DUR)
        js=f"""()=>{{
          const L=window.__L,I=window.__I,S=window.__S;
          L[0].style.opacity={e0};L[0].style.transform='translateY({d0}px)';
          L[1].style.opacity={e1};L[1].style.transform='translateY({d1}px)';
          L[2].style.opacity={e2};L[2].style.transform='translateY({d2}px)';
          L[3].style.clipPath='inset(-20px {(1-em)*100}% -20px -20px)';L[3].style.opacity={1 if em>0 else 0};
          L[4].style.opacity={ed};L[4].style.transform='translateX({pulse}px)';
          I.style.opacity={clamp(lap*1.6)};I.style.transform='translateY({lap_dy+fl}px) rotate(-5deg)';
          S.style.transformOrigin='50% 60%';S.style.transform='scale({zoom})';
        }}"""
        pg.evaluate(js)
        pg.screenshot(path=f"{OUT}/f{f:04d}.png")
    b.close()
