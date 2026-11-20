from defs import *
import sys
SSf="'Source Sans Pro',sans-serif"

# ---------- helpers ----------
def body3(t,top,w=880,col='#151316'):
    return f'<div style="position:absolute;left:86px;top:{top}px;width:{w}px;font:700 42px/1.25 {SSf};color:{col}">{t}</div>'
def row3(top,sym,txt,h=124,bg='#fff',fs=42):
    return (f'<div style="position:absolute;left:86px;top:{top}px;width:908px;height:{h}px;background:{bg};border:4px solid #151316;border-radius:26px;box-shadow:9px 10px 0 #151316">'
            f'<div style="position:absolute;left:28px;top:{(h-64)//2-4}px;width:64px;height:64px;border-radius:50%;background:#FFD23F;border:4px solid #151316;font:800 32px/56px Poppins;text-align:center">{sym}</div>'
            f'<div style="position:absolute;left:122px;right:24px;top:0;bottom:0;display:flex;align-items:center;font:700 {fs}px/1.15 {SSf}">{txt}</div></div>')
def card3(x,y,w,h,big_,lab,bg='#fff',fs=100,lfs=36):
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border:4px solid #151316;border-radius:28px;box-shadow:10px 12px 0 #151316;'
            f'display:flex;flex-direction:column;justify-content:center;padding:0 34px"><div style="font:800 {fs}px/1 Poppins">{big_}</div><div style="font:700 {lfs}px/1.2 {SSf};margin-top:16px">{lab}</div></div>')
def dk(n,idx=None):
    dots=''
    if idx is not None:
        dots=f'#s{n} .dots i{{background:#5b585f!important}}#s{n} .dots i:nth-child({idx+1}){{background:#F6F4EF!important}}'
    else:
        dots=f'#s{n} .dots{{display:none}}'
    return (f'<style>#s{n}{{background:#151316}}#s{n}:after{{background-image:radial-gradient(rgba(246,244,239,.09) 1.2px,transparent 1.3px)}}'
            f'#s{n} .t,#s{n} .body,#s{n} .foot,#s{n} .kick,#s{n} .serif,#s{n} .big{{color:#F6F4EF!important}}'
            f'#s{n} .serif span,#s{n} .hl{{color:#151316!important}}#s{n} .logo{{filter:invert(1)}}{dots}</style>')
def wb(x,y,w,text,side='in',time='',bg=None,fs=42,op=1):
    bgc=bg or ('#fff' if side=='in' else '#FFD23F')
    rad='32px 32px 32px 8px' if side=='in' else '32px 32px 8px 32px'
    t=f'<div style="font:700 26px {SSf};opacity:.6;text-align:right;margin-top:8px">{time}</div>' if time else ''
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;padding:26px 34px;background:{bgc};color:#151316;border:4px solid #151316;opacity:{op};'
            f'border-radius:{rad};box-shadow:9px 10px 0 #151316;font:700 {fs}px/1.2 {SSf}">{text}{t}</div>')
def solid(n,col): return f'<style>#s{n}{{background:{col}}}</style>'
def tapedk(n): return f'<style>#s{n} .tape{{background:#FFD23F;color:#151316}}#s{n} .arrow{{background:#F6F4EF}}</style>'

# ============ 1. WHATSAPP CON IA (lun 23) ============
def waia_cards():
    return (card3(86,800,430,360,'24/7','Meta dice que responde a cualquier hora',fs=120,lfs=38)+
            card3(564,800,430,360,'Meta','Business Agent, en WhatsApp Business','#B9A3E8',fs=104,lfs=38))
