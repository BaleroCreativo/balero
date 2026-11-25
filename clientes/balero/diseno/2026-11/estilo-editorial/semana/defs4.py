from defs3 import *

CREAM='#F6F4EF'
def bodyc(t,top,w=880): return body3(t,top,w,CREAM)

# ============ A · CYBER MONDAY (lun 30) ============
def notif_stack():
    return (wb(86,700,820,'WhatsApp · 3 mensajes sin leer','in',fs=40)+
            wb(130,850,820,'Instagram · 2 mensajes directos','in',fs=40,op=.85)+
            wb(86,1000,820,'Facebook · 1 mensaje','in',fs=40,op=.7)+
            '<div style="position:absolute;left:790px;top:660px;width:150px;height:150px;border-radius:50%;background:#FFD23F;border:5px solid #F6F4EF;font:800 76px/140px Poppins;text-align:center;color:#151316;transform:rotate(6deg)">6</div>')
cyber=[
 (dk(1,0)+chip('CYBER MONDAY')+big('EL FIN DE SEMANA',280,88)+big('TRAJO MENSAJES.',380,88)+
  serif('<span style="background:#FFD23F;padding:0 20px">¿Quién los contestó?</span>',520,92)+notif_stack(), FD),
 (chip('PASO 1')+title('Junta todos','tus '+hl('pendientes.'),96)+body3('Revisa cada lugar donde te escriben, no solo uno.',590)+
  row3(780,'1','WhatsApp',150)+row3(960,'2','Instagram, mensajes directos',150)+row3(1140,'3','Facebook, Messenger',150), F),
 (chip('PASO 2')+title('Ordénalos por','cuál compra '+hl('primero.'),78)+body3('Quien pidió precio o fecha va antes que quien solo saludó.',590)+
  row3(780,'1','Pidió precio o fecha',150,bg='#FFF6CF')+row3(960,'2','Preguntó cómo funciona',150)+row3(1140,'3','Solo saludó',150), F),
 (chip('PASO 3')+title('Contesta con','una '+hl('pregunta.'),96)+
  cmp(640,'bad','✗','ASÍ NO','«Gracias por escribir.»',280)+cmp(960,'good','✓','ASÍ SÍ','«¿Para qué fecha lo necesitas?»',280), foot('Ejemplo ilustrativo')),
 (chip('PASO 4')+title('Anota quién','contestó y '+hl('cuándo.'),80)+body3('Una línea por contacto, para no perder a nadie.',590)+reg_table(), foot('Ejemplo ilustrativo')),
 (solid(6,'#B9A3E8')+big('REVISA TUS',280,100)+big('PENDIENTES',390,100)+serif('<span style="background:#FFD23F;padding:0 20px">hoy mismo.</span>',520,120)+
  body3('Y si necesitas ayuda para ordenarlos, escríbenos.',720)+tape('Diagnóstico gratis de 15 minutos',900)+body3('Escríbenos por mensaje directo.',1060), FOOT),
]

# ============ B · WHATSAPP EN DICIEMBRE (mar 1) ============
def calendar():
    days=[None,1,2,3,4,5,6, 7,8,9,10,11,12,13, 14,15,16,17,18,19,20, 21,22,23,24,25,26,27, 28,29,30,31,None,None,None]
    hot={24,25,31}
    h='<div style="position:absolute;left:86px;top:650px;width:908px;background:#fff;border:4px solid #151316;border-radius:28px;box-shadow:10px 12px 0 #151316;overflow:hidden">'
    h+='<div style="height:86px;background:#151316;color:#F6F4EF;font:800 36px/86px Poppins;letter-spacing:.2em;padding-left:34px">DICIEMBRE 2026</div>'
    h+='<div style="display:flex;flex-wrap:wrap;padding:10px 12px 14px 12px">'
    for d in days:
        if d is None:
            h+='<div style="width:124px;height:96px"></div>'
        else:
            bg='background:#FFD23F;' if d in hot else ''
            h+=f'<div style="width:124px;height:96px;{bg}border-radius:14px;font:800 36px/96px Poppins;text-align:center">{d}</div>'
    h+='</div></div>'
    return h
