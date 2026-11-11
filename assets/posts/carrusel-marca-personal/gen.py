import os
D='/tmp/claude-0/-home-user-balero/e5dea3ae-5eb2-5590-8e46-102ca4555c6f/scratchpad/carrusel_personal'
BU,BR,CL,BE,LI,IN='#6F1F14','#A63A24','#E8B7A4','#EFE6D6','#C9F03B','#1E0F0B'
FONTS='''<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">'''
CSS='''*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:'Hanken Grotesk',sans-serif;-webkit-font-smoothing:antialiased}
.a{position:absolute}
.lab{left:80px;top:84px;font-family:'Familjen Grotesk';font-weight:600;font-size:34px;letter-spacing:.01em}
.h{font-family:'Familjen Grotesk';font-weight:700;line-height:.96;letter-spacing:-.045em}
.s{font-family:'Instrument Serif';font-style:italic;font-weight:400;letter-spacing:-.02em}
mark{background:#C9F03B;color:#6F1F14;border-radius:.16em;padding:.02em .14em .06em;display:inline-block;transform:rotate(-1deg)}
.foot{left:80px;right:80px;bottom:76px;display:flex;justify-content:space-between;font-family:'Familjen Grotesk';font-weight:700;font-size:38px}
.foot span:last-child{font-weight:500;font-size:34px}
.card{border-radius:44px;padding:40px 44px;display:flex;align-items:center;gap:32px}
.dot{width:110px;height:110px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Familjen Grotesk';font-weight:700;font-size:64px;flex:none}
.bub{border-radius:56px;padding:64px 60px}
'''
def page(n,bg,fg,labc,body):
    html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head>