waia=[
 (dk(1,0)+chip('FUERA DE HORARIO')+big('TU CLIENTE',290,110)+big('ESCRIBE.',410,110)+
  wb(86,640,800,'Hola, ¿tienen disponibilidad para mañana?','in','11:48 p. m.')+
  wb(86,900,300,'¿Hola?','in','11:52 p. m.')+sticker('Nadie contesta',440,950,-4)+
  serif('<span style="background:#FFD23F;padding:0 20px">¿Y si contestara una IA?</span>',1130,84), FD),
 (chip('LO NUEVO')+title('Meta lanzó','agentes de '+hl('IA.'),92)+body3('Responden a clientes en WhatsApp Business a cualquier hora.',590)+
  waia_cards()+body3('Revisa si ya está disponible en tu país.',1215,908,'#3d3a42'), foot('Fuente: Meta')),
 (chip('TÚ MANDAS')+title('Puedes entrar,','ajustarla o '+hl('apagarla.'),80)+body3('Meta indica que el negocio puede intervenir cuando quiera.',600)+
  row3(800,'1','Entrar a la conversación',150)+row3(980,'2','Ajustar al agente',150)+row3(1160,'3','Apagarlo cuando quieras',150), foot('Fuente: Meta')),
 (chip('ANTES DE ACTIVARLA')+title('Define','tres '+hl('reglas.'),100)+body3('Sin ellas, la IA habla por tu negocio sin límites.',600)+
  row3(800,'1','Qué responde sola',150)+row3(980,'2','Cuándo te pasa la conversación',150)+row3(1160,'3','Quién revisa lo que no sabe',150), F),
 (chip('SIN REGLAS')+title('Contesta rápido,','el lead '+hl('no avanza.'),84)+
  cmp(620,'bad','✗','SIN REGLAS','Responde en segundos y el lead se queda igual',300)+cmp(960,'good','✓','CON REGLAS','Responde, califica y te pasa lo importante',300), F),
 (solid(6,'#FFD23F')+big('¿TU WHATSAPP',280,92)+big('ATIENDE',390,120)+serif('<span style="background:#151316;color:#F6F4EF;padding:0 22px">de noche?</span>',520,130)+
  body3('Revisemos qué puede responder y qué no antes de activar nada.',760)+tape('Diagnóstico gratis de 15 minutos',1010)+
  body3('Escríbenos por mensaje directo.',1180), FOOT),
]

# ============ 2. TU CHAT NO ES UN SISTEMA (mar 24) ============
def fade_rows():
    data=[('Ana','¿Me mandas precio?','hace 2 min',1),('Luis','Hola, ¿sigue disponible?','hace 20 min',.8),('Marta','¿Ya se pudo lo del viernes?','hace 1 h',.6),('Pedro','Te escribo para dar seguimiento','ayer',.4),('Rosa','¿Me cotizas 3?','hace 3 días',.22)]
    h='<div style="position:absolute;left:86px;top:665px;width:908px;height:640px;background:#fff;border:4px solid #151316;border-radius:30px;box-shadow:10px 12px 0 #151316;overflow:hidden">'
    for k,(n,t,w,o) in enumerate(data):
        h+=(f'<div style="position:absolute;left:0;right:0;top:{k*128}px;height:128px;border-bottom:3px solid #cfc9dc;opacity:{o}">'
            f'<div style="position:absolute;left:28px;top:28px;width:72px;height:72px;border-radius:50%;background:#B9A3E8;border:3px solid #151316;font:800 32px/64px Poppins;text-align:center">{n[0]}</div>'
            f'<div style="position:absolute;left:128px;top:16px;font:800 34px Poppins">{n}</div>'
            f'<div style="position:absolute;left:128px;top:66px;font:700 36px {SSf}">{t}</div>'
            f'<div style="position:absolute;right:28px;top:22px;font:700 28px {SSf}">{w}</div></div>')
    return h+'</div>'
