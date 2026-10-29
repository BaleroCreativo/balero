import math,os,sys
from playwright.sync_api import sync_playwright
FPS=30;DUR=6.0;N=int(FPS*DUR);OUT=sys.argv[1];os.makedirs(OUT,exist_ok=True)
cl=lambda x:max(0.0,min(1.0,x)); seg=lambda t,a,b:cl((t-a)/(b-a))
eo=lambda x:1-(1-x)**3
eio=lambda x:3*x*x-2*x**3
def eob(x):
    c1=1.0;c3=c1+1;return 1+c3*(x-1)**3+c1*(x-1)**2
only=[int(a) for a in sys.argv[2:]] if len(sys.argv)>2 else None
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1440})
    pg.goto('file://'+os.getcwd()+'/laptop-open.html'); pg.wait_for_timeout(1200)
    for f in range(N):
        if only and f not in only: continue
        t=f/FPS
        enter=eo(seg(t,0,0.8)); y_in=240*(1-enter)
        a=-90+94*eob(eio(seg(t,0.6,2.0))) if t>0.6 else -90
        a=min(a,6)
        glow=0.95*(1-eio(seg(t,1.3,2.0))) if t>1.1 else 0
        tilt=-24+11*eio(seg(t,2.0,3.0))
        sy=-2300*eio(seg(t,2.6,5.6))
        emit=0.55*eio(seg(t,1.3,2.4))
        t1=eo(seg(t,0.25,0.8));t2=eo(seg(t,0.45,1.1));t3=eo(seg(t,4.6,5.1))
        pulse=0 if t<5.1 else 10*math.sin((t-5.1)*2*math.pi*1.2)**2
        js=f"""()=>{{const $=i=>document.getElementById(i);
        $('lid').style.setProperty('--a','{a}deg');document.querySelector('.deck').style.setProperty('--emit','{emit}');$('lp').style.setProperty('--tilt','{tilt}deg');
        $('lp').style.translate='0 {y_in}px';$('lp').style.opacity={cl(enter*1.5)};
        $('site').style.setProperty('--sy','{sy}px');$('glow').style.opacity={glow};
        $('t1').style.opacity={t1};$('t1').style.transform='translateY({40*(1-t1)}px)';
        $('t2').style.opacity={t2};$('t2').style.transform='translateY({40*(1-t2)}px)';
        $('t3').style.opacity={t3};$('t3').style.transform='translateX({pulse}px)';}}"""
        pg.evaluate(js); pg.screenshot(path=f'{OUT}/f{f:04d}.png')
    b.close()
