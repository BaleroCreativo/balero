import os,re,sys,math
from playwright.sync_api import sync_playwright
R=os.getcwd(); D=R+'/mac'
FPS=30
cl=lambda x:max(0.0,min(1.0,x)); seg=lambda t,a,b:cl((t-a)/(b-a))
eo=lambda x:1-(1-x)**3; eio=lambda x:3*x*x-2*x**3
base=open(R+'/p2/html/slide-1.html',encoding='utf8').read()
HEAD=base[:base.find('<body')]
LOGO='file:///home/user/balero/.claude/skills/balero-imagenes/assets/logo-balero.png'
MARK=lambda txt,bg='#665FE9',col='#fff':f"<span style=\"font-family:Instrument Serif;font-style:italic;font-weight:400;text-transform:none;letter-spacing:0;background:{bg};color:{col};padding:0 .14em;display:inline-block;transform:rotate(-1.5deg)\">{txt}</span>"
def dots(i,n=5): return '<div class="dots">'+''.join('<i class="on"></i>' if k==i else '<i></i>' for k in range(n))+'</div>'
COMMON=f"""
.stage{{position:absolute;left:0;top:0;width:1080px;height:1440px;z-index:1}}
.lp{{position:absolute;left:70px;top:585px;width:940px;height:632px;transform-origin:50% 62%}}
.lidw{{position:absolute;left:0;top:0;width:940px;height:470px}}
.lidw img.lid{{position:absolute;left:0;top:0;width:940px;height:470px}}
.scr{{position:absolute;left:129px;top:38px;width:661px;height:411px;overflow:hidden;background:#0c0c10;border-radius:3px}}
.scr .in{{position:absolute;left:0;top:0;width:661px;transform-origin:0 0}}
.scr .in img{{width:661px;display:block}}
.scr .gl{{position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.12) 0%,transparent 34%,transparent 70%,rgba(255,255,255,.05) 100%);pointer-events:none}}
.basew{{position:absolute;left:0;top:470px;width:940px;height:162px;z-index:3}}
.basew img{{width:940px;height:162px;display:block}}
.shd{{position:absolute;left:150px;top:1215px;width:780px;height:60px;border-radius:50%;background:rgba(120,70,0,.45);filter:blur(26px);z-index:0}}
.pill{{position:absolute;left:86px;top:1226px;z-index:4;background:#111;color:#FFD23F;font:700 36px 'Source Sans Pro',sans-serif;padding:12px 28px;border-radius:999px;box-shadow:0 8px 24px rgba(0,0,0,.22);opacity:0}}
.cur{{position:absolute;left:0;top:0;width:34px;height:34px;z-index:5;opacity:0}}
.rip{{position:absolute;width:60px;height:60px;border-radius:50%;border:4px solid #665FE9;opacity:0;z-index:5}}
.bg-y{{background:url('file://{D}/bg-yellow.png') center/cover!important}}
.bg-k{{background:url('file://{D}/bg-black.png') center/cover!important;color:#fff}}
.bg-k .foot,.bg-k .layer{{color:#fff}}
.bg-k .logo{{filter:invert(1)}}
.bg-k .dots i{{background:#3a3848}}
.bg-k .dots i.on{{background:#FFD23F}}
"""
def laptop(img, scrcls=''):
    return f'''<div class="shd"></div><div class="stage"><div class="lp" id="lp"><div class="lidw"><img class="lid" src="file://{D}/lid.png"><div class="scr"><div class="in" id="in"><img src="file://{R}/{img}"></div><div class="gl"></div><div class="cur" id="cur"><svg viewBox="0 0 24 24" width="34" height="34"><path d="M3 2l7 19 3-8 8-3z" fill="#111" stroke="#fff" stroke-width="1.6"/></svg></div><div class="rip" id="rip"></div></div></div><div class="basew"><img src="file://{D}/base.png"></div></div></div>'''
def html(body,css='',cls='bg-y',idx=0):
    return HEAD.replace('</head>','<style>'+COMMON+css+'</style></head>')+f'<body><div class="slide {cls}" style="--mx:86px;--my:86px"><img class="logo" src="{LOGO}">{dots(idx)}{body}<div class="foot">Balero Creativo</div></div></body></html>'
def text(i,top,sz,txt,cls=''): return f'<div class="layer {cls}" id="{i}" style="left:86px;top:{top}px;font-size:{sz}px;line-height:1;">{txt}</div>'
def pill(): return '<div class="pill" id="lab">x</div>'
def btn(top,txt,sz=48): return f"<div id='btn' style=\"position:absolute;left:86px;top:{top}px;z-index:3;background:#111;color:#FFD23F;font:700 {sz}px 'Source Sans Pro',sans-serif;padding:16px 42px;border-radius:999px;box-shadow:0 10px 28px rgba(0,0,0,.25);opacity:0;transform-origin:0 50%\">{txt}</div>"
def tin(t,a,b=None): return eo(seg(t,a,a+(b or 0.55)))

# ---------- escenas ----------
SC={}
SC['s2']=dict(dur=5.6,idx=1,html=html(
  text('t1',200,64,'La home de Wish:','l')+text('t2',288,88,'MENÚ Y BUSCADOR')+text('t4',392,112,MARK('a la vista'))+laptop('home-fixed.png')+pill()))
SC['s3']=dict(dur=5.8,idx=2,html=html(
  text('t1',200,64,'Cada destino,','l')+text('t2',288,88,'SU PROPIA PÁGINA')+text('t4',392,112,MARK('De Roma a Sicilia'))+laptop('italia-full.png')+pill(),idx=2))