def reg_table():
    cols=['Nombre','Fecha','Etapa','Próxima acción']
    ws=[160,170,250,328]
    rows=[('Ana','18 nov','Cotizó','Enviar fotos'),('Luis','19 nov','Nuevo','Preguntar zona'),('Marta','20 nov','Seguimiento','Llamar el lunes')]
    h='<div style="position:absolute;left:86px;top:690px;width:908px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316;overflow:hidden">'
    h+='<div style="display:flex;height:100px;background:#151316">'+''.join(f'<div style="width:{w}px;padding:0 20px;font:800 28px/100px Poppins;color:#F6F4EF;white-space:nowrap">{c}</div>' for c,w in zip(cols,ws))+'</div>'
    for i,r in enumerate(rows):
        bg='#FFF6CF' if i==1 else '#fff'
        h+=f'<div style="display:flex;height:150px;border-top:3px solid #cfc9dc;background:{bg}">'+''.join(f'<div style="width:{w}px;padding:0 20px;font:700 34px/150px {SSf};white-space:nowrap">{c}</div>' for c,w in zip(r,ws))+'</div>'
    return h+'</div>'
def stopwatch():
    return ('<div style="position:absolute;left:496px;top:660px;width:88px;height:46px;background:#151316;border-radius:12px"></div>'
            '<div style="position:absolute;left:320px;top:700px;width:440px;height:440px;border-radius:50%;border:8px solid #151316;box-shadow:12px 14px 0 #151316;background:#fff"></div>'
            '<div style="position:absolute;left:344px;top:724px;width:392px;height:392px;border-radius:50%;background:repeating-conic-gradient(from -1deg,#151316 0 2deg,transparent 2deg 30deg)"></div>'
            '<div style="position:absolute;left:366px;top:746px;width:348px;height:348px;border-radius:50%;background:conic-gradient(from 0deg,#FFD23F 0 25%,#fff 0 100%)"></div>'
            '<div style="position:absolute;left:536px;top:810px;width:8px;height:130px;background:#151316;border-radius:4px;transform-origin:4px 130px;transform:rotate(90deg)"></div>'
            '<div style="position:absolute;left:524px;top:924px;width:32px;height:32px;border-radius:50%;background:#151316"></div>'
            '<div style="position:absolute;left:86px;top:1170px;width:908px;height:120px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:9px 10px 0 #151316;font:800 46px/112px Poppins;text-align:center">Tu máximo: ____ minutos</div>')
def tpl(top,tag,txt,bg='#fff'):
    return (f'<div style="position:absolute;left:86px;top:{top}px;width:908px;height:190px;background:{bg};border:4px solid #151316;border-radius:28px;box-shadow:9px 10px 0 #151316">'
            f'<div style="position:absolute;left:30px;top:20px;padding:4px 20px;background:#151316;color:#F6F4EF;border-radius:20px;font:800 28px Poppins;letter-spacing:.08em">{tag}</div>'
            f'<div style="position:absolute;left:30px;right:30px;top:78px;font:700 40px/1.15 {SSf}">{txt}</div></div>')
def pile():
    return (wb(86,690,860,'Hola, ¿me mandas precio?','in',fs=50)+wb(120,860,780,'¿Ya se pudo lo del viernes?','in',op=.75)+
            wb(86,990,820,'Te escribo para dar seguimiento','in',op=.5)+wb(150,1100,700,'¿Sigue disponible?','in',op=.3))
