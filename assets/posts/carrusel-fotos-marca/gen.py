import os
D=os.path.dirname(os.path.abspath(__file__))
BU,BR,CL,BE,LI,IN='#6F1F14','#A63A24','#E8B7A4','#EFE6D6','#C9F03B','#1E0F0B'
FONTS='''<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'''
CSS='''*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:'Hanken Grotesk',sans-serif;-webkit-font-smoothing:antialiased}
.a{position:absolute}
.h{font-family:'Familjen Grotesk';font-weight:700;line-height:.96;letter-spacing:-.045em}
.s{font-family:'Instrument Serif';font-style:italic;font-weight:400;letter-spacing:-.02em}
.lab{left:80px;top:84px;font-family:'Familjen Grotesk';font-weight:600;font-size:34px}
.foot{left:80px;right:80px;bottom:76px;display:flex;justify-content:space-between;font-family:'Familjen Grotesk';font-weight:700;font-size:38px}
.foot span:last-child{font-weight:500;font-size:34px}
.photo{border-radius:44px;display:flex;align-items:center;justify-content:center;text-align:center;font-family:'Familjen Grotesk';font-weight:600;font-size:34px;line-height:1.3;padding:30px}
.card{border-radius:44px;padding:36px 44px;display:flex;align-items:center;gap:30px;background:#FAF3E6}
.dot{width:100px;height:100px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Familjen Grotesk';font-weight:700;font-size:56px;flex:none}
.bub{border-radius:56px;padding:56px 60px;background:#FAF3E6}
'''
def page(n,bg,fg,labc,label,body):
    html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head>
