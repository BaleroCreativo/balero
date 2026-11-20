from defs import *
import sys
SSf="'Source Sans Pro',sans-serif"

def dk(n):
    return (f'<style>#s{n}{{background:#151316}}#s{n}:after{{background-image:radial-gradient(rgba(246,244,239,.09) 1.2px,transparent 1.3px)}}'
            f'#s{n} .t,#s{n} .body,#s{n} .foot,#s{n} .kick,#s{n} .serif,#s{n} .big{{color:#F6F4EF!important}}'
            f'#s{n} .serif span,#s{n} .hl{{color:#151316!important}}#s{n} .logo{{filter:invert(1)}}#s{n} .dots{{display:none}}</style>')

def wb(x,y,w,text,side='in',time='',bg=None):
    """burbuja de WhatsApp: in = cliente (blanca), out = nosotros (amarilla)"""
    bgc=bg or ('#fff' if side=='in' else '#FFD23F')
    rad='30px 30px 30px 8px' if side=='in' else '30px 30px 8px 30px'
    t=f'<div style="font:700 22px {SSf};opacity:.6;text-align:right;margin-top:6px">{time}</div>' if time else ''
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;padding:24px 30px;background:{bgc};color:#151316;border:4px solid #151316;'
            f'border-radius:{rad};box-shadow:8px 9px 0 #151316;font:700 38px/1.2 {SSf}">{text}{t}</div>')

# ============ 1. WHATSAPP CON IA (lun 23) ============
waia=[
 (dk(1)+chip('FUERA DE HORARIO')+serif('Son las 11:48 p. m.',290,100)+big('TU CLIENTE ESCRIBE.',410,76)+
  wb(86,600,700,'Hola, ¿tienen disponibilidad para mañana?','in','11:48 p. m.')+
  '<div style="position:absolute;left:86px;top:860px;font:800 40px Poppins;color:#F6F4EF;letter-spacing:.04em;opacity:.85">Nadie contesta.</div>'+
  serif('<span style="background:#FFD23F;padding:0 20px">¿Y si contestara una IA?</span>',1010,88)+
  '<div style="position:absolute;left:86px;top:1180px;width:760px;font:700 34px/1.25 '+SSf+';color:#F6F4EF;opacity:.8">Meta ya lanzó agentes de IA para WhatsApp Business.</div>', FD),
 (chip('LO NUEVO')+title('Meta lanzó','agentes de '+hl('IA.'),92)+body2('Responden a clientes en WhatsApp Business a cualquier hora, también cuando tu equipo no está.',590)+
  stat(86,860,430,300,'24/7','atención sin tu equipo',fs=84)+stat(564,860,430,300,'Meta','Business Agent en WhatsApp','#B9A3E8',fs=70)+
  body2('Revisa si ya está disponible en tu país.',1210,908,'#3d3a42'), foot('Fuente: Meta')),
 (chip('TÚ MANDAS')+title('Puedes entrar,','ajustarla o '+hl('apagarla.'),80)+body2('Meta indica que el negocio puede intervenir cuando quiera.',590)+
  row2(780,'1','Entrar a la conversación')+row2(920,'2','Ajustar al agente')+row2(1060,'3','Apagarlo cuando quieras'), foot('Fuente: Meta')),
 (chip('ANTES DE ACTIVARLA')+title('Define','tres '+hl('reglas.'),100)+body2('Sin ellas, la IA habla por tu negocio sin límites.',590)+
  row2(780,'1','Qué responde sola')+row2(920,'2','Cuándo te pasa la conversación')+row2(1060,'3','Quién revisa lo que no sabe'), F),
 (chip('SIN REGLAS')+title('Contesta rápido,','el lead '+hl('no avanza.'),84)+
  cmp(640,'bad','✗','SIN REGLAS','Responde en segundos y el lead se queda igual',250)+cmp(930,'good','✓','CON REGLAS','Responde, califica y te pasa lo importante',250), F),
 ('<style>#s6{background:#B9A3E8}</style>'+serif('¿Tu WhatsApp',270,110)+big('ATIENDE',400,110)+serif('<span style="background:#FFD23F;padding:0 20px">de noche?</span>',520,130)+
  body2('Revisemos qué puede responder y qué no antes de activar nada.',790)+tape('Diagnóstico gratis de 15 minutos',1050)+
  body2('Escríbenos por mensaje directo.',1210), FOOT),
]