dic=[
 (GRID+solid(1,'#B9A3E8')+chip('PREPARA TU WHATSAPP')+big('DICIEMBRE',280,110)+big('NO ESPERA.',400,100)+calendar()+
  '<div style="position:absolute;left:86px;top:1330px"></div>', FD),
 (GRID+chip('1 · AUSENCIA')+title('Un mensaje','de '+hl('ausencia.'),100)+body3('Si no vas a contestar un día, avisa cuándo vuelves.',590)+
  wb(86,780,908,'Hola, gracias por escribir. Estamos fuera del [día] al [día] y te contestamos el [día]. ¿Me dejas tu nombre y qué necesitas?','out',fs=42)+sticker('Ejemplo',700,1110,-3), F),
 (GRID+chip('2 · HORARIO')+title('Avisa tu',hl('horario.'))+body3('Ponlo en cada lugar donde te encuentran.',590)+
  row3(780,'1','Bio de Instagram',150)+row3(960,'2','Ficha de Google',150)+row3(1140,'3','Descripción de WhatsApp Business',150,fs=38), F),
 (GRID+chip('3 · RESPUESTAS RÁPIDAS')+title('Deja respuestas',hl('guardadas.'))+body3('Para las preguntas que más se repiten.',590)+
  tpl(680,'HORARIO','Atendemos de [hora] a [hora].')+tpl(890,'UBICACIÓN','Estamos en [colonia], [ciudad].','#FFF6CF')+tpl(1100,'PRECIOS','Te paso la cotización con [dato].'), foot('Ejemplos ilustrativos')),
 (GRID+chip('4 · RESPONSABLE')+title('Quién contesta','cada '+hl('día.'),90)+body3('Anota un nombre por día, también en fines de semana.',590)+
  row3(760,'L','Lunes a viernes: ______',116)+row3(890,'S','Sábado: ______',116)+row3(1020,'D','Domingo: ______',116)+row3(1150,'F','Festivos: ______',116), F),
 (dk(6,5)+tapedk(6)+big('PREPARA TU',280,96)+big('WHATSAPP',390,110)+serif('<span style="background:#FFD23F;padding:0 20px">antes del 24.</span>',520,110)+
  bodyc('Y si quieres que lo revisemos juntos, escríbenos.',720)+tape('Diagnóstico gratis de 15 minutos',900)+bodyc('Escríbenos por mensaje directo.',1060), FOOT),
]

# ============ C · 4 FUGAS SILENCIOSAS (mié 2) ============
def drops():
    h=''
    for i in range(4):
        x=130+i*215; y=720+(i%2)*70
        h+=(f'<div style="position:absolute;left:{x}px;top:{y}px;width:120px;height:120px;background:#FFD23F;border:5px solid #151316;border-radius:50% 0 50% 50%;transform:rotate(45deg);box-shadow:6px 7px 0 #151316"></div>'
            f'<div style="position:absolute;left:{x}px;top:{y+22}px;width:120px;text-align:center;font:800 56px Poppins">{i+1}</div>')
    h+='<div style="position:absolute;left:86px;top:1070px;width:908px;height:190px;background:#151316;border-radius:30px 30px 110px 110px;color:#F6F4EF;font:800 44px/190px Poppins;text-align:center;letter-spacing:.08em;box-shadow:10px 12px 0 #B9A3E8">TU NEGOCIO</div>'
    return h
def fuga(n,idx,t1,t2,expl,fix):
    ghost=f'<div style="position:absolute;right:60px;top:520px;font:800 560px/1 Poppins;color:#FFD23F;opacity:.16">{n}</div>'
    card=(f'<div style="position:absolute;left:86px;top:960px;width:908px;height:300px;background:#B9A3E8;border:4px solid #151316;border-radius:30px;box-shadow:10px 12px 0 #F6F4EF;color:#151316">'
          f'<div style="position:absolute;left:36px;top:28px;font:800 28px Poppins;letter-spacing:.14em">CÓMO TAPARLA</div>'
          f'<div style="position:absolute;left:36px;right:36px;top:84px;font:700 42px/1.25 {SSf}">{fix}</div></div>')
    return dk(idx+1,idx)+ghost+chip(f'FUGA {n}')+title(t1,t2,84)+bodyc(expl,600)+card
fugas=[
 (chip('4 FUGAS SILENCIOSAS')+title('Cuánto cuesta','no tener '+hl('estrategia.'),86)+drops(), FD),
 (fuga(1,1,'Anuncios a una','página '+hl('sin preparar.'),'Pagas por que lleguen y se van sin escribirte.','Que la página cargue rápido y tenga un solo botón claro.'), ''),
 (fuga(2,2,'Mensajes','sin '+hl('responder.'),'Cada mensaje sin contestar es alguien que ya escribió.','Define un tiempo máximo de respuesta y una persona responsable.'), ''),
 (fuga(3,3,'Un perfil sin','prueba '+hl('social.'),'Quien te encuentra quiere ver que ya trabajaste con otros.','Muestra trabajos reales, reseñas y casos, con permiso de tus clientes.'), ''),
 (fuga(4,4,'Contenido sin','llamada a la '+hl('acción.'),'Si no dices qué hacer después, la gente solo mira y sigue.','Una sola acción por publicación: escribir, guardar o agendar.'), ''),
 (solid(6,'#FFD23F')+big('TAPA LA',280,100)+big('PRIMERA',390,110)+serif('<span style="background:#151316;color:#F6F4EF;padding:0 22px">esta semana.</span>',520,110)+
  body3('Escoge la que más reconoces y corrígela antes de pensar en las demás.',720)+tape('Diagnóstico gratis de 15 minutos',950)+body3('Escríbenos por mensaje directo.',1110), FOOT),
]
fugas=[(b,FD if i==0 else FOOT) for i,(b,f) in enumerate(fugas)]

