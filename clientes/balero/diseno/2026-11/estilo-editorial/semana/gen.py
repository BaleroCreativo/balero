import re,sys,os
src=open('trust-editorial-v2.html').read()
CSS=src.split('<style>')[1].split('</style>')[0]
CSS+="""
.stat{position:absolute;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316;padding:26px 32px}
.stat b{display:block;font:800 76px/1 Poppins;letter-spacing:-.02em}
.stat span{display:block;font:600 32px/1.2 'Source Sans Pro';margin-top:10px;color:#151316}
.row2{position:absolute;left:86px;right:86px;height:96px;background:#fff;border:4px solid #151316;border-radius:22px;box-shadow:8px 9px 0 #151316;font:700 38px/88px 'Source Sans Pro';padding-left:130px}
.row2 i{position:absolute;left:26px;top:14px;width:54px;height:54px;border-radius:50%;background:#FFD23F;border:4px solid #151316;font:800 28px/46px Poppins;text-align:center;font-style:normal}
.sticker{position:absolute;background:#FFD23F;border:4px solid #151316;border-radius:60px;padding:14px 34px;font:800 30px Poppins;box-shadow:6px 7px 0 #151316;transform:rotate(-4deg)}
.sc{position:absolute;font:800 72px Poppins}
.t{line-height:1.14!important}
.cmp.bad{opacity:1!important;background:#fff;border-style:dashed;box-shadow:none}
.cmp.bad .m{background:#151316}
.cmp.bad small{color:#3d3a42}
.cmp small{font-size:28px!important;color:#3d3a42}
.mini2 small{font-size:26px!important;color:#3d3a42}
.dots i{width:20px!important;height:20px!important}.dots{gap:12px!important}
.foot{font-size:32px!important}
.lbl{position:absolute;font:800 32px Poppins;letter-spacing:.06em;text-transform:uppercase}
.meter{position:absolute;left:86px;right:86px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316;overflow:hidden}

.bigy{position:absolute;left:86px;font:800 330px/.9 Poppins;background:#FFD23F;padding:10px 30px 24px;letter-spacing:-.04em}
"""
LOGO='<img class="logo" src="/home/user/balero/.claude/skills/balero-imagenes/assets/logo-balero.png">'
FOOT='<div class="foot"><span>Balero Creativo</span></div>'
def foot(note=''):
    n=f'<div style="position:absolute;right:86px;bottom:70px;font:700 30px \'Source Sans Pro\';color:#3d3a42;text-align:right;max-width:640px">{note}</div>' if note else ''
    return FOOT+n
def dots(i,n): return '<div class="dots">'+''.join(f'<i style="background:{"#151316" if k==i else "#cfc9dc"}"></i>' for k in range(n))+'</div>'
def hl(w): return f'<span class="serif" style="font-size:1.25em;text-transform:none;font-weight:400;background:#FFD23F;padding:0 18px">{w}</span>'
def lil(w,size=''): return f'<span class="hl">{w}</span>'
def chip(t): return f'<div class="chip">{t}</div>'
def kick(t): return f'<div class="kick" style="top:170px">{t}</div>'
def title(a,b=None,sz=100,top=290):
    return f'<div class="t" style="top:{top}px;font-size:{sz}px">{a}'+(f'<br>{b}' if b else '')+'</div>'
def body(t,top=610): return f'<div class="body" style="top:{top}px;width:880px">{t}</div>'
def serif(t,top,size=104): return f'<div class="serif" style="position:absolute;left:86px;top:{top}px;font-size:{size}px;line-height:1">{t}</div>'
def big(t,top,size=70,lh=1.08): return f'<div class="big" style="top:{top}px;font-size:{size}px;line-height:{lh}">{t}</div>'
def cmp(top,cls,sym,label,txt,h=230): return f'<div class="cmp {cls}" style="top:{top}px;height:{h}px"><div class="m">{sym}</div><div><small>{label}</small>{txt}</div></div>'
def tape(text,top=1150): return f'<div class="tape" style="top:{top}px;font-family:Poppins;font-weight:800;font-size:36px">{text}</div><div class="arrow" style="top:{top}px;transform:translateY(22px)">→</div>'
def stat(x,y,w,h,num,lab,bg='#fff',fs=76): return f'<div class="stat" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg}"><b style="font-size:{fs}px">{num}</b><span>{lab}</span></div>'
def row2(top,sym,txt,bg=''): return f'<div class="row2" style="top:{top}px;{("background:"+bg) if bg else ""}"><i>{sym}</i>{txt}</div>'
def mini(x,y,w,h,lab,txt,bg='#fff',bad=False):
    st='opacity:.6;border-style:dashed;' if bad else 'box-shadow:8px 9px 0 #151316;'
    return f'<div class="mini2" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{st}"><small>{lab}</small>{txt}</div>'
def sticker(t,x,y,rot=-4): return f'<div class="sticker" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)">{t}</div>'
def build(name,slides):
    n=len(slides)
    secs=''.join(f'<div class="s" id="s{i+1}">{dots(i,n)}{LOGO}{b}{f}</div>' for i,(b,f) in enumerate(slides))
    h='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="/home/user/balero/.claude/skills/balero-imagenes/fonts/fonts.css"><style>'+CSS+'</style></head><body>'+secs+'</body></html>'
    open(f'semana/{name}.html','w').write(h)
    return n
