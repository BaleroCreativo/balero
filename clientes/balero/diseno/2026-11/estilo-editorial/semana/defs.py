from gen import *
F=foot()
DESL='<div style="position:absolute;right:86px;bottom:70px;font:800 30px Poppins;letter-spacing:.14em">DESLIZA →</div>'
FD=FOOT+DESL
def cmpx(a,b,t1=800,t2=1040,h=230): return a+b
def sig(n,a,b,txt,bad,good,sz=100,top=800):
    return f'<div class="chip">SEÑAL {n}</div>'+title(a,b,sz)+body(txt)+cmp(top,'bad','✗','ASÍ NO',bad,230)+cmp(top+270,'good','✓','ASÍ SÍ',good,230)
def mcards(items,top,h=300):
    pass
# ---------- ROAS ----------
roas=[
 (kick('Publicidad digital')+serif('Un ROAS de 8',290,100)+big('PUEDE GANAR MENOS',420,70)+serif('<span class="hl">que uno de 5.</span>',525,104)+'<div style="position:absolute;left:70px;top:780px;width:450px;height:430px;background:#FFD23F;border:5px solid #151316;border-radius:34px;box-shadow:14px 16px 0 #151316;transform:rotate(-5deg);overflow:hidden"><div style="font:800 34px Poppins;letter-spacing:.14em;padding:26px 0 0 34px">ROAS</div><div style="font:800 430px/0.82 Poppins;position:absolute;left:30px;bottom:6px">8</div></div>'+'<div style="position:absolute;left:520px;top:720px;width:480px;height:520px;background:#B9A3E8;border:5px solid #151316;border-radius:34px;box-shadow:14px 16px 0 #151316;transform:rotate(4deg);overflow:hidden"><div style="font:800 34px Poppins;letter-spacing:.14em;padding:26px 0 0 34px">ROAS</div><div style="font:800 500px/0.82 Poppins;position:absolute;left:30px;bottom:6px">5</div></div>'+'<div style="position:absolute;left:408px;top:1000px;width:150px;height:150px;border-radius:50%;background:#151316;color:#FFD23F;font:800 54px/150px Poppins;text-align:center;transform:rotate(-8deg)">VS</div>', FD),
 (chip('LA FÓRMULA')+title('Ventas entre',hl('inversión.'),100)+body('Eso es el ROAS: lo que vendes dividido entre lo que inviertes en anuncios.')+
   stat(86,780,250,280,'$2,000','ventas',fs=58)+'<div class="sc" style="left:350px;top:890px">÷</div>'+stat(420,780,250,280,'$400','inversión',fs=58)+'<div class="sc" style="left:684px;top:890px">=</div>'+stat(748,780,246,280,'5','ROAS','#B9A3E8',fs=96)+
   serif('Por cada <span class="hl">$1</span> invertido,',1130,62)+serif('$5 en ventas.',1205,62), foot('Ejemplo ilustrativo')),
 (chip('EL PUNTO CIEGO')+title('El panel no ve','tus '+hl('costos.'))+body('No sabe cuánto te cuesta vender ni tus gastos fijos. Un ROAS de 3 puede ser bueno para uno y pérdida para otro.')+
   cmp(815,'good','✓','NEGOCIO A · ROAS 3','Le deja ganancia',190)+cmp(1025,'bad','✗','NEGOCIO B · ROAS 3','Pierde dinero',190)+serif('El mismo número, dos resultados.',1240,50), F),
 (chip('TU NÚMERO')+title('Tu ROAS mínimo:','dejar de '+hl('perder.'),100)+body('Es el ROAS donde dejas de perder. Por encima ganas, por debajo pierdes, aunque el panel se vea bien.')+
   '<div style="position:absolute;left:86px;top:830px;width:908px;height:200px;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316;overflow:hidden;background:#fff;display:flex"><div style="width:50%;background:#e6e1ef;font:800 40px/200px Poppins;text-align:center;letter-spacing:.1em">PIERDES</div><div style="width:50%;background:#B9A3E8;font:800 40px/200px Poppins;text-align:center;letter-spacing:.1em">GANAS</div></div>'+
   '<div style="position:absolute;left:515px;top:790px;width:50px;height:280px;background:#151316;border-radius:25px"></div>'+sticker('Tu ROAS mínimo',356,1110,-3)+serif('Sale de tus costos, no del panel.',1240,50), F),
 (chip('ESCALA')+title('¿Más ROAS =','más '+hl('ganancia?'),100)+body('No siempre: un ROAS de 8 con $500 puede dejar menos que uno de 5 con $10,000.')+
   stat(86,900,420,380,'ROAS 8','inviertes $500<br>ventas $4,000',fs=70)+stat(574,760,420,520,'ROAS 5','inviertes $10,000<br>ventas $50,000','#B9A3E8',fs=70), foot('Ejemplo ilustrativo')),
 (kick('Antes de invertir más')+serif('¿Sabes cuál es tu',270,104)+'<div class="t" style="top:420px;font-size:104px"><span class="hl">ROAS mínimo?</span></div>'+body('Calcúlalo antes de subir tu presupuesto.',620)+
   row2(800,'1','Suma lo que te cuesta vender')+row2(970,'2','Busca el ROAS donde dejas de perder')+tape('Diagnóstico gratis de 15 minutos',1150), foot('Los números son ejemplos ilustrativos')),
]
# ---------- STANFORD ----------
def hrow(top,h,num,lab,bg='#fff',fs=64):
    return f'<div style="position:absolute;left:86px;top:{top}px;width:908px;height:{h}px;background:{bg};border:4px solid #151316;border-radius:26px;box-shadow:8px 9px 0 #151316;display:flex;flex-direction:row;align-items:center;gap:34px;padding:0 44px"><div style="font:800 {fs}px/1 Poppins;min-width:370px;white-space:nowrap">{num}</div><div style="font:600 34px/1.2 \'Source Sans Pro\',sans-serif">{lab}</div></div>'
