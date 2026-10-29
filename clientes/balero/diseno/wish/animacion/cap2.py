import os,sys
from playwright.sync_api import sync_playwright
P=os.path.abspath('../wish-zip/landing-page-agencia-viajes/project')
px=os.environ['HTTPS_PROXY']
def scrollfull(pg,step,wait=700):
    h=pg.evaluate("document.documentElement.scrollHeight"); y=0
    while y<h:
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(wait); y+=step
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(1500); return h
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files','--ignore-certificate-errors','--proxy-server='+px])
    # escritorio 2x: home (primer viewport) y pagina completa
    c=b.new_context(viewport={'width':1440,'height':900},device_scale_factor=2); pg=c.new_page()
    pg.goto('file://'+P+'/_cap_Wish Travel Landing Page.dc.html'); pg.wait_for_timeout(6000)
    pg.screenshot(path='hero2x.png'); h=scrollfull(pg,450); pg.screenshot(path='home-full2x.png',full_page=True); print('home',h)
    pg2=c.new_page(); pg2.goto('file://'+P+'/_cap_Italia.dc.html'); pg2.wait_for_timeout(6000)
    h=scrollfull(pg2,450); pg2.screenshot(path='italia-full2x.png',full_page=True); print('italia',h)
    c.close()
    # movil 2x
    c=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); pg=c.new_page()
    pg.goto('file://'+P+'/_cap_Wish Travel Landing Page.dc.html'); pg.wait_for_timeout(6000)
    pg.screenshot(path='mob-hero.png'); h=scrollfull(pg,420); pg.screenshot(path='mob-full.png',full_page=True); print('mob',h)
    c.close(); b.close()