chatsis=[
 (chip('SEGUIMIENTO')+big('TU CHAT DE',270,84)+big('WHATSAPP NO ES',365,84)+big('UN '+hl('sistema.'),460,84)+
  pile()+
  '<div style="position:absolute;left:790px;top:660px;width:190px;height:190px;border-radius:50%;background:#FFD23F;border:5px solid #151316;box-shadow:8px 9px 0 #151316;font:800 66px/180px Poppins;text-align:center;transform:rotate(6deg)">99+</div>'+
  sticker('Se entierran en minutos',560,1235,-3), FD),
 (chip('EL PROBLEMA')+title('Un chat es','bitácora, no '+hl('sistema.'),84)+body3('Los mensajes nuevos entierran a los viejos.',590)+fade_rows()+sticker('¿Quién le contestó?',560,1290,-3), F),
 (chip('PASO 1')+title('Un registro',hl('aparte.'))+body3('Una hoja con cuatro columnas.',590)+reg_table(), foot('Ejemplo ilustrativo')),
 (chip('PASO 2')+title('Tiempo máximo de','primera '+hl('respuesta.'),80)+body3('Defínelo y que todo el equipo lo conozca.',590)+stopwatch(), F),
 (chip('PASO 3')+title('Plantillas por',hl('etapa.'))+body3('Mensajes listos para cada momento.',590)+
  tpl(670,'NUEVO','Hola, gracias por escribir. ¿Qué necesitas?')+tpl(880,'YA COTIZÓ','Te comparto la cotización. ¿La revisamos?','#FFF6CF')+tpl(1090,'SIN RESPUESTA','Retomo tu consulta. ¿Sigues buscando?'), foot('Ejemplos ilustrativos')),
 (dk(6,5)+tapedk(6)+big('EL PROBLEMA NO',280,92)+big('ES EL CHAT.',390,110)+serif('<span style="background:#FFD23F;padding:0 20px">Es que nadie lo convierte</span>',540,66)+serif('<span style="background:#FFD23F;padding:0 20px">en registro.</span>',630,66)+
  tape('Diagnóstico gratis de 15 minutos',960)+body3('Escríbenos por mensaje directo.',1130), FOOT),
]

# ============ 3. PLANTILLA PAUTA 2027 (mié 25) ============
GRID='<style>.s{background-image:linear-gradient(rgba(21,19,22,.055) 2px,transparent 2px),linear-gradient(90deg,rgba(21,19,22,.055) 2px,transparent 2px);background-size:54px 54px}</style>'
def chkrow(top,txt):
    return (f'<div style="position:absolute;left:86px;top:{top}px;width:908px;height:150px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:9px 10px 0 #151316">'
            f'<div style="position:absolute;left:34px;top:38px;width:66px;height:66px;border:5px solid #151316;border-radius:14px;background:#F6F4EF"></div>'
            f'<div style="position:absolute;left:136px;top:0;bottom:0;display:flex;align-items:center;font:700 46px {SSf}">{txt}</div></div>')
def months():
    ms='EFMAMJJASOND'
    h='<div style="position:absolute;left:86px;top:690px;width:908px;height:560px;background:#fff;border:4px solid #151316;border-radius:28px;box-shadow:10px 12px 0 #151316"></div>'
    for i,m in enumerate(ms):
        x=116+i*70
        h+=f'<div style="position:absolute;left:{x}px;top:940px;width:56px;height:240px;background:#B9A3E8;border:4px solid #151316;border-radius:12px 12px 0 0"></div>'
        h+=f'<div style="position:absolute;left:{x}px;top:1196px;width:56px;text-align:center;font:800 30px Poppins">{m}</div>'
    h+='<div style="position:absolute;left:122px;top:724px;font:800 40px/1.1 Poppins;width:800px">Sube las barras de tus meses fuertes.</div>'
    h+=''.join(f'<div style="position:absolute;left:{116+i*70}px;top:870px;width:56px;text-align:center;font:800 54px Poppins;color:#151316">?</div>' for i in (4,5,10))
    return h