<body style="background:{bg};color:{fg}">
<div class="a lab" style="color:{labc}">{label}</div>
{body}
<div class="a foot" style="color:{fg}"><span>Daniela Rubio</span><span>{n}/9</span></div>
</body></html>'''
    open(f'{D}/slide-{n}.html','w').write(html)
def ph(l,t,w,h,txt,bg='#FAF3E6',col=BU):
    return f'<div class="a photo" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;background:{bg};color:{col}">{txt}</div>'
page(1,IN,BE,LI,'Para tu cuenta de Instagram',f'''
<div class="a h" style="left:80px;top:200px;font-size:124px;width:920px;color:{BE}">¿Cuántas personas dejaron de <span class="s" style="color:{LI};font-size:138px">seguirte</span> esta semana?</div>
{ph(80,790,920,390,"FOTO 1<br>Tu foto en el escritorio o en acción (vertical, 4:5)","#2B1A14",BE)}
''')
page(2,BE,BU,BR,'Instagram no te lo dice a diario',f'''
<div class="a h" style="left:80px;top:200px;font-size:140px;width:920px;color:{BU}">¿Y tú <span class="s" style="color:{BR};font-size:150px">lo sabes?</span></div>
<div class="a card" style="left:80px;top:640px;width:920px;height:150px"><div class="dot" style="background:{LI};color:{BU}">−</div><div class="h" style="font-size:66px;color:{BU}">Quién se fue</div></div>
<div class="a card" style="left:80px;top:820px;width:920px;height:150px"><div class="dot" style="background:{CL};color:{BU}">+</div><div class="h" style="font-size:66px;color:{BU}">Quién llegó</div></div>
<div class="a card" style="left:80px;top:1000px;width:920px;height:150px"><div class="dot" style="background:{LI};color:{BU}">#</div><div class="h" style="font-size:66px;color:{BU}">Cuántos en total</div></div>
''')
page(3,BU,BE,LI,'Paso 1',f'''
<div class="a h" style="left:80px;top:200px;font-size:150px;width:920px;color:{BE}">Guarda tu <span class="s" style="color:{LI};font-size:166px">lista.</span></div>
<div class="a bub" style="left:80px;top:690px;width:600px;height:330px;color:{BU};font-size:44px;line-height:1.35;font-weight:500">Copia tus seguidores actuales y guárdalos como punto de partida.</div>
{ph(720,640,280,420,"FOTO 2<br>Captura de tu lista de seguidores (vertical)",BE,BU)}
''')
page(4,BE,BU,BR,'Paso 2',f'''
<div class="a h" style="left:80px;top:200px;font-size:150px;width:920px;color:{BU}">Compara <span class="s" style="color:{BR};font-size:166px">cada día.</span></div>
<div class="a bub" style="left:80px;top:690px;width:920px;height:300px;color:{BU};font-size:44px;line-height:1.35;font-weight:500">Cada día mira quién se fue, quién llegó y cuál fue el cambio neto. Si no hubo cambios, anótalo.</div>
{ph(80,1030,920,190,"FOTO 3<br>Tu escritorio con la libreta o el celular (horizontal)",BE,BU)}
''')
page(5,IN,BE,LI,'Así funciona',f'''
<div class="a h" style="left:80px;top:200px;font-size:124px;width:920px;color:{BE}">Hoy, mañana <span class="s" style="color:{LI};font-size:138px">y cada día.</span></div>
<div class="a" style="left:80px;top:760px;width:290px;height:290px;border-radius:50%;background:{BE};display:flex;align-items:center;justify-content:center;font-family:'Familjen Grotesk';font-weight:700;font-size:44px;color:{BU}">Hoy</div>
<div class="a" style="left:395px;top:760px;width:290px;height:290px;border-radius:50%;background:{CL};display:flex;align-items:center;justify-content:center;font-family:'Familjen Grotesk';font-weight:700;font-size:44px;color:{BU}">Mañana</div>
<div class="a" style="left:710px;top:760px;width:290px;height:290px;border-radius:50%;background:{LI};display:flex;align-items:center;justify-content:center;font-family:'Familjen Grotesk';font-weight:700;font-size:44px;color:{BU}">Cada día</div>
<div class="a" style="left:80px;top:1090px;width:920px;font-size:36px;color:{BE}">Guardas la lista, la comparas con el día anterior y revisas el reporte.</div>
''')
page(6,BE,BU,BR,'Ejemplo · cifras hipotéticas',f'''
<div class="a h" style="left:80px;top:200px;font-size:130px;width:920px;color:{BU}">Un reporte <span class="s" style="color:{BR};font-size:140px">así.</span></div>
<div class="a card" style="left:80px;top:500px;width:560px;height:640px;flex-direction:column;align-items:flex-start;justify-content:flex-start;padding:50px;border-radius:56px">
<div class="h" style="font-size:52px;color:{BU}">Hoy</div>
<div style="font-size:44px;margin-top:34px;color:{BU}">Seguidores <b>470</b></div>
<div style="font-size:44px;margin-top:24px;color:{BU}">Se fueron <b>2</b></div>
<div style="font-size:44px;margin-top:16px;color:{BU}">Llegaron <b>3</b></div>
<div class="h" style="font-size:60px;margin-top:40px;color:{BR}">Neto +1</div></div>
{ph(680,500,320,640,"FOTO 4<br>Captura real de tu reporte (vertical, con datos tapados)",BU,BE)}
''')
page(7,IN,BE,LI,'Lo que necesitas',f'''
<div class="a h" style="left:80px;top:200px;font-size:170px;width:920px;color:{BE}">Solo <span class="s" style="color:{LI};font-size:186px">esto.</span></div>
<div class="a dot" style="left:80px;top:680px;background:{LI};color:{BU}">✓</div><div class="a" style="left:230px;top:700px;font-size:58px;color:{BE};font-weight:500">Tu cuenta de Instagram</div>
<div class="a dot" style="left:80px;top:870px;background:{LI};color:{BU}">✓</div><div class="a" style="left:230px;top:890px;font-size:58px;color:{BE};font-weight:500">La lista guardada</div>
<div class="a dot" style="left:80px;top:1060px;background:{LI};color:{BU}">✓</div><div class="a" style="left:230px;top:1080px;font-size:58px;color:{BE};font-weight:500">Diez minutos al día</div>
''')
page(8,BE,BU,BR,'Para ti, que me lees',f'''
<div class="a h" style="left:80px;top:200px;font-size:124px;width:520px;color:{BU}">Guárdalo para <span class="s" style="color:{BR};font-size:136px">mañana.</span></div>
<div class="a" style="left:80px;top:830px;width:500px;font-size:46px;line-height:1.3;color:{BU}">Escríbeme y revisamos tu cuenta juntas.</div>
<div class="a h" style="left:80px;top:1040px;font-size:72px;color:{BR}">@rubiagz</div>
<div class="a" style="left:600px;top:200px;width:400px;height:700px;border-radius:200px 200px 0 0;overflow:hidden"><img src="retrato.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 30%"></div>
''')
page(9,BU,BE,LI,'Herramienta que uso',f'''
<div class="a h" style="left:80px;top:200px;font-size:130px;width:920px;color:{BE}">[TU HERRAMIENTA] <span class="s" style="color:{LI};font-size:140px">[tu beneficio].</span></div>
<div class="a bub" style="left:80px;top:700px;width:920px;height:300px;color:{BU};font-size:44px;line-height:1.35;font-weight:500">[TU CÓDIGO O ENLACE]<br><span style="font-size:36px;color:{BR}">[VERIFICAR: condiciones oficiales antes de publicar]</span></div>
''')
