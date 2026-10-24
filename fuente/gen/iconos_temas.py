import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from temas_iconos import TI, slug, tema_symbols
from posts import OUT
import json
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'search.json')))
blo = {t['n']: t['b'] for t in D['temas']}
order = []
for t in D['temas']:
    if t['b'] not in order: order.append(t['b'])
secs = ''
for b in order:
    cells = ''.join(f'<figure><svg viewBox="0 0 64 64" style="overflow:visible"><use href="#{slug(n)}" class="k"/><use href="#{slug(n)}" class="m" x="3" y="2.5"/></svg><figcaption>{n}</figcaption></figure>'
                    for n in TI if blo.get(n) == b)
    secs += f'<h2>{b}</h2><div class="grid">{cells}</div>'
html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Iconos de temas · inconsolata»</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>
body{{margin:0;background:#ECE7DC;color:#16140F;font-family:'Archivo',sans-serif}}
.k{{color:#16140F}}.m{{color:#D1006F;mix-blend-mode:multiply}}
main{{max-width:1200px;margin:0 auto;padding:48px 24px}}
h1{{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:56px;margin:0 0 8px}}
h2{{font-size:13px;font-weight:800;letter-spacing:2px;text-transform:uppercase;border-bottom:2px solid #16140F;padding-bottom:6px;margin:40px 0 16px}}
p{{margin:0;font-size:17px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:16px}}
figure{{margin:0;background:#fff;border:2px solid #16140F;padding:22px 12px 14px;display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center}}
figure svg{{width:84px;height:84px}}
figcaption{{font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:16px;line-height:1.15}}
</style></head><body>{tema_symbols()}<main>
<h1>iconos de temas</h1><p>Uno por tema, con el mismo trazo y el mismo desfase de tinta que los iconos de tipo y la urna.</p>
{secs}
</main></body></html>"""
open(os.path.join(OUT, 'iconos-temas.html'), 'w').write(html); print('ok', len(TI))