# ============ D · 7 ERRORES (dom 6) ============
def sietecircs():
    pos=[(86,640),(300,640),(514,640),(728,640),(193,850),(407,850),(621,850)]
    cols=['#FFD23F','#fff','#FFD23F','#fff','#fff','#FFD23F','#fff']
    return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:180px;height:180px;border-radius:50%;background:{cols[i]};border:5px solid #151316;box-shadow:8px 9px 0 #151316;font:800 100px/170px Poppins;text-align:center">{i+1}</div>' for i,(x,y) in enumerate(pos))
errs=['Tratar a todos los leads igual','Responder lento','Que nadie sea dueño del lead','Depender de un solo canal','Mensajes que solo piden cerrar','Rendirse tras un solo intento','No anotar por qué se pierde un lead']
siete=[
 (solid(1,'#B9A3E8')+chip('SEGUIMIENTO')+big('7 ERRORES',280,110)+serif('<span style="background:#FFD23F;padding:0 20px">de proceso.</span>',410,100)+sietecircs()+
  serif('Ninguno requiere comprar una herramienta.',1090,54), FD),
 (chip('MARCA LOS QUE HACES')+title('¿Cuántos','reconoces?',100)+''.join(row3(600+i*98,str(i+1),e,88,fs=34,bg='#FFF6CF' if i==2 else '#fff') for i,e in enumerate(errs)), F),
 (chip('EL MÁS URGENTE')+title('Que cada lead','tenga '+hl('un nombre.'),84)+body3('Uno, no «el equipo». Si nadie es dueño, lo demás ni se puede medir.',590)+
  row3(800,'1','Ana → responsable: ______',130)+row3(950,'2','Luis → responsable: ______',130)+row3(1100,'3','Marta → responsable: ______',130), foot('Ejemplo ilustrativo')),
 (chip('NO TODO A LA VEZ')+title('Corrige uno','o '+hl('dos.'),100)+body3('Hazlo durante unas semanas, hasta que sea hábito. Después sigue con el siguiente.',590)+
  card3(86,830,400,340,'AHORA','1 o 2 errores',fs=64,lfs=38,bg='#B9A3E8')+'<div class="sc" style="left:496px;top:960px;font-size:64px">→</div>'+card3(594,830,400,340,'DESPUÉS','El siguiente',bg='#FFD23F',fs=58,lfs=38), F),
 (chip('UN SOLO CANAL')+title('Prueba otro','canal.')+body3('Si llevas 2 o 3 intentos sin respuesta por WhatsApp, prueba una vez por correo o con una llamada.',590)+
  row3(800,'1','Intento 1: WhatsApp',130)+row3(950,'2','Intento 2: WhatsApp',130)+row3(1100,'3','Intento 3: correo o llamada',130,bg='#FFF6CF'), F),
 (dk(6,5)+tapedk(6)+big('¿CUÁL VAS',280,96)+big('A CORREGIR',390,96)+serif('<span style="background:#FFD23F;padding:0 20px">primero?</span>',520,130)+
  bodyc('Los siete están explicados en el blog de balerocreativo.com.',720)+tape('Diagnóstico gratis de 15 minutos',920)+bodyc('Escríbenos por mensaje directo.',1080), FOOT),
]

# ============ E · IMAGEN VIERNES 4 ============
def perdidos():
    cols=[('NO CONTESTÓ','#fff'),('PRECIO','#fff'),('ELIGIÓ A OTRO','#fff')]
    h=''
    for i,(lab,bg) in enumerate(cols):
        x=86+i*314
        h+=(f'<div style="position:absolute;left:{x}px;top:780px;width:280px;height:380px;background:{bg};border:4px solid #151316;border-radius:28px;box-shadow:9px 10px 0 #151316;overflow:hidden">'
            f'<div style="height:84px;background:#151316;color:#F6F4EF;font:800 25px/84px Poppins;text-align:center;letter-spacing:.04em">{lab}</div>'
            +''.join(f'<div style="position:absolute;left:{26+(k%4)*58}px;top:{120+(k//4)*72}px;width:44px;height:44px;border:4px solid #151316;border-radius:10px;background:#F6F4EF"></div>' for k in range(12))+'</div>')
    return h
viernes_perdidos=[
 (NODOTS+chip('TAREA DE LA SEMANA')+title('Anota por qué','se pierde cada '+hl('lead.'),84)+body3('Una nota corta por cada lead perdido. En unas semanas el patrón se ve solo.',590)+perdidos()+
  body2('Si lo que más se repite es «no contestó», revisa tu cadencia de reintento.',1190,908), foot('Marca una casilla por cada lead')),
]

ALL4={'cyber':cyber,'dic':dic,'fugas':fugas,'siete':siete,'perdidos':viernes_perdidos}
if __name__=='__main__':
    for k,v in ALL4.items(): print(k,build(k,v))
