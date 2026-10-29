import math,os,sys
from playwright.sync_api import sync_playwright
FPS=30;DUR=9.5;N=int(FPS*DUR);OUT=sys.argv[1];os.makedirs(OUT,exist_ok=True)
cl=lambda x:max(0.0,min(1.0,x)); seg=lambda t,a,b:cl((t-a)/(b-a))
eo=lambda x:1-(1-x)**3
eio=lambda x:3*x*x-2*x**3
def eob(x):
    c1=1.0;c3=c1+1;return 1+c3*(x-1)**3+c1*(x-1)**2
only=[int(a) for a in sys.argv[2:]] if len(sys.argv)>2 else None
LABS=[(2.0,3.6,'01 · Inicio'),(4.3,5.9,'02 · Destinos'),(6.6,8.2,'03 · Cómo funciona')]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
    pg=b.new_page(viewport={'width':1080,'height':1440})
    pg.goto('file://'+os.getcwd()+'/laptop-open.html'); pg.wait_for_timeout(1200)
    for f in range(N):
        if only and f not in only: continue
        t=f/FPS
        enter=eo(seg(t,0,0.8)); y_in=240*(1-enter)
        a=min(6,-90+94*eob(eio(seg(t,0.6,2.0)))) if t>0.6 else -90
        glow=0.95*(1-eio(seg(t,1.3,2.0))) if t>1.1 else 0
        tilt=-24+11*eio(seg(t,2.0,3.0))
        emit=0.55*eio(seg(t,1.3,2.4))
        # scroll con pausas
        sy=-1140*eio(seg(t,3.6,4.3)) + -1320*eio(seg(t,5.9,6.6))
        # zoom suave en los puntos de pausa
        sc=0.83+0.17*eio(seg(t,4.3,5.0))*(1-eio(seg(t,5.5,6.4)))+0.12*eio(seg(t,6.6,7.3))*(1-eio(seg(t,7.8,8.6)))
        t1=eo(seg(t,0.25,0.8));t2=eo(seg(t,0.4,0.95));t4=eo(seg(t,0.6,1.2))
        lab_txt='';lab_op=0
        for (a0,a1,txt) in LABS:
            o=eo(seg(t,a0,a0+0.35))*(1-eo(seg(t,a1-0.3,a1)))
            if o>lab_op: lab_op=o;lab_txt=txt
        bt=eo(seg(t,8.4,9.0)); pulse=1+0.05*math.sin((t-9.0)*2*math.pi*1.3)**2 if t>9.0 else 1
        js=f"""()=>{{const $=i=>document.getElementById(i);
        $('lid').style.setProperty('--a','{a}deg');document.querySelector('.deck').style.setProperty('--emit','{emit}');
        $('lp').style.setProperty('--tilt','{tilt}deg');$('lp').style.setProperty('--sc','{sc}');
        $('lp').style.translate='0 {y_in}px';$('lp').style.opacity={cl(enter*1.5)};
        $('site').style.setProperty('--sy','{sy}px');$('glow').style.opacity={glow};
        for(const [i,o] of [['t1',{t1}],['t2',{t2}],['t4',{t4}]]){{$(i).style.opacity=o;$(i).style.transform='translateY('+(40*(1-o))+'px)';}}
        if({lab_op}>0) $('lab').textContent={lab_txt!r};
        $('lab').style.opacity={lab_op};$('lab').style.transform='translateY({16*(1-lab_op)}px)';
        $('btn').style.opacity={bt};$('btn').style.transform='scale({pulse*(0.92+0.08*bt)})';}}"""
        pg.evaluate(js); pg.screenshot(path=f'{OUT}/f{f:04d}.png')
    b.close()
