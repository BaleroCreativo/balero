import sys,os
from playwright.sync_api import sync_playwright
names=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--allow-file-access-from-files','--no-sandbox'])
    for nm in names:
        pg=b.new_page(viewport={'width':1080,'height':1440}); pg.goto(f'file://{os.getcwd()}/{nm}.html'); pg.wait_for_timeout(600)
        os.makedirs(nm,exist_ok=True)
        for i in range(pg.locator('.s').count()): pg.locator(f'#s{i+1}').screenshot(path=f'{nm}/slide-{i+1}.png')
    b.close()
