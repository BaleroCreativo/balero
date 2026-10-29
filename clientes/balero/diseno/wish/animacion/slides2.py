import os,sys,math
from playwright.sync_api import sync_playwright
R=os.getcwd(); D=R+'/mac'; FPS=30
cl=lambda x:max(0.0,min(1.0,x)); seg=lambda t,a,b:cl((t-a)/(b-a))
eo=lambda x:1-(1-x)**3; eio=lambda x:3*x*x-2*x**3
base=open(R+'/p2/html/slide-1.html',encoding='utf8').read(); HEAD=base[:base.find('<body')]
LOGO='file:///home/user/balero/.claude/skills/balero-imagenes/assets/logo-balero.png'
NS=7
MARK=lambda txt,bg='#665FE9',col='#fff':f"<span style=\"font-family:Instrument Serif;font-style:italic;font-weight:400;text-transform:none;letter-spacing:0;background:{bg};color:{col};padding:0 .14em;display:inline-block;transform:rotate(-1.5deg)\">{txt}</span>"
def dots(i): return '<div class="dots">'+''.join('<i class="on"></i>' if k==i else '<i></i>' for k in range(NS))+'</div>'
CSS=f"""
.bg-y{{background:url('file://{D}/bg-yellow.png') center/cover!important}}
.bg-k{{background:url('file://{D}/bg-black.png') center/cover!important;color:#fff}}
.bg-k .foot,.bg-k .layer{{color:#fff}} .bg-k .logo{{filter:invert(1)}} .bg-k .dots i{{background:#3a3848}} .bg-k .dots i.on{{background:#FFD23F}}
.bw{{position:absolute;left:86px;top:566px;width:908px;height:626px;border-radius:22px;background:#f3f3f6;box-shadow:0 30px 60px rgba(90,50,0,.30),0 0 0 2px rgba(255,255,255,.5) inset;overflow:hidden;z-index:2}}
.bw .hd{{height:54px;display:flex;align-items:center;gap:10px;padding-left:22px;background:#e6e6ec}}
.bw .hd i{{width:14px;height:14px;border-radius:50%;background:#c4c4cc}}
.bw .vp{{position:absolute;left:0;top:54px;width:908px;height:572px;overflow:hidden;background:#111}}
.bw .in{{position:absolute;left:0;top:0;width:908px;transform-origin:0 0}}
.bw .in img{{width:908px;display:block}}
.cur{{position:absolute;left:0;top:0;width:44px;height:44px;z-index:5;opacity:0}}
.rip{{position:absolute;width:80px;height:80px;border-radius:50%;border:5px solid #665FE9;opacity:0;z-index:5}}
.pill{{position:absolute;left:86px;top:1226px;z-index:4;background:#111;color:#FFD23F;font:700 36px 'Source Sans Pro',sans-serif;padding:12px 28px;border-radius:999px;box-shadow:0 8px 24px rgba(0,0,0,.22);opacity:0}}
.step{{position:absolute;left:86px;z-index:4;font:700 40px 'Source Sans Pro',sans-serif;padding:14px 32px;border-radius:999px;border:3px solid #111;color:#111;opacity:0;transition:none}}
.row{{position:absolute;left:86px;width:880px;z-index:3;display:flex;align-items:center;gap:28px;opacity:0;font:700 48px/1.15 'Source Sans Pro',sans-serif;color:#111}}
.row b{{flex:0 0 76px;height:76px;border-radius:50%;background:#665FE9;color:#fff;font:800 38px/76px Poppins,sans-serif;text-align:center}}
.phone{{position:absolute;left:560px;top:580px;width:352px;height:720px;border-radius:58px;background:#0b0b0d;box-shadow:0 30px 60px rgba(90,50,0,.35),0 0 0 3px #3a3a40 inset;z-index:2}}
.phone .sc{{position:absolute;left:14px;top:14px;width:324px;height:692px;border-radius:46px;overflow:hidden;background:#111}}
.phone .in{{position:absolute;left:0;top:0;width:324px;transform-origin:0 0}} .phone .in img{{width:324px;display:block}}
.phone .nt{{position:absolute;left:50%;top:22px;width:92px;height:26px;margin-left:-46px;border-radius:14px;background:#0b0b0d;z-index:3}}
"""
def html(body,cls='bg-y',idx=0):
    return HEAD.replace('</head>','<style>'+CSS+'</style></head>')+f'<body><div class="slide {cls}" style="--mx:86px;--my:86px"><img class="logo" src="{LOGO}">{dots(idx)}{body}<div class="foot">Balero Creativo</div></div></body></html>'
