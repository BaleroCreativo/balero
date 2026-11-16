const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path=require('path');const D=__dirname;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let n=1;n<=9;n++){await p.goto('file://'+path.join(D,`slide-${n}.html`));await p.waitForTimeout(500);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:path.join(D,`carrusel-${n}.png`)});}
await b.close();console.log('ok')})()
