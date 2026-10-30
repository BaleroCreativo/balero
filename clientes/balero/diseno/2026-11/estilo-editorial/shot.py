import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--allow-file-access-from-files','--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1440})
    pg.goto('file:///'+sys.argv[1]); pg.wait_for_timeout(600)
    for i in (1,2):
        pg.locator(f'#s{i}').screenshot(path=f'{sys.argv[2]}-{i}.png')
    b.close()