def tx(i,top,sz,txt,cls=''): return f'<div class="layer {cls}" id="{i}" style="left:86px;top:{top}px;font-size:{sz}px;line-height:1;">{txt}</div>'
PILL='<div class="pill" id="lab">x</div>'
def browser(img): return f'<div class="bw" id="bw"><div class="hd"><i></i><i></i><i></i></div><div class="vp"><div class="in" id="in"><img src="file://{R}/{img}"></div><div class="cur" id="cur"><svg viewBox="0 0 24 24" width="44" height="44"><path d="M3 2l7 19 3-8 8-3z" fill="#111" stroke="#fff" stroke-width="1.6"/></svg></div><div class="rip" id="rip"></div></div></div>'
tin=lambda t,a,b=0.55:eo(seg(t,a,a+b))
def rise(t,ids):
    s=''
    for i,a in ids: o=tin(t,a); s+=f"$('{i}').style.opacity={o};$('{i}').style.transform='translateY({36*(1-o)}px)';"
    return s
def labjs(t,labs):
    txt='';op=0
    for a0,a1,x in labs:
        o=eo(seg(t,a0,a0+0.35))*(1-eo(seg(t,a1-0.3,a1)))
        if o>op: op=o;txt=x
    return f"if({op}>0)$('lab').textContent={txt!r};$('lab').style.opacity={op};$('lab').style.transform='translateY({16*(1-op)}px)';"
SC={}
# --- 2: menu y buscador
SC['s2']=dict(dur=5.6,html=html(tx('t1',200,64,'La home de Wish Travel:','l')+tx('t2',288,88,'MENÚ Y BUSCADOR')+tx('t4',392,112,MARK('a la vista'))+browser('hero2x.png')+PILL,idx=1))
def js2(t):
    e=eo(seg(t,0,0.8)); s=f"$('bw').style.translate='0 {120*(1-e)}px';$('bw').style.opacity={cl(e*1.6)};"
    s+=rise(t,[('t1',0.2),('t2',0.4),('t4',0.6)])
    z1=eio(seg(t,1.0,1.7))*(1-eio(seg(t,2.5,3.1))); z2=eio(seg(t,3.1,3.8)); tot=z1+z2
    W,H=908,572; sc=1+0.8*z1+1.0*z2
    fx,fy=((0.5*z1+0.30*z2)/tot,(0.05*z1+0.72*z2)/tot) if tot>1e-6 else (0.5,0.5)
    txp=max(W-W*sc,min(0,W/2-fx*W*sc)); typ=max(H-H*sc,min(0,H/2-fy*H*sc))
    s+=f"$('in').style.transform='translate({txp}px,{typ}px) scale({sc})';"
    c=eio(seg(t,3.7,4.6)); px=560+300*c*0+ (520-560)*c; py=300+(300-300)*c
    # destino del cursor: boton de busqueda (zoom 1.0 de 2.0) ~ (x 690, y 420) en pantalla del visor
    px=420+270*c; py=300+120*c
    s+=f"$('cur').style.opacity={eo(seg(t,3.6,3.9))};$('cur').style.left='{px}px';$('cur').style.top='{py}px';"
    r=seg(t,4.6,5.2); s+=f"$('rip').style.opacity={(1-r) if 0<r<1 else 0};$('rip').style.left='{px-26}px';$('rip').style.top='{py-26}px';$('rip').style.transform='scale({0.4+1.6*r})';"
    return s+labjs(t,[(1.2,2.7,'Menú'),(3.3,5.5,'Buscador')])
# --- 3: destino (italia)
SC['s3']=dict(dur=5.8,html=html(tx('t1',200,64,'Cada destino,','l')+tx('t2',288,88,'SU PROPIA PÁGINA')+tx('t4',392,112,MARK('De Roma a Sicilia'))+browser('italia-comp2.png')+PILL,idx=2))
def js3(t):
    e=eo(seg(t,0,0.8)); s=f"$('bw').style.translate='0 {120*(1-e)}px';$('bw').style.opacity={cl(e*1.6)};"
    s+=rise(t,[('t1',0.2),('t2',0.4),('t4',0.6)])
    K=908/1440; W=908
    y=2250*eio(seg(t,2.0,2.9))+450*eio(seg(t,3.9,5.3))     # px del sitio (1440)
    z=1+0.65*eio(seg(t,2.0,2.9))
    s+=f"$('in').style.transform='translate({-W*(z-1)/2}px,0) scale({z}) translate(0,{-y*K}px)';"
    return s+labjs(t,[(0.9,2.0,'Página de destino'),(3.0,5.6,'Itinerario día a día')])
