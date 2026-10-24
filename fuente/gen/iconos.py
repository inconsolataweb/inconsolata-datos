import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import TIPOS, icon
from posts import OUT
cells=''.join(f'<figure>{icon(k)}<figcaption>{v[0]}</figcaption></figure>' for k,v in TIPOS.items())
html=f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Iconos de tipo · inconsolata» (maqueta)</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>
body{{margin:0;background:#ECE7DC;color:#16140F;font-family:'Archivo',sans-serif}}
.k{{color:#16140F}}.m{{color:#D1006F;mix-blend-mode:multiply}}
main{{max-width:1200px;margin:0 auto;padding:48px 24px}}
h1{{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:56px;margin:0 0 8px}}
p{{margin:0 0 36px;font-size:17px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:20px}}
figure{{margin:0;background:#fff;border:2px solid #16140F;padding:28px 16px 16px;display:flex;flex-direction:column;align-items:center;gap:16px}}
figure svg{{width:120px;height:120px}}
figcaption{{font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase}}
.sp{{display:flex;align-items:center;gap:24px;margin-top:40px;border-top:2px solid #16140F;padding-top:24px}}
.sp svg{{width:120px;height:120px}}
</style></head><body><main>
<h1>iconos de tipo</h1><p>Los nueve tipos de pieza. En la web van sin texto; el nombre aparece al pasar el ratón.</p>
<div class="grid">{cells}</div>

</main></body></html>"""
open(os.path.join(OUT,'iconos.html'),'w').write(html); print('ok')
