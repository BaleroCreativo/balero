from defs2 import *

NODOTS='<style>.dots{display:none}</style>'

def tiempos():
    h='<div style="position:absolute;left:86px;top:770px;width:908px;background:#fff;border:4px solid #151316;border-radius:28px;box-shadow:10px 12px 0 #151316;overflow:hidden">'
    cols=[('LLEGÓ',270),('CONTESTASTE',380),('TARDÓ',258)]
    h+='<div style="display:flex;height:84px;background:#151316">'+''.join(f'<div style="width:{w}px;padding:0 28px;font:800 28px/84px Poppins;color:#F6F4EF;letter-spacing:.06em;white-space:nowrap">{c}</div>' for c,w in cols)+'</div>'
    rows=['9:02','9:40','11:15','12:30','14:05']
    for i,t in enumerate(rows):
        bg='#FFF6CF' if i==2 else '#fff'
        h+=(f'<div style="display:flex;height:86px;border-top:3px solid #cfc9dc;background:{bg}">'
            f'<div style="width:270px;padding:0 28px;font:800 36px/86px Poppins">{t}</div>'
            f'<div style="width:380px;padding:0 28px;font:700 36px/86px {SSf};color:#6B6870">__:__</div>'
            f'<div style="width:258px;padding:0 28px;font:700 36px/86px {SSf};color:#6B6870">___ min</div></div>')
    return h+'</div>'
def img2video():
    box=lambda x,bg,lab,inner:(f'<div style="position:absolute;left:{x}px;top:720px;width:340px;height:180px;background:{bg};border:4px solid #151316;border-radius:26px;box-shadow:9px 10px 0 #151316">'
                               f'<div style="position:absolute;left:24px;top:16px;font:800 26px Poppins;letter-spacing:.12em">{lab}</div>{inner}</div>')
    pic='<div style="position:absolute;left:24px;right:24px;top:62px;bottom:22px;background:#fff;border:3px solid #151316;border-radius:14px"><div style="position:absolute;left:18px;bottom:0;width:90px;height:60px;background:#151316;clip-path:polygon(0 100%,50% 20%,100% 100%)"></div><div style="position:absolute;right:24px;top:14px;width:34px;height:34px;border-radius:50%;background:#FFD23F;border:3px solid #151316"></div></div>'
    play='<div style="position:absolute;left:0;right:0;top:56px;bottom:0;display:flex;align-items:center;justify-content:center"><div style="width:96px;height:96px;border-radius:50%;background:#151316"><div style="margin:26px 0 0 38px;width:0;height:0;border-left:36px solid #FFD23F;border-top:22px solid transparent;border-bottom:22px solid transparent"></div></div></div>'
    return (box(86,'#B9A3E8','IMAGEN',pic)+
            '<div class="sc" style="left:468px;top:765px;font-size:96px">→</div>'+
            box(654,'#FFD23F','VIDEO',play))
semana_b=[
 (NODOTS+chip('TAREA DE LA SEMANA')+title('Anota la hora','de '+hl('cinco chats.'),96)+body3('Cuándo llegó cada mensaje y cuándo contestó alguien de verdad.',600)+tiempos(), foot('Los mensajes automáticos no cuentan')),
 (NODOTS+chip('META ADS')+title('De imagen','a '+hl('video.'),100)+body3('Meta ofrece generar video a partir de tus imágenes con IA.',600)+img2video()+
  row3(930,'1','Que siga reflejando tu marca',108,fs=38)+row3(1050,'2','Que se entienda sin sonido',108,fs=38)+row3(1170,'3','Que la oferta sea la misma',108,fs=38), foot('Revisa si lo tienes en tu cuenta')),
]
ALL3={'sem17b':semana_b}
if __name__=='__main__':
    for k,v in ALL3.items(): print(k,build(k,v))