pauta27=[
 (GRID+solid(1,'#FFD23F')+chip('PLANTILLA · 5 PASOS')+big('PLANEAR TU',270,92)+big('PAUTA',380,92)+
  '<div style="position:absolute;left:86px;top:560px;width:520px;height:300px;background:#151316;border-radius:34px;box-shadow:12px 14px 0 #B9A3E8;transform:rotate(-3deg)"><div style="position:absolute;left:30px;top:16px;font:800 220px/1.1 Poppins;color:#F6F4EF;letter-spacing:-.04em">2027</div></div>'+
  '<div style="position:absolute;left:690px;top:640px;width:290px;height:290px;background:#fff;border:5px solid #151316;border-radius:34px;box-shadow:10px 12px 0 #151316;transform:rotate(4deg);padding:34px"><div style="font:800 30px Poppins;letter-spacing:.1em">5 PASOS</div>'+''.join(f'<div style="height:30px;border-bottom:4px solid #151316;margin-top:{28 if i==0 else 22}px"></div>' for i in range(5))+'</div>'+
  serif('<span style="background:#151316;color:#F6F4EF;padding:0 22px">Para llenar con tus números.</span>',1030,62), FD),
 (chip('PASO 1')+title('Elige tu',hl('meta.'))+body3('¿Qué quieres lograr con la pauta el próximo año? Marca una.',590)+chkrow(770,'Más mensajes')+chkrow(950,'Más citas')+chkrow(1130,'Más ventas'), F),
 (chip('PASO 2')+title('Saca tu costo','por '+hl('contacto.'),92)+body3('Con lo que invertiste el último trimestre y los contactos que llegaron.',590)+
  card3(86,830,250,340,'$ ___','invertido',fs=62,lfs=34)+'<div class="sc" style="left:352px;top:960px">÷</div>'+card3(420,830,250,340,'___','contactos',fs=62,lfs=34)+'<div class="sc" style="left:686px;top:960px">=</div>'+card3(748,830,246,340,'$ ___','por contacto','#B9A3E8',fs=62,lfs=34), foot('Tú pones tus números')),
 (chip('PASO 3')+title('Calcula tu',hl('presupuesto.'),96)+body3('Multiplica los contactos que quieres por tu costo actual.',590)+
  card3(86,830,250,340,'___','contactos que quieres',fs=62,lfs=32)+'<div class="sc" style="left:352px;top:960px">×</div>'+card3(420,830,250,340,'$ ___','por contacto',fs=62,lfs=34)+'<div class="sc" style="left:686px;top:960px">=</div>'+card3(748,830,246,340,'$ ___','presupuesto','#FFD23F',fs=62,lfs=34)+body3('Si no te alcanza, ajusta la meta.',1230,880,'#3d3a42'), foot('Tú pones tus números')),
 (chip('PASO 4')+title('Reparte por',hl('mes.'))+body3('Pon más donde tu negocio vende más.',590)+months(), foot('Ilustrativo')),
 (chip('PASO 5')+title('Revisa cada',hl('mes.'))+body3('Un chequeo corto el mismo día de cada mes.',590)+
  row3(780,'1','Contactos contra tu meta',150)+row3(960,'2','Costo contra tu cálculo',150)+row3(1140,'3','Ajusta o pausa lo que no funciona',150,fs=40), F),
 (solid(7,'#B9A3E8')+big('GUARDA ESTA',280,92)+big('PLANTILLA',390,120)+serif('<span style="background:#FFD23F;padding:0 20px">para tu 2027.</span>',520,110)+
  body3('Llénala con tus números del último trimestre.',720)+tape('Revisamos tu plan 2027',900)+body3('Diagnóstico gratis de 15 minutos por mensaje directo.',1060), FOOT),
]

# ============ 4. CADENCIA DE TOQUES (dom 29) ============
ACC=['#FFD23F','#B9A3E8','#FFD23F','#E4572E']
def track(cur):
    days=[('0',0),('1',1),('3',2),('7',3)]
    h='<div style="position:absolute;left:156px;top:700px;width:768px;height:10px;background:#151316;border-radius:5px"></div>'
    for lab,i in days:
        x=134+i*256; on=i==cur; sz=84 if on else 64
        h+=(f'<div style="position:absolute;left:{x-(10 if on else 0)}px;top:{705-sz//2}px;width:{sz}px;height:{sz}px;border-radius:50%;'
            f'background:{ACC[cur] if on else "#fff"};border:5px solid #151316;font:800 {40 if on else 30}px/{sz-10}px Poppins;text-align:center;box-shadow:{"6px 7px 0 #151316" if on else "none"}">{lab}</div>')
    h+='<div style="position:absolute;left:86px;top:770px;font:800 30px Poppins;letter-spacing:.08em;color:#3d3a42">DÍAS DESDE EL PRIMER CONTACTO</div>'
    return h