# ============ 2. TU CHAT NO ES UN SISTEMA (mar 24) ============
def fade_rows():
    data=[('Ana','¿Me mandas precio?','hace 2 min',1),('Luis','Hola, ¿sigue disponible?','hace 20 min',.8),('Marta','¿Ya se pudo lo del viernes?','hace 1 h',.6),('Pedro','Te escribo para dar seguimiento','ayer',.4),('Rosa','¿Me cotizas 3?','hace 3 días',.22)]
    h='<div style="position:absolute;left:86px;top:640px;width:908px;height:640px;background:#fff;border:4px solid #151316;border-radius:30px;box-shadow:10px 12px 0 #151316;overflow:hidden">'
    for k,(n,t,w,o) in enumerate(data):
        h+=(f'<div style="position:absolute;left:0;right:0;top:{k*128}px;height:128px;border-bottom:3px solid #cfc9dc;opacity:{o}">'
            f'<div style="position:absolute;left:28px;top:28px;width:70px;height:70px;border-radius:50%;background:#B9A3E8;border:3px solid #151316;font:800 30px/62px Poppins;text-align:center">{n[0]}</div>'
            f'<div style="position:absolute;left:124px;top:22px;font:800 30px Poppins">{n}</div>'
            f'<div style="position:absolute;left:124px;top:66px;font:700 32px {SSf}">{t}</div>'
            f'<div style="position:absolute;right:28px;top:30px;font:700 24px {SSf}">{w}</div></div>')
    h+='</div>'
    return h
def reg_table():
    cols=['Nombre','Fecha','Etapa','Próxima acción']
    ws=[190,170,200,348]
    rows=[('Ana','18 nov','Cotizó','Enviar fotos'),('Luis','19 nov','Nuevo','Preguntar zona'),('Marta','20 nov','Seguimiento','Llamar el lunes')]
    h='<div style="position:absolute;left:86px;top:700px;width:908px;background:#fff;border:4px solid #151316;border-radius:26px;box-shadow:10px 12px 0 #151316;overflow:hidden">'
    h+='<div style="display:flex;height:84px;background:#151316">'+''.join(f'<div style="width:{w}px;padding:0 20px;font:800 24px/84px Poppins;color:#F6F4EF;letter-spacing:.04em;white-space:nowrap">{c}</div>' for c,w in zip(cols,ws))+'</div>'
    for i,r in enumerate(rows):
        bg='#FFF6CF' if i==1 else '#fff'
        h+=f'<div style="display:flex;height:112px;border-top:3px solid #cfc9dc;background:{bg}">'+''.join(f'<div style="width:{w}px;padding:0 20px;font:700 31px/112px {SSf};white-space:nowrap">{c}</div>' for c,w in zip(r,ws))+'</div>'
    h+='</div>'
    return h
def timer_ring():
    return ('<div style="position:absolute;left:290px;top:690px;width:500px;height:500px;border-radius:50%;border:6px solid #151316;box-shadow:12px 14px 0 #151316;background:conic-gradient(#FFD23F 0 68%,#fff 0)"></div>'
            '<div style="position:absolute;left:360px;top:760px;width:360px;height:360px;border-radius:50%;border:5px solid #151316;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center">'
            '<div style="font:800 110px/1 Poppins">X min</div><div style="font:800 26px Poppins;letter-spacing:.14em;margin-top:14px">TÚ LO DEFINES</div></div>')
def tpl(top,tag,txt,bg='#fff'):
    return (f'<div style="position:absolute;left:86px;top:{top}px;width:908px;height:190px;background:{bg};border:4px solid #151316;border-radius:28px;box-shadow:9px 10px 0 #151316">'
            f'<div style="position:absolute;left:30px;top:20px;padding:4px 18px;background:#151316;color:#F6F4EF;border-radius:20px;font:800 24px Poppins;letter-spacing:.1em">{tag}</div>'
            f'<div style="position:absolute;left:30px;right:30px;top:76px;font:700 37px/1.2 {SSf}">{txt}</div></div>')
