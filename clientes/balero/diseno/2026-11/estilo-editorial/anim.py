import sys,os,subprocess,shutil
from playwright.sync_api import sync_playwright
src,outdir=sys.argv[1],sys.argv[2]; os.makedirs(outdir,exist_ok=True)
FPS=30
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--allow-file-access-from-files','--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1440}); pg.goto('file:///'+src); pg.wait_for_timeout(800)
    pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
    for i in range(1,7):
        pg.evaluate("n=>document.querySelectorAll('.s').forEach((s,k)=>s.style.display=(k+1==n)?'block':'none')",i)
        dur=6.0 if i==1 else 5.0
        fd=f'{outdir}/f{i}'; shutil.rmtree(fd,ignore_errors=True); os.makedirs(fd)
        for f in range(int(dur*FPS)):
            pg.evaluate("t=>document.getAnimations().forEach(a=>{a.currentTime=t})",f/FPS*1000)
            pg.locator(f'#s{i}').screenshot(path=f'{fd}/{f:04d}.png')
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{fd}/%04d.png','-c:v','libx264','-pix_fmt','yuv420p','-crf','16',f'{outdir}/slide{i}.mp4'],check=True)
        shutil.rmtree(fd)
    b.close()