# --- 4: movil
STEPS=[('Inicio',640),('Por qué elegir',730),('Destinos',820)]
steps_html=''.join(f'<div class="step" id="st{k}" style="top:{y}px">{n}</div>' for k,(n,y) in enumerate(STEPS))
phone=f'<div class="phone" id="ph"><div class="nt"></div><div class="sc"><div class="in" id="in"><img src="file://{R}/mob-comp.png"></div></div></div>'
SC['s4']=dict(dur=5.6,html=html(tx('t1',200,64,'También en celular:','l')+tx('t2',288,88,'VERSIÓN MÓVIL')+tx('t4',392,112,MARK('se adapta'))+steps_html+phone,idx=3))
def js4(t):
    e=eo(seg(t,0,0.8)); s=f"$('ph').style.translate='0 {160*(1-e)}px';$('ph').style.opacity={cl(e*1.6)};"
    s+=rise(t,[('t1',0.2),('t2',0.4),('t4',0.6)])
    K=324/780
    # posiciones (px de la captura 2x): hero 0, destinos ~ 3300, como funciona ~ 7300
    y=2280*eio(seg(t,1.7,2.7))+4150*eio(seg(t,3.3,4.9))
    s+=f"$('in').style.transform='translate(0,{-y*K}px)';"
    act=0 if t<1.9 else (1 if t<3.6 else 2)
    for k in range(3):
        o=eo(seg(t,0.9+0.15*k,1.3+0.15*k))
        on=(k==act)
        s+=f"$('st{k}').style.opacity={o};$('st{k}').style.background='{'#111' if on else 'transparent'}';$('st{k}').style.color='{'#FFD23F' if on else '#111'}';"
    return s
# --- 5: lo que incluye
rows=[('1','Buscador por destino<br>y tipo de viaje',620),('2','Una página por destino,<br>con itinerario día a día',850),('3','Contacto directo por<br>WhatsApp o videollamada',1080)]
rows_html=''.join(f'<div class="row" id="r{k}" style="top:{y}px"><b>{n}</b><span>{t}</span></div>' for k,(n,t,y) in enumerate(rows))
SC['s5']=dict(dur=5.0,html=html(tx('t1',200,64,'Lo que incluye','l')+tx('t2',288,88,'EL SITIO DE WISH')+tx('t4',392,112,MARK('en pocas palabras'))+rows_html,idx=4))
def js5(t):
    s=rise(t,[('t1',0.2),('t2',0.4),('t4',0.6)])
    for k in range(3):
        o=tin(t,1.0+0.7*k,0.6); s+=f"$('r{k}').style.opacity={o};$('r{k}').style.transform='translateX({-50*(1-o)}px)';"
    return s
# --- 6: idea
SC['s6']=dict(dur=5.0,html=html(tx('t1',200,64,'La idea del sitio:','l')+tx('a1',380,100,'PORQUE TODO')+tx('a2',496,100,'VIAJE COMIENZA')+tx('a3',612,100,'CON')+tx('a4',770,190,MARK('un deseo.','#FFD23F','#111'))+'<div class="layer l" id="a5" style="left:86px;top:1130px;font-size:40px;font-family:Source Sans Pro;text-transform:none;letter-spacing:0;color:#A9A4F7;font-weight:600">El concepto detrás del sitio de Wish Travel</div>',cls='bg-k',idx=5))
def js6(t): return rise(t,[('t1',0.2),('a1',0.5),('a2',0.75),('a3',1.0),('a4',1.35),('a5',2.4)])
# --- 7: cierre
btn="<div id='btn' style=\"position:absolute;left:86px;top:930px;z-index:3;background:#111;color:#FFD23F;font:700 46px 'Source Sans Pro',sans-serif;padding:20px 44px;border-radius:999px;box-shadow:0 10px 28px rgba(0,0,0,.25);opacity:0;transform-origin:0 50%\">Escríbenos por mensaje directo</div>"
SC['s7']=dict(dur=5.2,html=html(tx('t1',260,64,'Tu turno:','l')+tx('t2',350,120,'¿QUIERES UN')+tx('t3',476,120,'SITIO ASÍ?')+tx('t4',660,120,MARK('para tu negocio'))+btn+'<div class="layer l" id="u" style="left:86px;top:1080px;font-size:44px;">Diagnóstico gratis de 15 min</div><div class="layer l" id="u2" style="left:86px;top:1150px;font-size:44px;">balerocreativo.com</div>',idx=6))
def js7(t):
    s=rise(t,[('t1',0.2),('t2',0.45),('t3',0.7),('t4',1.0),('u',2.0),('u2',2.2)])
    b=tin(t,1.6,0.6); pulse=1+0.04*math.sin((t-2.3)*2*math.pi*1.2)**2 if t>2.3 else 1
    return s+f"$('btn').style.opacity={b};$('btn').style.transform='scale({pulse*(0.92+0.08*b)})';"
JS={'s2':js2,'s3':js3,'s4':js4,'s5':js5,'s6':js6,'s7':js7}
def render(name,only=None):
    sc=SC[name]; N=int(sc['dur']*FPS); out=f'{R}/v2_{name}'; os.makedirs(out,exist_ok=True)
    hp=f'{R}/v2_{name}.html'; open(hp,'w',encoding='utf8').write(sc['html'])
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=b.new_page(viewport={'width':1080,'height':1440}); pg.goto('file://'+hp); pg.wait_for_timeout(1500)
        for f in range(N):
            if only and f not in only: continue
            body=JS[name](f/FPS)
            pg.evaluate("()=>{const $=i=>document.getElementById(i);"+body+"}"); pg.screenshot(path=f'{out}/f{f:04d}.png')
        b.close()
if __name__=='__main__':
    render(sys.argv[1],[int(a) for a in sys.argv[2:]] or None)