def dayslide(cur,chiptxt,t1,t2,expl,msgtxt,tag):
    return (chip(chiptxt)+title(t1,t2,84)+track(cur)+body3(expl,840)+
            wb(86,990,908,msgtxt,'out',bg=ACC[cur],fs=54)+
            f'<div style="position:absolute;right:96px;top:950px;padding:8px 30px;background:#151316;color:#F6F4EF;border-radius:30px;font:800 28px Poppins;letter-spacing:.1em;transform:rotate(3deg)">{tag}</div>')
cad=[
 (solid(1,'#B9A3E8')+big('CUÁNDO INSISTIR',270,80)+big('Y CUÁNDO',365,92)+serif('<span style="background:#FFD23F;padding:0 20px">dejarlo ir.</span>',480,120)+
  ''.join(f'<div style="position:absolute;left:{86+i*236}px;top:{1020-i*95}px;width:210px;height:{250+i*95}px;background:{"#FFD23F" if i==0 else "#fff"};border:5px solid #151316;border-radius:26px 26px 0 0;box-shadow:9px 0 0 #151316"><div style="font:800 28px Poppins;letter-spacing:.14em;padding:22px 0 0 24px">DÍA</div><div style="font:800 120px/1 Poppins;padding:0 0 0 24px">{d}</div></div>' for i,d in enumerate(['0','1','3','7'])), FD),
 (dayslide(0,'DÍA 0','Primer contacto','con una '+hl('pregunta.'),'Una pregunta de calificación, no un catálogo.','¡Hola! Gracias por escribir. ¿Para qué fecha lo necesitas?','EJEMPLO'), F),
 (dayslide(1,'DÍA 1','Un recordatorio','sin '+hl('presión.'),'Un solo mensaje breve que le facilite contestar.','Hola, ¿pudiste ver mi mensaje de ayer? Aquí sigo para lo que necesites.','EJEMPLO'), F),
 (dayslide(2,'DÍA 3','Aporta valor','con '+hl('otro ángulo.'),'No repitas lo mismo: cuéntale algo que le sirva.','Muchos clientes preguntan primero por tiempos. Te cuento cómo lo manejamos.','EJEMPLO'), F),
 (dayslide(3,'DÍA 7','Cierre','temporal.','Avisa que cierras y deja la puerta abierta.','Cierro tu consulta por ahora. Si lo retomas más adelante, escríbeme.','EJEMPLO')+sticker('Aquí paras',700,1290,4), F),
 (big('INSISTIR NO ES',270,84)+big('DAR SEGUIMIENTO.',380,84)+serif('<span style="background:#FFD23F;padding:0 20px">Una cadencia fija te dice</span>',510,66)+serif('<span style="background:#FFD23F;padding:0 20px">cuándo parar.</span>',600,66)+
  ''.join(f'<div style="position:absolute;left:{86+i*236}px;top:760px;width:210px;height:150px;background:{ACC[i]};border:5px solid #151316;border-radius:26px;box-shadow:8px 9px 0 #151316;font:800 80px/140px Poppins;text-align:center">{d}</div>' for i,d in enumerate(['0','1','3','7']))+
  tape('Diagnóstico gratis de 15 minutos',1010)+body3('Escríbenos por mensaje directo.',1170), FOOT),
]

ALL2={'waia':waia,'chatsis':chatsis,'pauta27':pauta27,'cad':cad}
if __name__=='__main__':
    for k,v in ALL2.items(): print(k,build(k,v))