chatsis=[
 (serif('Tu chat de WhatsApp',250,96)+big('NO ES UN SISTEMA',360,80)+serif('<span class="hl">de seguimiento.</span>',470,90)+
  wb(86,720,640,'Hola, ¿me mandas precio?','in').replace('transform','transform')+wb(360,860,640,'¿Sigue disponible?','in')+wb(86,980,700,'Te escribo para dar seguimiento','in')+wb(400,1100,580,'¿Ya se pudo?','in')+
  sticker('Se entierran en minutos',86,1235,-3), FD),
 (chip('EL PROBLEMA')+title('Un chat es','bitácora, no '+hl('sistema.'),84)+body2('Los mensajes nuevos entierran a los viejos.',590)+fade_rows()+sticker('¿Quién le contestó?',560,1250,-3), F),
 (chip('PASO 1')+title('Un registro',hl('aparte.'))+body2('Una hoja con cuatro columnas: quién, cuándo, en qué etapa y qué sigue.',590)+reg_table(), foot('Ejemplo ilustrativo')),
 (chip('PASO 2')+title('Tiempo máximo de','primera '+hl('respuesta.'),80)+body2('Defínelo y que todo el equipo lo conozca.',590)+timer_ring()+sticker('Lo sabe todo el equipo',330,1240,-3), F),
 (chip('PASO 3')+title('Plantillas por',hl('etapa.'))+body2('Mensajes listos para cada momento.',590)+
  tpl(680,'NUEVO','Hola, gracias por escribir. ¿Qué necesitas?')+tpl(890,'YA COTIZÓ','Te comparto la cotización. ¿La revisamos?','#FFF6CF')+tpl(1100,'SIN RESPUESTA','Retomo tu consulta. ¿Sigues buscando?'), foot('Ejemplos ilustrativos')),
 ('<style>#s6{background:#B9A3E8}</style>'+serif('El problema no',280,100)+big('ES EL CHAT.',400,100)+serif('<span style="background:#FFD23F;padding:0 20px">Es que nadie</span>',540,96)+serif('<span style="background:#FFD23F;padding:0 20px">lo convierte en registro.</span>',660,72)+
  tape('Diagnóstico gratis de 15 minutos',1000)+body2('Escríbenos por mensaje directo.',1160), FOOT),
]

# ============ 3. PLANTILLA PAUTA 2027 (mié 25) ============
GRID='<style>.s{background-image:linear-gradient(rgba(21,19,22,.055) 2px,transparent 2px),linear-gradient(90deg,rgba(21,19,22,.055) 2px,transparent 2px);background-size:54px 54px}</style>'
def chkrow(top,txt,on=False):
    return (f'<div style="position:absolute;left:86px;top:{top}px;width:908px;height:120px;background:#fff;border:4px solid #151316;border-radius:24px;box-shadow:8px 9px 0 #151316">'
            f'<div style="position:absolute;left:30px;top:30px;width:52px;height:52px;border:4px solid #151316;border-radius:12px;background:{"#FFD23F" if on else "#F6F4EF"};font:800 34px/44px Poppins;text-align:center">{"✓" if on else ""}</div>'
            f'<div style="position:absolute;left:118px;top:0;bottom:0;display:flex;align-items:center;font:700 40px {SSf}">{txt}</div></div>')
def months():
    ms='EFMAMJJASOND'; hs=[60,50,70,80,70,60,55,65,90,110,160,130]
    h='<div style="position:absolute;left:86px;top:690px;width:908px;height:480px;background:#fff;border:4px solid #151316;border-radius:28px;box-shadow:10px 12px 0 #151316"></div>'
    for i,(m,v) in enumerate(zip(ms,hs)):
        x=122+i*73; hh=v*2.2
        col='#FFD23F' if i in (10,11) else '#B9A3E8'
        h+=f'<div style="position:absolute;left:{x}px;bottom:{1440-1070-0}px;"></div>'
        h+=f'<div style="position:absolute;left:{x}px;top:{1090-hh}px;width:56px;height:{hh}px;background:{col};border:4px solid #151316;border-radius:12px 12px 0 0"></div>'
        h+=f'<div style="position:absolute;left:{x}px;top:1100px;width:56px;text-align:center;font:800 26px Poppins">{m}</div>'
    h+='<div class="lbl" style="left:122px;top:716px;font-size:24px;color:#3d3a42">TU CALENDARIO MANDA (ILUSTRATIVO)</div>'
    return h
