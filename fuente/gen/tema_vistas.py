"""Estilos y código de las vistas especiales del tema (mucho más, EXTRA!, metablog).
Los estilos se toman tal cual de las maquetas y se encierran en una clase del <body> (v-mm, v-x, v-b)
para que no choquen entre sí ni con los del post normal."""
import os, re
D = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(D, '..', 'html')

def _var(fichero, nombre):
    s = open(os.path.join(D, fichero)).read()
    m = re.search(nombre + r' = """(.*?)"""', s, re.S)
    return m.group(1)

def _reglas(css):
    out, depth, start = [], 0, 0
    for j, ch in enumerate(css):
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                out.append(css[start:j + 1].strip()); start = j + 1
    return [r for r in out if r]

def ambito(css, pre):
    """Antepone «pre» a cada selector (respetando @media y sin tocar @keyframes)."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    res = []
    for r in _reglas(css):
        if r.startswith('@keyframes'):
            res.append(r); continue
        if r.startswith('@media'):
            i = r.index('{')
            res.append(r[:i + 1] + ambito(r[i + 1:-1], pre) + '}'); continue
        i = r.index('{')
        sels = []
        for s in r[:i].split(','):
            s = s.strip()
            if s in ('html', 'body', ':root'):
                sels.append(s)
            elif s == '*':
                sels.append(pre + ' *')
            else:
                sels.append(pre + ' ' + s)
        res.append(','.join(sels) + r[i:])
    return '\n'.join(res)

def _mm_css():
    s = open(os.path.join(HTML, 'inconsolata-mucho-mas.html')).read()
    st = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    a = st.index('/* apertura amarilla */')
    b = st.index('@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}')
    c = st.index('.cover-fan{')
    e = st.index('.head .brand{display:block')
    return st[a:b] + st[c:e] + '.filters{top:56px}' + """
.filters.tk{overflow:hidden}
.tk-v{display:flex;width:max-content}
.tk-r{display:flex;align-items:center;gap:10px;padding:12px 10px 12px 24px;flex-shrink:0}
.tk-v.gira{animation:tkm var(--tk,40s) linear infinite}
.tk-v.gira:hover,.tk-v.gira:focus-within{animation-play-state:paused}
@keyframes tkm{to{transform:translateX(-50%)}}
.tk-l{font-size:13px;letter-spacing:3px;margin:0 2px 0 14px;white-space:nowrap}
.tk-l:first-child{margin-left:0}
.filters .tk-r button{white-space:nowrap}
.tk-t{display:inline-flex;align-items:center;gap:8px;white-space:nowrap;font:700 14px Archivo,sans-serif;color:var(--ink);background:var(--yellow);border:2px solid var(--ink);padding:8px 14px;min-height:44px;text-decoration:none}
.tk-t svg{width:24px;height:24px;overflow:visible}
.tk-t:hover{background:var(--ink);color:var(--paper)}
.tk-t.tk-e{background:var(--accent);color:#fff}
.tk-t.tk-e small{font-size:12px;opacity:.85}
.tk-t.tk-e:hover{background:var(--ink)}
.v-mm .item .txt .ico-esp{display:inline-block;color:var(--ink)}
.v-mm .item .txt .ico-esp .m{color:var(--accent)}
@media (prefers-reduced-motion:reduce){.filters.tk{overflow-x:auto}}
"""

VCSS = (ambito(_mm_css(), '.v-mm')
        + ambito(_var('extra.py', 'XCSS'), '.v-x')
        + ambito(_var('metablog.py', 'MCSS') + _var('sismolive.py', 'SCSS'), '.v-b')
        + """
.v-mm .mm-top .legacy,.v-x .mm-top .legacy{margin:16px 0}
.v-mm .close .pn{border:2px solid var(--ink);padding:28px;display:flex;flex-direction:column;gap:8px}
.v-mm .close .pn .big{font-size:44px;line-height:1}
.v-mm .item .txt .ico{display:block}
.v-x .idx .tx b{font-weight:700}
.v-x .idx .k-n{white-space:nowrap}
.v-x .prev-row.y{display:grid}
.v-x .prev-row .ls a{border:2px solid var(--ink);padding:10px 14px;font-size:14px;font-weight:700;min-height:44px}
.v-x .idx .k-n.w{font-size:40px}
.v-b .col img{max-width:100%;height:auto}
.v-b .col figure.pair{grid-template-columns:repeat(var(--n,2),minmax(0,1fr))}
.v-b .col .vid{margin:0 0 26px}
.v-b .hero-one .fshot{display:block}
.v-b .mhead h1 em{color:var(--accent)}
.v-b .mhead h1.long{font-size:clamp(40px,5.2vw,84px);line-height:.95;letter-spacing:-.02em}
.v-mm .item .desc{margin:0;font-family:'Fraunces',serif;font-size:19px;line-height:1.45}
.v-mm .item .desc strong,.v-mm .item .desc b{font-weight:700}
""")

VJS = open(os.path.join(D, 'tema_vistas.js')).read()
