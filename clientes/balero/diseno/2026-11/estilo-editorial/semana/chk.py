import sys,os
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--allow-file-access-from-files','--no-sandbox'])
    for nm in sys.argv[1:]:
        pg=b.new_page(viewport={'width':1080,'height':1440}); pg.goto(f'file://{os.getcwd()}/{nm}.html'); pg.wait_for_timeout(500)
        r=pg.evaluate('''()=>{const o=[];document.querySelectorAll('.s').forEach((s,i)=>{const sr=s.getBoundingClientRect();s.querySelectorAll('.t,.serif,.big,.body,.hl,.chip,.kick').forEach(e=>{const r=e.getBoundingClientRect();if(r.right-sr.left>1000||r.bottom-sr.top>1290)o.push((i+1)+':'+e.className+':'+Math.round(r.right-sr.left)+','+Math.round(r.bottom-sr.top)+':'+e.textContent.slice(0,25))})});return o}''')
        print(nm,r)
    b.close()
