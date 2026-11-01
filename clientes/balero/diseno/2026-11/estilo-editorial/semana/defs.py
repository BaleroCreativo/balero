from gen import *
F=foot()
DESL='<div style="position:absolute;right:86px;bottom:70px;font:800 30px Poppins;letter-spacing:.14em">DESLIZA →</div>'
FD=FOOT+DESL
def tilecards(items,top,w=190,gap=25,start=86):
    pass
# ---------- ROAS ----------
roas=[
 (kick('Publicidad digital')+serif('Un ROAS de',250,100)+'<div class="bigy" style="top:350px">8</div>'+big('PUEDE GANAR MENOS',700,64)+serif('<span class="hl">que uno de 5.</span>',800,110)+tape('Calcula tu número mínimo',1110), FD),
 (chip('LA FÓRMULA')+title('Ventas entre',hl('inversión.'),100)+body('Eso es el ROAS: lo que vendes dividido entre lo que inviertes en anuncios.')+
   stat(86,820,250,250,'$2,000','ventas',fs=56)+'<div class="sc" style="left:350px;top:900px">÷</div>'+stat(420,820,250,250,'$400','inversión',fs=56)+'<div class="sc" style="left:684px;top:900px">=</div>'+stat(748,820,246,250,'5','ROAS','#B9A3E8'), foot('Ejemplo ilustrativo')),
 (chip('EL PUNTO CIEGO')+title('El panel no ve','tus '+hl('costos.'))+body('No sabe cuánto te cuesta vender ni tus gastos fijos. Un ROAS de 3 puede ser bueno para uno y pérdida para otro.')+
   cmp(840,'good','✓','NEGOCIO A · ROAS 3','Le deja ganancia',200)+cmp(1070,'bad','✗','NEGOCIO B · ROAS 3','Pierde dinero',200), F),
 (chip('TU NÚMERO')+title('Tu ROAS mínimo:','dejar de '+hl('perder.'),100)+body('Es el ROAS donde dejas de perder. Por encima ganas, por debajo pierdes, aunque el panel se vea bien.')+
   '<div style="position:absolute;left:86px;top:860px;width:908px;height:140px;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316;overflow:hidden;background:#fff;display:flex"><div style="width:50%;background:#e6e1ef;font:800 34px/140px Poppins;text-align:center;letter-spacing:.1em">PIERDES</div><div style="width:50%;background:#B9A3E8;font:800 34px/140px Poppins;text-align:center;letter-spacing:.1em">GANAS</div></div>'+
   '<div style="position:absolute;left:515px;top:820px;width:50px;height:220px;background:#151316;border-radius:25px"></div>'+sticker('Tu ROAS mínimo',356,1090,-3), F),
 (chip('ESCALA')+title('Más ROAS no siempre','es más '+hl('ganancia.'),84)+body('Un ROAS de 8 con $500 puede dejar menos que uno de 5 con $10,000.')+
   stat(86,960,420,230,'ROAS 8','inviertes $500')+stat(574,820,420,370,'ROAS 5','inviertes $10,000','#B9A3E8'), foot('Ejemplo ilustrativo')),
 (kick('Antes de invertir más')+serif('¿Sabes cuál es tu',270,104)+'<div class="t" style="top:420px;font-size:130px"><span class="hl">ROAS mínimo?</span></div>'.replace('130px','104px')+body('Calcúlalo antes de subir tu presupuesto.',620)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Los números son ejemplos ilustrativos')),
]
# ---------- STANFORD ----------
stan=[
 (kick('Estudio de Stanford')+serif('Tu título con pregunta',270,92)+big('TE CUESTA',420,100)+serif('<span class="hl">interacción.</span>',540,150)+
   '<div class="card" style="left:86px;right:86px;top:880px;height:300px;padding:40px 46px"><div style="font:800 24px Poppins;letter-spacing:.16em;color:#6B6870">TU PUBLICACIÓN</div><div style="font:800 52px/1.1 Poppins;margin-top:18px">¿Cuánto cuesta un lead?</div><div class="sticker" style="left:46px;top:196px;transform:none;background:#B9A3E8;font-size:26px">↓ interacción</div></div>', FD),
 (chip('QUÉ ANALIZÓ')+title('Qué analizó',hl('Stanford.'))+stat(86,640,430,260,'53,030','posts de Reddit')+stat(564,640,430,260,'3,078,791','artículos académicos')+stat(86,950,430,260,'22,743','experimentos A/B de titulares','#B9A3E8')+stat(564,950,430,260,'400','personas en un estudio de laboratorio'), F),
 (chip('LA CONCLUSIÓN')+title('La pregunta','suena a '+hl('duda.'))+body('Los títulos en forma de pregunta reducen la interacción porque el lector los percibe como menos informativos.')+
   cmp(860,'bad','✗','TÍTULO CON PREGUNTA','Se percibe menos informativo',190)+cmp(1080,'good','✓','TÍTULO QUE AFIRMA','Se percibe más informativo',190), F),
 (chip('QUÉ HACER')+title('Afirma,','no '+hl('preguntes.'))+body('Pruébalo en pocas piezas antes de reescribir todo.')+
   cmp(800,'bad','✗','ASÍ NO','¿Cuánto cuesta un lead?',210)+cmp(1050,'good','✓','ASÍ SÍ','Cuánto cuesta un lead',210), F),
 (kick('Revisemos juntos')+serif('¿Revisamos tus',270,104)+big('TÍTULOS Y',420,100)+serif('<span class="hl">ganchos?</span>',540,150)+body('Te decimos qué ajustar en 15 minutos, sin costo.',760)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: Stanford GSB')),
]
# ---------- WORKDAY ----------
work=[
 (kick('Estudio de Workday · ene 2026')+serif('Casi',250,100)+'<div class="bigy" style="top:340px">40%</div>'+big('DEL TIEMPO QUE TE AHORRA LA IA',700,52,1.15)+serif('<span class="hl">se va en corregirla.</span>',840,84)+
   '<div style="position:absolute;left:86px;top:1080px;width:908px;height:70px;border:4px solid #151316;border-radius:35px;overflow:hidden;background:#fff;display:flex"><div style="width:60%;background:#fff;font:700 26px/62px Source Sans Pro;padding-left:24px">tiempo ahorrado</div><div style="width:40%;background:#B9A3E8;border-left:4px solid #151316;font:800 26px/62px Poppins;text-align:center">CORREGIR</div></div>', FD),
 (chip('EL COSTO OCULTO')+title('Casi 40%','se '+hl('pierde.'))+body('Del tiempo que la IA ahorra, se va corrigiendo, reescribiendo y verificando lo que produce.',590)+
   row2(820,'1','Corrigiendo')+row2(950,'2','Reescribiendo')+row2(1080,'3','Verificando'), foot('Encuesta de Workday, ene 2026')),
 (chip('OJO')+title('Un estudio de','empresas '+hl('grandes.'),92)+body('No es un dato de pymes y no tiene verificación independiente.')+
   stat(86,800,430,260,'3,200','empleados encuestados')+stat(564,800,430,260,'USD 100 M+','ingresos de las empresas','#B9A3E8',fs=52)+'<div class="sticker" style="left:230px;top:1120px;background:#151316;color:#fff;transform:rotate(-2deg)">NO ES UN DATO DE PYMES</div>', F),
 (chip('LA LECCIÓN')+title('La IA ahorra tiempo','si alguien '+hl('revisa.'),92)+body('Mide cuánto tiempo te toma corregir lo que genera la IA.')+
   cmp(800,'bad','✗','ASÍ NO','Publicar lo que sale, sin revisar',210)+cmp(1050,'good','✓','ASÍ SÍ','Alguien revisa antes de publicar',210), F),
 (kick('Antes de usar IA en tu marketing')+serif('¿Y quién la',270,120)+'<div class="t" style="top:430px;font-size:150px"><span class="hl">revisa?</span></div>'+body('Te ayudamos a revisar cómo usas la IA en tu marketing.',620)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: Workday, comunicado del 14 ene 2026')),
]
# ---------- TRIGGER ----------
bulb='<div style="position:absolute;left:640px;top:760px;width:210px;height:210px;border-radius:50%;background:#FFD23F;border:5px solid #151316;box-shadow:10px 12px 0 #151316"></div><div style="position:absolute;left:688px;top:965px;width:114px;height:56px;background:#151316;border-radius:0 0 18px 18px"></div>'
trig=[
 (kick('Copywriting')+serif('Tu cliente no compra',250,96)+'<div class="serif" style="position:absolute;left:86px;top:350px;font-size:170px;line-height:1;text-decoration:line-through;text-decoration-thickness:14px;text-decoration-color:#B9A3E8">beneficios</div>'+big('COMPRA POR LO QUE LE PASÓ',640,60)+serif('<span class="hl">hoy.</span>',740,200)+bulb+sticker('Empieza aquí',560,1100), FD),
 (chip('TRIGGER EVENT')+title('El momento de','decidir '+hl('actuar.'),96)+body('Un problema puede llevar meses ahí. Lo que lo mueve a actuar es una situación concreta.')+
   '<div style="position:absolute;left:86px;right:86px;top:860px;height:250px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316"></div>'+''.join(f'<div style="position:absolute;left:{126+i*58}px;top:960px;width:30px;height:30px;border-radius:50%;background:#cfc9dc"></div>' for i in range(10))+'<div style="position:absolute;left:716px;top:925px;width:100px;height:100px;border-radius:50%;background:#FFD23F;border:5px solid #151316;font:800 54px/90px Poppins;text-align:center">!</div>'+'<div style="position:absolute;left:126px;top:885px;font:800 24px Poppins;letter-spacing:.14em;color:#6B6870">MESES CON EL PROBLEMA</div><div style="position:absolute;left:640px;top:1040px;font:800 24px Poppins;letter-spacing:.14em">HOY</div>', F),
 (chip('EJEMPLO')+title('Así puede empezar','un '+hl('anuncio.'),84)+body('Para un negocio con WhatsApp saturado.')+
   '<div class="card" style="left:86px;right:86px;top:800px;height:380px;padding:50px 56px;background:#B9A3E8"><div style="font:800 24px Poppins;letter-spacing:.16em">TU ANUNCIO DICE</div><div class="serif" style="font-size:84px;line-height:1.05;margin-top:24px">“Hoy no alcancé a contestar a todos.”</div></div>', foot('Ejemplo ilustrativo')),
 (chip('DÓNDE ENCONTRARLO')+title('Tus clientes','ya te lo '+hl('dijeron.'),96)+body('¿Qué pasó para que buscaran ayuda y qué habían probado antes?')+
   row2(800,'★','Reseñas')+row2(930,'“','Comentarios')+row2(1060,'✉','Mensajes'), F),
 (kick('Antes de tu próximo anuncio')+serif('¿Tu anuncio empieza',270,100)+big('CON TU CLIENTE',420,84)+serif('<span class="hl">o contigo?</span>',540,150)+body('Revisemos juntos cómo empieza tu mensaje.',780)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Concepto de copywriting: trigger event')),
]
# ---------- CHATGPT ----------
stairs=''.join(f'<div class="day" style="left:{86+i*215}px;top:{1180-i*0-(60+i*60)}px;width:190px;height:{60+i*60+130}px;{"background:#B9A3E8;" if i==2 else ""}"><b>{i+1}</b><small>paso</small></div>' for i in range(3))
chat=[
 (kick('ChatGPT Ads')+serif('3 pasos antes de',250,96)+big('GASTAR UN PESO EN',390,64)+serif('<span class="hl">ChatGPT Ads.</span>',470,120)+sticker('Mide primero',640,660,4)+
   ''.join(f'<div class="day" style="left:{86+i*230}px;top:{1000-i*70}px;width:210px;height:{230+i*70}px;{"background:#B9A3E8;" if i==2 else ""}"><b>{i+1}</b><small>paso</small></div>' for i in range(3)), FD),
 (chip('PASO 1')+title('Define la',hl('conversión.'))+body('¿Qué cuenta como resultado en tu negocio? Decídelo antes de lanzar el anuncio.')+
   row2(780,'✓','Un mensaje')+row2(910,'✓','Una llamada')+row2(1040,'✓','Una cita'), F),
 (chip('PASO 2')+title('Registra la',hl('fuente.'))+body('Cada contacto debe entrar con su origen, en tu CRM o en una hoja.')+
   cmp(800,'bad','✗','ASÍ NO','Contactos sin saber de dónde vienen',210)+cmp(1050,'good','✓','ASÍ SÍ','Cada contacto con su canal de origen',210), F),
 (chip('PASO 3')+title('Compara y','prueba '+hl('chico.'))+body('Compara contra tu costo actual por contacto y empieza con un presupuesto de prueba.')+
   mini(86,840,390,250,'HOY','Costo actual por contacto')+'<div class="sym" style="left:500px;top:900px">?</div>'+mini(604,840,390,250,'CHATGPT ADS','Costo por contacto','#B9A3E8'), F),
 (kick('Revisémoslo juntos')+serif('¿Lo revisamos',270,120)+'<div class="t" style="top:430px;font-size:150px"><span class="hl">juntos?</span></div>'+body('Te ayudamos a medir antes de invertir.',620)+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: OpenAI')),
]
# ---------- ENLACES ----------
links=''.join(f'<div class="mini2" style="left:{86+i*310}px;top:{960+(i%2)*40}px;width:290px;height:170px;text-align:center;font:800 44px/1 Poppins;padding-top:34px;{"background:#B9A3E8;" if i==1 else ""}box-shadow:8px 9px 0 #151316">↗<small style="margin-top:12px;font-size:22px">ENLACE</small></div>' for i in range(3))
enl=[
 (kick('Google · AI Mode')+serif('Google puso más',250,104)+serif('<span class="hl">enlaces</span>',380,150)+big('EN AI MODE',560,80)+body('Más enlaces, sin datos de clics.',690)+links+sticker('Más enlaces',640,850,4), FD),
 (chip('QUÉ CAMBIÓ')+title('Más',hl('enlaces.'))+body('En oct 2026 Google anunció más enlaces en AI Mode y AI Overviews.')+
   mini(86,800,430,300,'GOOGLE','AI Mode ↗')+mini(564,800,430,300,'GOOGLE','AI Overviews ↗','#B9A3E8'), foot('Fuente: Google y Search Engine Journal')),
 (chip('EN SEARCH CONSOLE')+title('Impresiones sí,','clics '+hl('no.'))+body('Las impresiones de IA se ven aparte. Los clics se cuentan en Búsqueda web, sin separarlos.')+
   cmp(860,'good','✓','IMPRESIONES DE IA','Se ven aparte',190)+cmp(1080,'bad','✗','CLICS','Dentro de Búsqueda web',190), foot('Fuente: Google Search Central')),
 (kick('Mide tu tráfico')+serif('¿Sabes de dónde',270,104)+serif('viene',380,104)+'<div class="t" style="top:500px;font-size:96px"><span class="hl">el tráfico de tu web?</span></div>'.replace('<span class="hl">el tráfico de tu web?</span>','<span class="hl">tu tráfico?</span>')+tape('Diagnóstico gratis de 15 minutos',1150), foot('Fuente: Google y Search Engine Journal')),
]
# ---------- CRM ----------
sheet='<div class="card" style="left:86px;top:900px;width:430px;height:300px;overflow:hidden;padding:0"><div style="height:56px;background:#e6e1ef;border-bottom:4px solid #151316"></div>'+''.join(f'<div style="height:2px;background:#cfc9dc;margin-top:{40 if i==0 else 38}px"></div>' for i in range(5))+'<div style="position:absolute;left:96px;top:56px;bottom:0;width:3px;background:#cfc9dc"></div><div style="position:absolute;left:230px;top:56px;bottom:0;width:3px;background:#cfc9dc"></div></div>'
crmc='<div class="card" style="left:564px;top:900px;width:430px;height:300px;padding:24px;background:#B9A3E8">'+''.join(f'<div style="position:absolute;left:{24+i*132}px;top:24px;width:118px;height:252px;background:#fff;border:3px solid #151316;border-radius:14px"><div style="margin:10px;height:46px;background:#FFD23F;border:3px solid #151316;border-radius:8px"></div>'+(f'<div style="margin:10px;height:46px;background:#e6e1ef;border:3px solid #151316;border-radius:8px"></div>' if i<2 else '')+'</div>' for i in range(3))+'</div>'
crm=[
 (kick('Del blog')+serif('¿CRM o hoja de',270,100)+serif('<span class="hl">cálculo?</span>',390,170)+big('CUÁNDO UNA PYME<br>SÍ NECESITA UN CRM',640,56,1.15)+sheet+crmc+'<div class="sc" style="left:520px;top:1010px;font-size:56px;display:none">vs</div>', FD),
 (chip('LA REGLA')+title('Un CRM organiza','lo que '+hl('ya existe.'),92)+body('No inventa tu proceso: lo ordena. Primero las reglas, luego la herramienta.')+
   row2(840,'1','Define tus reglas')+row2(980,'2','Elige la herramienta'), F),
 (chip('PARA EMPEZAR')+title('Una o dos','personas '+hl('bastan.'),96)+body('Con menos de 20 a 30 leads nuevos al mes y un proceso simple, una hoja de cálculo alcanza.')+
   cmp(880,'good','✓','HOJA DE CÁLCULO','Alcanza si son pocos leads',190)+cmp(1100,'bad','✗','CRM','Todavía no hace falta',190), foot('Regla práctica de nuestro blog')),
 (chip('EL PROBLEMA')+title('Dos personas en','el mismo '+hl('archivo.'),88)+body('Aparecen versiones distintas y datos que se sobreescriben sin querer.')+
   mini(86,860,390,260,'ARCHIVO DE ANA','Cliente: Luis, llamar el lunes','#fff')+'<div class="sym" style="left:500px;top:930px">≠</div>'+mini(604,860,390,260,'ARCHIVO DE BETO','Cliente: Luis, ya compró','#B9A3E8'), F),
 (chip('UN CRM RESUELVE')+title('Tres',hl('cosas.'))+body('Las reglas las defines tú, con o sin CRM.')+
   row2(800,'1','Recordatorios')+row2(930,'2','Registro central')+row2(1060,'3','Reportes sin armar'), F),
 (kick('Antes de comprar un CRM')+serif('¿Ya tienes tus',270,104)+'<div class="t" style="top:420px;font-size:150px"><span class="hl">reglas?</span></div>'+body('Lee el blog completo en balerocreativo.com.',620)+tape('Diagnóstico gratis de 15 minutos',1150), F),
]
ALL={'roas':roas,'stanford':stan,'workday':work,'trigger':trig,'chatgpt':chat,'enlaces':enl,'crm':crm}
if __name__=='__main__':
    for k,v in ALL.items(): print(k,build(k,v))