SC['s4']=dict(dur=5.0,idx=3,html=html(
  text('t1',200,64,'La idea del sitio:','l')+text('a1',380,100,'PORQUE TODO')+text('a2',496,100,'VIAJE COMIENZA')+text('a3',612,100,'CON')+text('a4',770,190,MARK('un deseo.','#FFD23F','#111'))
  +'<div class="layer l" id="a5" style="left:86px;top:1130px;font-size:40px;font-family:Source Sans Pro;text-transform:none;letter-spacing:0;color:#A9A4F7;font-weight:600">El concepto detrás del sitio de Wish Travel</div>',cls='bg-k',idx=3))
SC['s5']=dict(dur=5.2,idx=4,html=html(
  text('t1',260,64,'Tu turno:','l')+text('t2',350,120,'¿QUIERES UN')+text('t3',476,120,'SITIO ASÍ?')+text('t4',680,120,MARK('para tu negocio'))
  +btn(960,'Escríbenos →',60)+'<div class="layer l" id="u" style="left:86px;top:1120px;font-size:48px;">balerocreativo.com</div>',idx=4))

def js_s2(t):
    e=eo(seg(t,0,0.8)); lap=f"$('lp').style.translate='0 {160*(1-e)}px';$('lp').style.opacity={cl(e*1.6)};"
    z1=eio(seg(t,0.9,1.7))*(1-eio(seg(t,2.3,3.0))); z2=eio(seg(t,3.0,3.7))
    Wd,Ht=661,373
    tot=z1+z2
    sc=1+1.1*z1+1.3*z2
    if tot>1e-6:
        fx=(0.5*z1+0.27*z2)/tot; fy=(0.05*z1+0.70*z2)/tot
    else: fx,fy=0.5,0.5
    txp=max(Wd-Wd*sc,min(0,Wd/2-fx*Wd*sc)); typ=max(Ht-Ht*sc,min(0,Ht/2-fy*Ht*sc))
    inn=f"$('in').style.transform='translate({txp}px,{typ}px) scale({sc})';"
    # cursor
    c=eio(seg(t,3.6,4.5)); cx=400+(0.31*Wd-400+60)*0 ; 
    px=440+150*c; py=200+86*c   # llega al boton de busqueda
    cur=f"$('cur').style.opacity={eo(seg(t,3.5,3.8))};$('cur').style.left='{px}px';$('cur').style.top='{py}px';"
    r=seg(t,4.5,5.1); rip=f"$('rip').style.opacity={(1-r) if 0<r<1 else 0};$('rip').style.left='{px-18}px';$('rip').style.top='{py-18}px';$('rip').style.transform='scale({0.4+1.6*r})';"
    labs=[(1.2,2.7,'01 · Menú'),(3.2,5.5,'02 · Buscador')]
    return lap+inn+cur+rip,labs
def js_s3(t):
    e=eo(seg(t,0,0.8)); lap=f"$('lp').style.translate='0 {160*(1-e)}px';$('lp').style.opacity={cl(e*1.6)};"
    K=661/1440
    sy=-(250*K)*eio(seg(t,1.0,2.0)) -(1420*K)*eio(seg(t,2.6,4.8))
    sc=1+0.0
    inn=f"$('in').style.transform='translate(0px,{sy}px)';"
    return lap+inn,[(0.9,2.5,'01 · Destino'),(3.0,5.5,'02 · Día a día')]
def js_s4(t):
    s=''
    for k,(i,a) in enumerate([('t1',0.2),('a1',0.5),('a2',0.75),('a3',1.0),('a4',1.35),('a5',2.4)]):
        o=tin(t,a); s+=f"$('{i}').style.opacity={o};$('{i}').style.transform='translateY({36*(1-o)}px)';"
    return s,[]
def js_s5(t):
    s=''
    for i,a in [('t1',0.2),('t2',0.45),('t3',0.7),('t4',1.0),('u',2.0)]:
        o=tin(t,a); s+=f"$('{i}').style.opacity={o};$('{i}').style.transform='translateY({36*(1-o)}px)';"
    b=tin(t,1.6,0.6); pulse=1+0.05*math.sin((t-2.3)*2*math.pi*1.2)**2 if t>2.3 else 1
    s+=f"$('btn').style.opacity={b};$('btn').style.transform='scale({pulse*(0.92+0.08*b)})';"
    return s,[]
JS={'s2':js_s2,'s3':js_s3,'s4':js_s4,'s5':js_s5}

def render(name,only=None):
    sc=SC[name]; N=int(sc['dur']*FPS); out=f'{R}/fr_{name}'; os.makedirs(out,exist_ok=True)
    hp=f'{R}/{name}.html'; open(hp,'w',encoding='utf8').write(sc['html'])
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=b.new_page(viewport={'width':1080,'height':1440}); pg.goto('file://'+hp); pg.wait_for_timeout(1200)
        for f in range(N):
            if only and f not in only: continue
            t=f/FPS; body,labs=JS[name](t)
            lab_txt='';lab_op=0
            for a0,a1,txt in labs:
                o=eo(seg(t,a0,a0+0.35))*(1-eo(seg(t,a1-0.3,a1)))
                if o>lab_op: lab_op=o;lab_txt=txt
            lab=f"if(document.getElementById('lab')){{ if({lab_op}>0) $('lab').textContent={lab_txt!r};$('lab').style.opacity={lab_op};$('lab').style.transform='translateY({16*(1-lab_op)}px)';}}" if labs else ''
            pg.evaluate("()=>{const $=i=>document.getElementById(i);"+body+lab+"}")
            pg.screenshot(path=f'{out}/f{f:04d}.png')
        b.close()
if __name__=='__main__':
    name=sys.argv[1]; only=[int(a) for a in sys.argv[2:]] or None
    render(name,only)