pauta27=[
 (GRID+'<style>#s1{background-color:#FFD23F}</style>'+serif('Plantilla para',260,96)+big('PLANEAR TU PAUTA',370,72)+
  '<div style="position:absolute;left:86px;top:560px;width:520px;height:300px;background:#151316;border-radius:34px;box-shadow:12px 14px 0 #B9A3E8;transform:rotate(-3deg)"><div style="position:absolute;left:30px;top:16px;font:800 220px/1.1 Poppins;color:#F6F4EF;letter-spacing:-.04em">2027</div></div>'+
  '<div style="position:absolute;left:690px;top:640px;width:290px;height:290px;background:#fff;border:5px solid #151316;border-radius:34px;box-shadow:10px 12px 0 #151316;transform:rotate(4deg);padding:34px"><div style="font:800 28px Poppins;letter-spacing:.1em">5 PASOS</div>'+''.join(f'<div style="height:30px;border-bottom:4px solid #151316;margin-top:{28 if i==0 else 22}px"></div>' for i in range(5))+'</div>'+
  serif('<span style="background:#151316;color:#F6F4EF;padding:0 22px">Sin cifras inventadas.</span>',1010,64)+body2('Pon tus números y listo.',1130), FD),
 (chip('PASO 1')+title('Elige tu',hl('meta.'))+body2('¿Qué quieres lograr con la pauta el próximo año? Marca una.',590)+chkrow(760,'Más mensajes',False)+chkrow(910,'Más citas',True)+chkrow(1060,'Más ventas',False), F),
 (chip('PASO 2')+title('Saca tu costo','por '+hl('contacto.'),92)+body2('Con lo que invertiste el último trimestre y los contactos que llegaron.',590)+
  stat(86,830,250,300,'$ ___','invertido',fs=58)+'<div class="sc" style="left:352px;top:950px">÷</div>'+stat(420,830,250,300,'___','contactos',fs=58)+'<div class="sc" style="left:686px;top:950px">=</div>'+stat(748,830,246,300,'$ ___','por contacto','#B9A3E8',fs=58), foot('Tú pones tus números')),
 (chip('PASO 3')+title('Calcula tu',hl('presupuesto.'),96)+body2('Multiplica los contactos que quieres por tu costo actual.',590)+
  stat(86,830,250,300,'___','contactos que quieres',fs=58)+'<div class="sc" style="left:352px;top:950px">×</div>'+stat(420,830,250,300,'$ ___','por contacto',fs=58)+'<div class="sc" style="left:686px;top:950px">=</div>'+stat(748,830,246,300,'$ ___','presupuesto','#FFD23F',fs=58)+serif('Si no te alcanza, ajusta la meta.',1240,48), foot('Tú pones tus números')),
 (chip('PASO 4')+title('Reparte por',hl('mes.'))+body2('Pon más donde tu negocio vende más.',590)+months(), foot('Ilustrativo')),
 (chip('PASO 5')+title('Revisa cada',hl('mes.'))+body2('Un chequeo corto el mismo día de cada mes.',590)+
  row2(760,'1','Contactos contra tu meta')+row2(900,'2','Costo contra tu cálculo')+row2(1040,'3','Ajusta o pausa lo que no funciona'), F),
 ('<style>#s7{background-color:#B9A3E8}</style>'+serif('Guarda esta',270,110)+big('PLANTILLA',400,104)+serif('<span style="background:#FFD23F;padding:0 20px">para tu 2027.</span>',520,110)+
  body2('Llénala con tus números del último trimestre.',720)+tape('Revisamos tu plan 2027',900)+body2('Diagnóstico gratis de 15 minutos por mensaje directo.',1060), FOOT),
]

