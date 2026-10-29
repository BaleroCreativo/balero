import sys
from playwright.sync_api import sync_playwright
P="file:///tmp/claude-0/-home-user-balero/0dfc59f6-e69c-50c8-8e37-f37524f18834/scratchpad/wish-zip/landing-page-agencia-viajes/project/_wish_capture.dc.html"
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox','--allow-file-access-from-files','--ignore-certificate-errors','--proxy-server='+__import__('os').environ['HTTPS_PROXY']])
    pg=b.new_page(viewport={'width':1440,'height':900})
    pg.goto(P); pg.wait_for_timeout(5000)
    h=pg.evaluate("document.documentElement.scrollHeight"); print('h',h)
    y=0
    while y<h:
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(900); y+=450
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(1500)
    pg.screenshot(path='site-full.png',full_page=True)
    b.close()