def hcmp(top,cls,sym,lab,txt,h=190):
    return f'<div class="cmp {cls}" style="top:{top}px;height:{h}px"><div class="m">{sym}</div><div style="display:flex;align-items:center;gap:36px"><small style="display:inline;margin:0;white-space:nowrap">{lab}</small><span>{txt}</span></div></div>'
bars=lambda top:(f'<div class="meter" style="top:{top}px;height:400px;padding:36px 44px"><div class="lbl" style="left:44px;top:30px;font-size:26px;color:#3d3a42">SE PERCIBE QUÉ TAN INFORMATIVO (ILUSTRATIVO)</div>'
  f'<div class="lbl" style="left:44px;top:150px;white-space:nowrap">Con pregunta</div><div style="position:absolute;left:350px;top:135px;width:190px;height:70px;background:#e6e1ef;border:4px solid #151316;border-radius:35px"></div>'
  f'<div class="lbl" style="left:44px;top:270px;white-space:nowrap">Que afirma</div><div style="position:absolute;left:350px;top:255px;width:500px;height:70px;background:#B9A3E8;border:4px solid #151316;border-radius:35px"></div></div>')
stan=[
 (serif('Tu título con pregunta',340,92)+big('TE CUESTA',490,100)+serif('<span class="hl">interacción.</span>',610,150)+
   '<div class="card" style="left:86px;right:86px;top:930px;height:230px;padding:0 50px;display:flex;align-items:center;justify-content:space-between;gap:30px"><div style="font:800 52px/1.1 Poppins">¿Cuánto cuesta un lead?</div><div class="sticker" style="position:static;transform:none;background:#B9A3E8;font-size:30px;white-space:nowrap">↓ interacción</div></div>', FD),
 (chip('LOS DATOS')+title('Qué analizó',hl('Stanford.'))+hrow(620,150,'53,030','posts de Reddit')+hrow(790,150,'3,078,791','artículos académicos')+hrow(960,150,'22,743','experimentos A/B de titulares','#B9A3E8')+hrow(1130,150,'400','personas en un estudio de laboratorio'), F),
 (chip('LA CONCLUSIÓN')+title('La pregunta','suena a '+hl('duda.'))+body('Los títulos en forma de pregunta reducen la interacción porque el lector los percibe como menos informativos.')+bars(830), F),
 (chip('QUÉ HACER')+title('Afirma,','no '+hl('preguntes.'))+body('Pruébalo en pocas piezas antes de reescribir todo.')+
   hcmp(820,'bad','✗','ASÍ NO','¿Cuánto cuesta un lead?')+hcmp(1060,'good','✓','ASÍ SÍ','Cuánto cuesta un lead'), F),
 (kick('Antes de publicar')+serif('Guarda este',250,104)+big('CARRUSEL',370,100)+serif('<span class="hl">para tu próximo título.</span>',490,96)+tape('Toca el ícono de guardar',668)+body('Cuando redactes, afirma en lugar de preguntar.',900), foot('Fuente: Stanford GSB')),
]
# ---------- WORKDAY ----------
def flow(top):
    cw=270
    out=''
    labs=[('1','La IA','genera'),('2','Alguien','revisa'),('3','Se','publica')]
    for i,(n,a,b) in enumerate(labs):
        x=86+i*(cw+49)
        bg='background:#B9A3E8;' if i==1 else ''
        out+=f'<div class="stat" style="left:{x}px;top:{top}px;width:{cw}px;height:300px;{bg}padding:26px 28px"><b style="font-size:70px">{n}</b><span style="font:800 40px/1.15 Poppins;margin-top:16px">{a}<br>{b}</span></div>'
        if i<2: out+=f'<div class="sc" style="left:{x+cw+4}px;top:{top+110}px;font-size:48px">→</div>'
    return out