# ============ 4. CADENCIA DE TOQUES (dom 29) ============
def track(cur):
    days=[('0',0),('1',1),('3',2),('7',3)]
    h='<div style="position:absolute;left:156px;top:690px;width:768px;height:10px;background:#151316;border-radius:5px"></div>'
    for lab,i in days:
        x=140+i*256
        on=i==cur
        h+=(f'<div style="position:absolute;left:{x}px;top:{665-(10 if on else 0)}px;width:{60+(20 if on else 0)}px;height:{60+(20 if on else 0)}px;border-radius:50%;'
            f'background:{"#FFD23F" if on else "#fff"};border:5px solid #151316;font:800 {32 if on else 28}px/{50+(20 if on else 0)}px Poppins;text-align:center;box-shadow:{"6px 7px 0 #151316" if on else "none"}">{lab}</div>')
    h+='<div class="lbl" style="left:86px;top:760px;font-size:24px;color:#3d3a42">DÍAS DESDE EL PRIMER CONTACTO</div>'
    return h
def dayslide(cur,chiptxt,t1,t2,expl,msgtxt,tag=''):
    return (chip(chiptxt)+title(t1,t2,84)+track(cur)+body2(expl,830)+wb(86,990,800,msgtxt,'out')+(tag if tag else ''))
cad=[
 ('<style>#s1{background:#B9A3E8}</style>'+serif('Cuándo insistir',250,100)+big('Y CUÁNDO',365,92)+serif('<span style="background:#FFD23F;padding:0 20px">dejarlo ir.</span>',470,120)+
  ''.join(f'<div style="position:absolute;left:{86+i*236}px;top:{1020-i*95}px;width:210px;height:{250+i*95}px;background:{"#FFD23F" if i==0 else "#fff"};border:5px solid #151316;border-radius:26px 26px 0 0;box-shadow:9px 0 0 #151316"><div style="font:800 24px Poppins;letter-spacing:.14em;padding:22px 0 0 24px">DÍA</div><div style="font:800 110px/1 Poppins;padding:0 0 0 24px">{d}</div></div>' for i,d in enumerate(['0','1','3','7'])), FD),
 (dayslide(0,'DÍA 0','Primer contacto','con una '+hl('pregunta.'),'Una pregunta de calificación, no un catálogo.','¡Hola! Gracias por escribir. ¿Para qué fecha lo necesitas?')+sticker('Ejemplo',700,1240,-3), F),
 (dayslide(1,'DÍA 1','Un recordatorio','sin '+hl('presión.'),'Un solo mensaje breve que le facilite contestar.','Hola, ¿pudiste ver mi mensaje de ayer? Aquí sigo para lo que necesites.')+sticker('Ejemplo',700,1260,-3), F),
 (dayslide(2,'DÍA 3','Aporta valor','con '+hl('otro ángulo.'),'No repitas lo mismo: cuéntale algo que le sirva.','Muchos clientes preguntan primero por tiempos. Te cuento cómo lo manejamos.')+sticker('Ejemplo',700,1260,-3), F),
 (dayslide(3,'DÍA 7','Cierre','temporal.','Avisa que cierras la consulta y deja la puerta abierta.','Cierro tu consulta por ahora. Si lo retomas más adelante, escríbeme.')+sticker('Aquí paras',730,1290,4), F),
 ('<style>#s6{background:#B9A3E8}</style>'+serif('Insistir no es',270,104)+big('DAR SEGUIMIENTO.',390,84)+serif('<span style="background:#FFD23F;padding:0 20px">Una cadencia fija</span>',510,84)+serif('<span style="background:#FFD23F;padding:0 20px">te dice cuándo parar.</span>',620,72)+
  tape('Diagnóstico gratis de 15 minutos',960)+body2('Escríbenos por mensaje directo.',1120), FOOT),
]

ALL2={'waia':waia,'chatsis':chatsis,'pauta27':pauta27,'cad':cad}
if __name__=='__main__':
    for k,v in ALL2.items(): print(k,build(k,v))
