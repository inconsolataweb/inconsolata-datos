import base64, json, re, sys
D = '/tmp/claude-0/-home-claude/b753561d-def2-5a8d-ab88-1423c0df1d75/scratchpad/pres/'
t = open(D + 'tpl.html').read()
cache = {}
def img(m):
    n = m.group(1)
    if n not in cache:
        cache[n] = 'data:image/jpeg;base64,' + base64.b64encode(open(D + 'img/' + n + '.jpg', 'rb').read()).decode()
    return cache[n]
# imágenes repetidas: una sola vez como variable CSS no sirve en <img>, así que se repiten (son pocas)
t = re.sub(r'\{\{img:(\w+)\}\}', img, t)
py = json.load(open('/home/claude/inconsolata-datos/datos/estadisticas.json'))['total']['per_year']
mx = max(py.values())
bars = ''.join(f'<div><b>{v}</b><i style="--v:{v/mx:.3f};--k:{k}"></i><span>’{y[2:]}</span></div>' for k, (y, v) in enumerate(py.items()))
t = t.replace('{{barras}}', bars)
open(sys.argv[1], 'w').write(t)
print(len(t) // 1024, 'KB')