work=[
 (kick('Estudio de Workday · ene 2026')+serif('Casi',270,100)+'<div class="bigy" style="top:372px">40%</div>'+big('DEL TIEMPO QUE TE AHORRA LA IA',730,52,1.15)+serif('<span class="hl">se va en corregirla.</span>',860,84)+
   '<div style="position:absolute;left:86px;top:1060px;width:908px;height:90px;border:4px solid #151316;border-radius:45px;overflow:hidden;background:#fff;display:flex"><div style="width:60%;background:#fff;font:700 32px/82px Source Sans Pro;padding-left:30px">tiempo ahorrado</div><div style="width:40%;background:#B9A3E8;border-left:4px solid #151316;font:800 32px/82px Poppins;text-align:center">CORREGIR</div></div>', FD),
 (chip('EL COSTO OCULTO')+title('Casi 40%','se '+hl('pierde.'))+body('Del tiempo que la IA ahorra, se va corrigiendo, reescribiendo y verificando lo que produce.',590)+
   row2(810,'1','Corrigiendo')+row2(940,'2','Reescribiendo')+row2(1070,'3','Verificando'), foot('Encuesta de Workday, ene 2026')),
 (chip('OJO')+title('Un estudio de','empresas '+hl('grandes.'),92)+body('No es un dato de pymes y no tiene verificación independiente.')+
   stat(86,780,430,300,'3,200','empleados encuestados')+stat(564,780,430,300,'USD 100 M+','ingresos de las empresas','#B9A3E8',fs=52)+'<div class="sticker" style="left:230px;top:1140px;background:#151316;color:#fff;transform:rotate(-2deg)">NO ES UN DATO DE PYMES</div>', F),
 (chip('LA LECCIÓN')+title('Si alguien revisa,','la IA '+hl('ahorra.'),96)+body('Mide cuánto tiempo te toma corregir lo que genera la IA.')+flow(800), F),
 (kick('Antes de usar IA en tu marketing')+serif('¿Y quién la',270,120)+'<div class="t" style="top:430px;font-size:150px"><span class="hl">revisa?</span></div>'+body('Te ayudamos a revisar cómo usas la IA en tu marketing.',640)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: Workday, comunicado del 14 ene 2026')),
]
# ---------- TRIGGER ----------
rays=''.join(f'<div style="position:absolute;left:{755+int(150*__import__("math").cos(a))-6}px;top:{855+int(150*__import__("math").sin(a))-28}px;width:12px;height:56px;background:#151316;border-radius:6px;transform:rotate({int(a*180/3.14159)+90}deg)"></div>' for a in [(-2.9+i*0.52) for i in range(0,9)])
bulb=rays+'<div style="position:absolute;left:665px;top:765px;width:180px;height:180px;border-radius:50%;background:#FFD23F;border:5px solid #151316;box-shadow:8px 9px 0 #151316"></div><div style="position:absolute;left:715px;top:830px;width:80px;height:60px;border:5px solid #151316;border-top:none;border-radius:0 0 40px 40px;transform:scaleY(1)"></div><div style="position:absolute;left:700px;top:940px;width:110px;height:24px;background:#151316;border-radius:8px"></div><div style="position:absolute;left:712px;top:972px;width:86px;height:24px;background:#151316;border-radius:8px"></div>'
tl=''.join(f'<div style="position:absolute;left:{120+i*62}px;top:1000px;width:44px;height:44px;border-radius:50%;background:#cfc9dc;border:4px solid #151316"></div>' for i in range(11))
trig=[
 (kick('Copywriting')+serif('Tu cliente no compra',270,96)+'<div class="serif" style="position:absolute;left:86px;top:375px;font-size:170px;line-height:1;text-decoration:line-through;text-decoration-thickness:14px;text-decoration-color:#151316">beneficios</div>'+big('COMPRA POR LO QUE LE PASÓ',650,60)+serif('<span class="hl">hoy.</span>',760,200)+'<div style="position:absolute;left:0;top:0;transform:translate(40px,90px)">'+bulb+'</div>'+sticker('Empieza aquí',560,1180,-4), FD),
 (chip('TRIGGER EVENT')+title('El momento de','decidir '+hl('actuar.'),96)+body('Un problema puede llevar meses ahí. Lo que lo mueve a actuar es una situación concreta.')+
   '<div style="position:absolute;left:86px;right:86px;top:830px;height:330px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316"></div><div style="position:absolute;left:126px;top:880px;font:800 28px Poppins;letter-spacing:.12em;color:#3d3a42">MESES CON EL PROBLEMA</div>'+tl+'<div style="position:absolute;left:806px;top:975px;width:100px;height:100px;border-radius:50%;background:#FFD23F;border:5px solid #151316;font:800 58px/90px Poppins;text-align:center">!</div><div style="position:absolute;left:806px;top:1090px;width:100px;text-align:center;font:800 28px Poppins;letter-spacing:.08em">HOY</div>', F),
 (chip('EJEMPLO')+title('Así puede empezar','un '+hl('anuncio.'),84)+body('Para un negocio con WhatsApp saturado.')+
   '<div class="card" style="left:86px;right:86px;top:790px;height:440px;padding:56px 56px;background:#B9A3E8"><div style="font:800 28px Poppins;letter-spacing:.16em">TU ANUNCIO DICE</div><div class="serif" style="font-size:92px;line-height:1.05;margin-top:28px">“Hoy no alcancé a contestar a todos.”</div></div>', foot('Ejemplo ilustrativo')),
 (chip('DÓNDE ENCONTRARLO')+title('Tus clientes','ya te lo '+hl('dijeron.'),96)+body('¿Qué pasó para que buscaran ayuda y qué habían probado antes?')+
   row2(790,'★','Reseñas')+row2(930,'“','Comentarios')+row2(1070,'✉','Mensajes'), F),
 (kick('Antes de tu próximo anuncio')+serif('¿Tu anuncio empieza',270,100)+big('CON TU CLIENTE',420,84)+serif('<span class="hl">o contigo?</span>',540,150)+body('Revisemos juntos cómo empieza tu mensaje.',770)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Concepto de copywriting: trigger event')),
]
# ---------- CHATGPT ----------
def step(i,top,h,name,bg=''):
    x=86+i*310
    return f'<div class="day" style="left:{x}px;top:{top}px;width:290px;height:{h}px;{bg}text-align:left;padding:22px 26px"><b style="font-size:90px;margin-top:0">{i+1}</b><small style="font-size:30px;color:#151316;letter-spacing:.04em;margin-top:8px">{name}</small></div>'
chat=[
 (kick('ChatGPT Ads')+serif('3 pasos antes de',270,96)+big('GASTAR UN PESO EN',410,64)+serif('<span class="hl">ChatGPT Ads.</span>',490,120)+
   step(0,900,290,'Define')+step(1,830,360,'Registra')+step(2,760,430,'Compara','background:#B9A3E8;')+sticker('Mide primero',620,640,4), FD),
 (chip('PASO 1')+title('Define la',hl('conversión.'))+body('¿Qué cuenta como resultado en tu negocio? Decídelo antes de lanzar el anuncio.')+
   row2(790,'✓','Un mensaje')+row2(930,'✓','Una llamada')+row2(1070,'✓','Una cita'), F),
 (chip('PASO 2')+title('Registra la',hl('fuente.'))+body('Cada contacto debe entrar con su origen, en tu CRM o en una hoja.')+
   '<div class="meter" style="top:800px;height:430px"><div style="height:80px;background:#e6e1ef;border-bottom:4px solid #151316;font:800 28px/76px Poppins;letter-spacing:.1em;padding-left:36px">CONTACTO <span style="margin-left:230px">ORIGEN</span></div>'+''.join(f'<div style="height:116px;border-bottom:3px solid #cfc9dc;font:700 38px/112px Source Sans Pro;padding-left:36px;{"background:#B9A3E8;" if i==1 else ""}">Contacto {i+1} <span style="position:absolute;left:340px">→ {o}</span></div>' for i,o in enumerate(['ChatGPT Ads','Google','Recomendación']))+'</div>', foot('Ejemplo ilustrativo')),
 (chip('PASO 3')+title('Compara y','prueba '+hl('chico.'))+body('Compara contra tu costo actual por contacto y empieza con un presupuesto de prueba.')+
   mini(86,820,390,300,'HOY','Costo actual por contacto')+'<div class="sym" style="left:500px;top:900px">?</div>'+mini(604,820,390,300,'CHATGPT ADS','Costo por contacto','#B9A3E8'), F),
 (kick('Revisémoslo juntos')+serif('¿Lo revisamos',270,120)+'<div class="t" style="top:430px;font-size:150px"><span class="hl">juntos?</span></div>'+body('Te ayudamos a medir antes de invertir.',640)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: OpenAI')),
]
# ---------- ENLACES ----------
links=''.join(f'<div class="mini2" style="left:{86+i*310}px;top:{900+(i%2)*40}px;width:290px;height:200px;text-align:center;font:800 56px/1 Poppins;padding-top:36px;{"background:#B9A3E8;" if i==1 else ""}box-shadow:8px 9px 0 #151316">↗<small style="margin-top:14px;font-size:28px!important">ENLACE</small></div>' for i in range(3))
enl=[
 (kick('Google · AI Mode')+serif('Google puso más',270,104)+serif('<span class="hl">enlaces</span>',400,150)+big('EN AI MODE',580,80)+body('Más enlaces, sin datos de clics.',700)+links+sticker('Más enlaces',640,830,4), FD),
 (chip('QUÉ CAMBIÓ')+title('Más',hl('enlaces.'))+body('En oct 2026 Google anunció más enlaces en AI Mode y AI Overviews.')+
   mini(86,800,430,260,'GOOGLE','AI Mode ↗')+mini(564,800,430,260,'GOOGLE','AI Overviews ↗','#B9A3E8'), foot('Fuente: Google y Search Engine Journal')),
 (chip('EN SEARCH CONSOLE')+title('Impresiones sí,','clics '+hl('no.'))+body('Las impresiones de IA se ven aparte. Los clics se cuentan en Búsqueda web, sin separarlos.')+
   stat(86,820,430,290,'Aparte','impresiones de IA','#B9A3E8',fs=60)+stat(564,820,430,290,'Mezclados','clics, dentro de Búsqueda web',fs=52), foot('Fuente: Google Search Central')),
 (kick('Mide tu tráfico')+serif('¿Sabes de dónde',270,104)+serif('viene',390,104)+'<div class="t" style="top:520px;font-size:96px"><span class="hl">tu tráfico?</span></div>'+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: Google y Search Engine Journal')),
]
# ---------- CRM ----------
sheet='<div class="card" style="left:86px;top:860px;width:430px;height:320px;overflow:hidden;padding:0"><div style="height:56px;background:#e6e1ef;border-bottom:4px solid #151316"></div>'+''.join(f'<div style="height:2px;background:#cfc9dc;margin-top:{40 if i==0 else 38}px"></div>' for i in range(5))+'<div style="position:absolute;left:96px;top:56px;bottom:0;width:3px;background:#cfc9dc"></div><div style="position:absolute;left:230px;top:56px;bottom:0;width:3px;background:#cfc9dc"></div></div><div class="lbl" style="left:86px;top:1200px">Hoja de cálculo</div>'
crmc='<div class="card" style="left:564px;top:860px;width:430px;height:320px;padding:24px;background:#B9A3E8">'+''.join(f'<div style="position:absolute;left:{24+i*132}px;top:24px;width:118px;height:272px;background:#fff;border:3px solid #151316;border-radius:14px"><div style="margin:10px;height:46px;background:#FFD23F;border:3px solid #151316;border-radius:8px"></div>'+(f'<div style="margin:10px;height:46px;background:#e6e1ef;border:3px solid #151316;border-radius:8px"></div>' if i<2 else '')+'</div>' for i in range(3))+'</div><div class="lbl" style="left:564px;top:1200px">CRM</div>'
crm=[
 (kick('Del blog')+serif('¿CRM o hoja de',270,100)+serif('<span class="hl">cálculo?</span>',390,170)+big('UNA REGLA SIMPLE<br>PARA DECIDIR.',650,64,1.15)+sheet+crmc, FD),
 (chip('LA REGLA')+title('Un CRM organiza','lo que '+hl('ya existe.'),92)+body('No inventa tu proceso: lo ordena. Primero las reglas, luego la herramienta.')+
   row2(830,'1','Define tus reglas')+row2(970,'2','Elige la herramienta'), F),
 (chip('PARA EMPEZAR')+title('Una o dos','personas '+hl('bastan.'),96)+body('Con menos de 20 a 30 leads nuevos al mes y un proceso simple, una hoja de cálculo alcanza.')+
   '<div class="meter" style="top:840px;height:240px;display:flex"><div style="width:55%;background:#B9A3E8;font:800 36px/236px Poppins;text-align:center">HOJA DE CÁLCULO</div><div style="width:45%;background:#fff;border-left:4px solid #151316;font:800 36px/236px Poppins;text-align:center">CRM</div></div><div class="sticker" style="left:340px;top:1120px;transform:rotate(-3deg)">20 a 30 leads nuevos al mes</div>', foot('Regla práctica de nuestro blog')),
 (chip('EL PROBLEMA')+title('Dos personas en','el mismo '+hl('archivo.'),88)+body('Aparecen versiones distintas y datos que se sobreescriben sin querer.')+
   mini(86,850,390,300,'ARCHIVO DE ANA','Cliente: Luis, llamar el lunes','#fff')+'<div class="sym" style="left:500px;top:930px">≠</div>'+mini(604,850,390,300,'ARCHIVO DE BETO','Cliente: Luis, ya compró','#B9A3E8'), F),
 (chip('UN CRM RESUELVE')+title('Tres',hl('cosas.'))+body('Las reglas las defines tú, con o sin CRM.')+
   row2(790,'1','Recordatorios')+row2(930,'2','Registro central')+row2(1070,'3','Reportes sin armar'), F),
 (kick('Antes de comprar un CRM')+serif('¿Ya tienes tus',270,104)+'<div class="t" style="top:420px;font-size:150px"><span class="hl">reglas?</span></div>'+body('Lee el blog completo en balerocreativo.com.',640)+tape('Diagnóstico gratis de 15 minutos',1150), F),
]
ALL={'roas':roas,'stanford':stan,'workday':work,'trigger':trig,'chatgpt':chat,'enlaces':enl,'crm':crm}
if __name__=='__main__':
    for k,v in ALL.items(): print(k,build(k,v))