<body style="background:{bg};color:{fg}">
<div class="a lab" style="color:{labc}">{body[0]}</div>
{body[1]}
<div class="a foot" style="color:{fg}"><span>Daniela Rubio</span><span>{n}/9</span></div>
</body></html>'''
    open(f'{D}/slide-{n}.html','w').write(html)

# 1 portada con retrato
page(1,IN,BE,LI,('Para tu Instagram personal',f'''
<div class="a" style="left:520px;top:640px;width:460px;height:560px"><svg viewBox="0 0 400 480" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><ellipse cx="200" cy="330" rx="118" ry="128" fill="#EFE6D6"/><circle cx="318.0" cy="330.0" r="30" fill="#EFE6D6"/><circle cx="313.2" cy="366.1" r="30" fill="#EFE6D6"/><circle cx="299.3" cy="399.2" r="30" fill="#EFE6D6"/><circle cx="277.3" cy="426.7" r="30" fill="#EFE6D6"/><circle cx="249.0" cy="446.4" r="30" fill="#EFE6D6"/><circle cx="216.8" cy="456.7" r="30" fill="#EFE6D6"/><circle cx="183.2" cy="456.7" r="30" fill="#EFE6D6"/><circle cx="151.0" cy="446.4" r="30" fill="#EFE6D6"/><circle cx="122.7" cy="426.7" r="30" fill="#EFE6D6"/><circle cx="100.7" cy="399.2" r="30" fill="#EFE6D6"/><circle cx="86.8" cy="366.1" r="30" fill="#EFE6D6"/><circle cx="82.0" cy="330.0" r="30" fill="#EFE6D6"/><circle cx="86.8" cy="293.9" r="30" fill="#EFE6D6"/><circle cx="100.7" cy="260.8" r="30" fill="#EFE6D6"/><circle cx="122.7" cy="233.3" r="30" fill="#EFE6D6"/><circle cx="151.0" cy="213.6" r="30" fill="#EFE6D6"/><circle cx="183.2" cy="203.3" r="30" fill="#EFE6D6"/><circle cx="216.8" cy="203.3" r="30" fill="#EFE6D6"/><circle cx="249.0" cy="213.6" r="30" fill="#EFE6D6"/><circle cx="277.3" cy="233.3" r="30" fill="#EFE6D6"/><circle cx="299.3" cy="260.8" r="30" fill="#EFE6D6"/><circle cx="313.2" cy="293.9" r="30" fill="#EFE6D6"/><ellipse cx="78" cy="310" rx="34" ry="60" fill="#EFE6D6" transform="rotate(18 78 310)"/><ellipse cx="322" cy="310" rx="34" ry="60" fill="#EFE6D6" transform="rotate(-18 322 310)"/><ellipse cx="200" cy="170" rx="104" ry="98" fill="#EFE6D6"/><circle cx="304.0" cy="170.0" r="26" fill="#EFE6D6"/><circle cx="298.9" cy="200.3" r="26" fill="#EFE6D6"/><circle cx="284.1" cy="227.6" r="26" fill="#EFE6D6"/><circle cx="261.1" cy="249.3" r="26" fill="#EFE6D6"/><circle cx="232.1" cy="263.2" r="26" fill="#EFE6D6"/><circle cx="200.0" cy="268.0" r="26" fill="#EFE6D6"/><circle cx="167.9" cy="263.2" r="26" fill="#EFE6D6"/><circle cx="138.9" cy="249.3" r="26" fill="#EFE6D6"/><circle cx="115.9" cy="227.6" r="26" fill="#EFE6D6"/><circle cx="101.1" cy="200.3" r="26" fill="#EFE6D6"/><circle cx="96.0" cy="170.0" r="26" fill="#EFE6D6"/><circle cx="101.1" cy="139.7" r="26" fill="#EFE6D6"/><circle cx="115.9" cy="112.4" r="26" fill="#EFE6D6"/><circle cx="138.9" cy="90.7" r="26" fill="#EFE6D6"/><circle cx="167.9" cy="76.8" r="26" fill="#EFE6D6"/><circle cx="200.0" cy="72.0" r="26" fill="#EFE6D6"/><circle cx="232.1" cy="76.8" r="26" fill="#EFE6D6"/><circle cx="261.1" cy="90.7" r="26" fill="#EFE6D6"/><circle cx="284.1" cy="112.4" r="26" fill="#EFE6D6"/><circle cx="298.9" cy="139.7" r="26" fill="#EFE6D6"/><circle cx="166" cy="172" r="12" fill="#1E0F0B"/><circle cx="234" cy="172" r="12" fill="#1E0F0B"/><ellipse cx="150" cy="200" rx="18" ry="11" fill="#E8B7A4" opacity=".9"/><ellipse cx="250" cy="200" rx="18" ry="11" fill="#E8B7A4" opacity=".9"/><path d="M186 196 Q200 212 214 196" stroke="#1E0F0B" stroke-width="7" fill="none" stroke-linecap="round"/><ellipse cx="150" cy="452" rx="46" ry="24" fill="#EFE6D6"/><ellipse cx="250" cy="452" rx="46" ry="24" fill="#EFE6D6"/></svg></div>
<div class="a" style="left:560px;top:520px;width:130px;height:130px"><svg viewBox="0 0 200 200" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="170" height="170" rx="36" fill="#EFE6D6"/><circle cx="95" cy="80" r="26" fill="#C8B9A4"/><path d="M50 160 Q95 105 140 160 Z" fill="#C8B9A4"/><circle cx="160" cy="40" r="30" fill="#C9F03B"/><rect x="146" y="36" width="28" height="8" rx="4" fill="#6F1F14"/><rect x="156" y="26" width="8" height="28" rx="4" fill="#6F1F14"/></svg></div>
<div class="a" style="left:840px;top:560px;width:130px;height:130px"><svg viewBox="0 0 200 200" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="170" height="170" rx="36" fill="#EFE6D6"/><circle cx="95" cy="80" r="26" fill="#C8B9A4"/><path d="M50 160 Q95 105 140 160 Z" fill="#C8B9A4"/><circle cx="160" cy="40" r="30" fill="#E8B7A4"/><rect x="146" y="36" width="28" height="8" rx="4" fill="#6F1F14"/></svg></div>
<div class="a h" style="left:80px;top:200px;font-size:132px;width:920px;color:{BE}">¿Quién te dejó de <span class="s" style="color:{LI};font-size:150px">seguir?</span></div>
<div class="a" style="left:80px;top:760px;width:440px;font-size:42px;line-height:1.3;color:{BE}">Cada día, en un solo mensaje.</div>
'''))
# 2 beige: tres tarjetas
cards=''
for i,(t,bgc,txt,sym) in enumerate([('Se fue',LI,BU,'−'),('Llegó',CL,BU,'+'),('Cuántos',LI,BU,'#')]):
    y=640+i*190
    cards+=f'<div class="a card" style="left:80px;top:{y}px;width:920px;height:160px;background:#FAF3E6"><div class="dot" style="background:{bgc};color:{txt}">{sym}</div><div class="h" style="font-size:72px;color:{BU}">{t}</div></div>'
page(2,BE,BU,BR,('Muse te lo dice cada día',f'''
<div class="a h" style="left:80px;top:220px;font-size:150px;width:940px;color:{BU}">¿Qué te <span class="s" style="color:{BR};font-size:164px">dice?</span></div>
{cards}
'''))
# 3 burnt: prompt 1
page(3,BU,BE,LI,('Guarda este prompt · 1 de 2',f'''
<div class="a" style="left:730px;top:640px;width:290px;height:340px"><svg viewBox="0 0 400 480" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><ellipse cx="200" cy="330" rx="118" ry="128" fill="#EFE6D6"/><circle cx="318.0" cy="330.0" r="30" fill="#EFE6D6"/><circle cx="313.2" cy="366.1" r="30" fill="#EFE6D6"/><circle cx="299.3" cy="399.2" r="30" fill="#EFE6D6"/><circle cx="277.3" cy="426.7" r="30" fill="#EFE6D6"/><circle cx="249.0" cy="446.4" r="30" fill="#EFE6D6"/><circle cx="216.8" cy="456.7" r="30" fill="#EFE6D6"/><circle cx="183.2" cy="456.7" r="30" fill="#EFE6D6"/><circle cx="151.0" cy="446.4" r="30" fill="#EFE6D6"/><circle cx="122.7" cy="426.7" r="30" fill="#EFE6D6"/><circle cx="100.7" cy="399.2" r="30" fill="#EFE6D6"/><circle cx="86.8" cy="366.1" r="30" fill="#EFE6D6"/><circle cx="82.0" cy="330.0" r="30" fill="#EFE6D6"/><circle cx="86.8" cy="293.9" r="30" fill="#EFE6D6"/><circle cx="100.7" cy="260.8" r="30" fill="#EFE6D6"/><circle cx="122.7" cy="233.3" r="30" fill="#EFE6D6"/><circle cx="151.0" cy="213.6" r="30" fill="#EFE6D6"/><circle cx="183.2" cy="203.3" r="30" fill="#EFE6D6"/><circle cx="216.8" cy="203.3" r="30" fill="#EFE6D6"/><circle cx="249.0" cy="213.6" r="30" fill="#EFE6D6"/><circle cx="277.3" cy="233.3" r="30" fill="#EFE6D6"/><circle cx="299.3" cy="260.8" r="30" fill="#EFE6D6"/><circle cx="313.2" cy="293.9" r="30" fill="#EFE6D6"/><ellipse cx="78" cy="310" rx="34" ry="60" fill="#EFE6D6" transform="rotate(18 78 310)"/><ellipse cx="322" cy="310" rx="34" ry="60" fill="#EFE6D6" transform="rotate(-18 322 310)"/><ellipse cx="200" cy="170" rx="104" ry="98" fill="#EFE6D6"/><circle cx="304.0" cy="170.0" r="26" fill="#EFE6D6"/><circle cx="298.9" cy="200.3" r="26" fill="#EFE6D6"/><circle cx="284.1" cy="227.6" r="26" fill="#EFE6D6"/><circle cx="261.1" cy="249.3" r="26" fill="#EFE6D6"/><circle cx="232.1" cy="263.2" r="26" fill="#EFE6D6"/><circle cx="200.0" cy="268.0" r="26" fill="#EFE6D6"/><circle cx="167.9" cy="263.2" r="26" fill="#EFE6D6"/><circle cx="138.9" cy="249.3" r="26" fill="#EFE6D6"/><circle cx="115.9" cy="227.6" r="26" fill="#EFE6D6"/><circle cx="101.1" cy="200.3" r="26" fill="#EFE6D6"/><circle cx="96.0" cy="170.0" r="26" fill="#EFE6D6"/><circle cx="101.1" cy="139.7" r="26" fill="#EFE6D6"/><circle cx="115.9" cy="112.4" r="26" fill="#EFE6D6"/><circle cx="138.9" cy="90.7" r="26" fill="#EFE6D6"/><circle cx="167.9" cy="76.8" r="26" fill="#EFE6D6"/><circle cx="200.0" cy="72.0" r="26" fill="#EFE6D6"/><circle cx="232.1" cy="76.8" r="26" fill="#EFE6D6"/><circle cx="261.1" cy="90.7" r="26" fill="#EFE6D6"/><circle cx="284.1" cy="112.4" r="26" fill="#EFE6D6"/><circle cx="298.9" cy="139.7" r="26" fill="#EFE6D6"/><circle cx="166" cy="172" r="12" fill="#1E0F0B"/><circle cx="234" cy="172" r="12" fill="#1E0F0B"/><ellipse cx="150" cy="200" rx="18" ry="11" fill="#E8B7A4" opacity=".9"/><ellipse cx="250" cy="200" rx="18" ry="11" fill="#E8B7A4" opacity=".9"/><path d="M186 196 Q200 212 214 196" stroke="#1E0F0B" stroke-width="7" fill="none" stroke-linecap="round"/><ellipse cx="150" cy="452" rx="46" ry="24" fill="#EFE6D6"/><ellipse cx="250" cy="452" rx="46" ry="24" fill="#EFE6D6"/></svg></div>
<div class="a h" style="left:80px;top:200px;font-size:150px;width:900px;color:{BE}">Copia <span class="s" style="color:{LI};font-size:166px">y pega.</span></div>
<div class="a bub" style="left:80px;top:680px;width:600px;height:400px;background:#FAF3E6;color:{BU};font-size:48px;line-height:1.35;font-weight:500">Quiero saber cada día quién me dejó de seguir y quién me empezó a seguir en Instagram.</div>
'''))
# 4 beige: prompt 2
page(4,BE,BU,BR,('Guarda este prompt · 2 de 2',f'''
<div class="a" style="left:720px;top:560px;width:300px;height:360px"><svg viewBox="0 0 400 480" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><ellipse cx="200" cy="330" rx="118" ry="128" fill="#EFE6D6"/><circle cx="318.0" cy="330.0" r="30" fill="#EFE6D6"/><circle cx="313.2" cy="366.1" r="30" fill="#EFE6D6"/><circle cx="299.3" cy="399.2" r="30" fill="#EFE6D6"/><circle cx="277.3" cy="426.7" r="30" fill="#EFE6D6"/><circle cx="249.0" cy="446.4" r="30" fill="#EFE6D6"/><circle cx="216.8" cy="456.7" r="30" fill="#EFE6D6"/><circle cx="183.2" cy="456.7" r="30" fill="#EFE6D6"/><circle cx="151.0" cy="446.4" r="30" fill="#EFE6D6"/><circle cx="122.7" cy="426.7" r="30" fill="#EFE6D6"/><circle cx="100.7" cy="399.2" r="30" fill="#EFE6D6"/><circle cx="86.8" cy="366.1" r="30" fill="#EFE6D6"/><circle cx="82.0" cy="330.0" r="30" fill="#EFE6D6"/><circle cx="86.8" cy="293.9" r="30" fill="#EFE6D6"/><circle cx="100.7" cy="260.8" r="30" fill="#EFE6D6"/><circle cx="122.7" cy="233.3" r="30" fill="#EFE6D6"/><circle cx="151.0" cy="213.6" r="30" fill="#EFE6D6"/><circle cx="183.2" cy="203.3" r="30" fill="#EFE6D6"/><circle cx="216.8" cy="203.3" r="30" fill="#EFE6D6"/><circle cx="249.0" cy="213.6" r="30" fill="#EFE6D6"/><circle cx="277.3" cy="233.3" r="30" fill="#EFE6D6"/><circle cx="299.3" cy="260.8" r="30" fill="#EFE6D6"/><circle cx="313.2" cy="293.9" r="30" fill="#EFE6D6"/><ellipse cx="78" cy="310" rx="34" ry="60" fill="#EFE6D6" transform="rotate(18 78 310)"/><ellipse cx="322" cy="310" rx="34" ry="60" fill="#EFE6D6" transform="rotate(-18 322 310)"/><ellipse cx="200" cy="170" rx="104" ry="98" fill="#EFE6D6"/><circle cx="304.0" cy="170.0" r="26" fill="#EFE6D6"/><circle cx="298.9" cy="200.3" r="26" fill="#EFE6D6"/><circle cx="284.1" cy="227.6" r="26" fill="#EFE6D6"/><circle cx="261.1" cy="249.3" r="26" fill="#EFE6D6"/><circle cx="232.1" cy="263.2" r="26" fill="#EFE6D6"/><circle cx="200.0" cy="268.0" r="26" fill="#EFE6D6"/><circle cx="167.9" cy="263.2" r="26" fill="#EFE6D6"/><circle cx="138.9" cy="249.3" r="26" fill="#EFE6D6"/><circle cx="115.9" cy="227.6" r="26" fill="#EFE6D6"/><circle cx="101.1" cy="200.3" r="26" fill="#EFE6D6"/><circle cx="96.0" cy="170.0" r="26" fill="#EFE6D6"/><circle cx="101.1" cy="139.7" r="26" fill="#EFE6D6"/><circle cx="115.9" cy="112.4" r="26" fill="#EFE6D6"/><circle cx="138.9" cy="90.7" r="26" fill="#EFE6D6"/><circle cx="167.9" cy="76.8" r="26" fill="#EFE6D6"/><circle cx="200.0" cy="72.0" r="26" fill="#EFE6D6"/><circle cx="232.1" cy="76.8" r="26" fill="#EFE6D6"/><circle cx="261.1" cy="90.7" r="26" fill="#EFE6D6"/><circle cx="284.1" cy="112.4" r="26" fill="#EFE6D6"/><circle cx="298.9" cy="139.7" r="26" fill="#EFE6D6"/><circle cx="166" cy="172" r="12" fill="#1E0F0B"/><circle cx="234" cy="172" r="12" fill="#1E0F0B"/><ellipse cx="150" cy="200" rx="18" ry="11" fill="#E8B7A4" opacity=".9"/><ellipse cx="250" cy="200" rx="18" ry="11" fill="#E8B7A4" opacity=".9"/><path d="M186 196 Q200 212 214 196" stroke="#1E0F0B" stroke-width="7" fill="none" stroke-linecap="round"/><ellipse cx="150" cy="452" rx="46" ry="24" fill="#EFE6D6"/><ellipse cx="250" cy="452" rx="46" ry="24" fill="#EFE6D6"/></svg></div>
<div class="a h" style="left:80px;top:200px;font-size:140px;width:920px;color:{BU}">Y cada día <span class="s" style="color:{BR};font-size:150px">te dice…</span></div>
<div class="a bub" style="left:80px;top:640px;width:920px;height:460px;background:#FAF3E6;color:{BU};font-size:44px;line-height:1.38;font-weight:500">La fecha, cuántos seguidores tengo hoy, quiénes se fueron, quiénes llegaron y el cambio neto. Si no hubo cambios, dilo claramente. No inventes nombres ni cantidades.
<div class="a dot" style="right:50px;bottom:40px;width:120px;height:120px;background:{LI};color:{BU};font-size:70px">✓</div></div>
'''))
# 5 burnt: tres momentos con círculos
circ=''
for i,(t,bgc,cap) in enumerate([('Hoy',BE,'Se guarda tu lista'),('Mañana',CL,'Se compara con hoy'),('Cada día',LI,'Te llega el reporte')]):
    x=80+i*315
    circ+=f'<div class="a" style="left:{x}px;top:760px;width:290px;height:290px;border-radius:50%;background:{bgc};display:flex;align-items:center;justify-content:center;font-family:Familjen Grotesk;font-weight:700;font-size:44px;color:{BU}">{t}</div>'
    circ+=f'<div class="a" style="left:{x}px;top:1090px;width:290px;text-align:center;font-size:36px;line-height:1.3;color:{BE}">{cap}</div>'
page(5,IN,BE,LI,('Así funciona',f'''
<div class="a h" style="left:80px;top:200px;font-size:124px;width:920px;color:{BE}">Hoy, mañana <span class="s" style="color:{LI};font-size:138px">y cada día.</span></div>
{circ}
'''))
# 6 beige: reporte
page(6,BE,BU,BR,('Así se ve el reporte · ejemplo',f'''
<div class="a h" style="left:80px;top:200px;font-size:130px;width:920px;color:{BU}">Un reporte <span class="s" style="color:{BR};font-size:140px">así.</span></div>
<div class="a" style="left:240px;top:560px;width:600px;height:640px;border-radius:56px;background:#FAF3E6;padding:60px 56px;color:{BU}">
<div class="h" style="font-size:52px">Hoy</div>
<div style="font-size:44px;margin-top:40px">Seguidores <b>470</b></div>
<div style="font-size:44px;margin-top:30px;display:flex;align-items:center;gap:20px"><span style="width:34px;height:34px;border-radius:50%;background:{BR};display:inline-block"></span>Se fueron <b>2</b></div>
<div style="font-size:44px;margin-top:24px;display:flex;align-items:center;gap:20px"><span style="width:34px;height:34px;border-radius:50%;background:{LI};display:inline-block"></span>Llegaron <b>3</b></div>
<div class="h" style="font-size:64px;margin-top:60px">Neto +1</div>
</div>'''))
# 7 burnt: lo que necesitas
items=''
for i,t in enumerate(['Tu Instagram conectada','El prompt guardado','Nada más']):
    y=680+i*190
    items+=f'<div class="a dot" style="left:80px;top:{y}px;width:110px;height:110px;background:{LI};color:{BU};font-size:64px">✓</div><div class="a" style="left:230px;top:{y+18}px;font-size:58px;color:{BE};font-weight:500;width:760px">{t}</div>'
page(7,IN,BE,LI,('Lo que necesitas',f'''
<div class="a h" style="left:80px;top:200px;font-size:170px;width:920px;color:{BE}">Solo <span class="s" style="color:{LI};font-size:186px">esto.</span></div>
{items}
'''))
# 8 beige: cierre con retrato
page(8,BE,BU,BR,('Para ti, que me lees',f'''
<div class="a h" style="left:80px;top:200px;font-size:124px;width:520px;color:{BU}">Guárdalo para <span class="s" style="color:{BR};font-size:136px">mañana.</span></div>
<div class="a" style="left:80px;top:830px;width:500px;font-size:46px;line-height:1.3;color:{BU}">Comenta <b>PROMPT</b> y te lo paso por DM.</div>
<div class="a h" style="left:80px;top:1040px;font-size:72px;color:{BR}">@rubiagz</div>
<div class="a" style="left:600px;top:200px;width:400px;height:700px;border-radius:200px 200px 0 0;overflow:hidden">
<img src="retrato.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 30%"></div>
'''))
# 9 burnt: código propio de la autora (confirmado por ella), texto original
page(9,BU,BE,LI,('Herramienta que uso',f'''
<div class="a h" style="left:80px;top:200px;font-size:130px;width:920px;color:{BE}">Pruébala con <span class="s" style="color:{LI};font-size:140px">mi código.</span></div>
<div class="a bub" style="left:80px;top:700px;width:920px;height:300px;background:#FAF3E6;color:{BU};font-size:44px;line-height:1.35;font-weight:500">Mi código: <b>ECOKCV</b><br><span style="font-size:36px;color:{BR}">Canjéalo en la configuración de Muse dentro del plazo que indica la app.</span></div>
'''))
