import sys
from playwright.sync_api import sync_playwright
src,out,n=sys.argv[1],sys.argv[2],int(sys.argv[3])
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--allow-file-access-from-files','--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1440}); pg.goto('file:///'+src); pg.wait_for_timeout(700)
    for i in range(1,n+1): pg.locator(f'#s{i}').screenshot(path=f'{out}-{i}.png')
    b.close()
