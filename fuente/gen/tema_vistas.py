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
.item .txt .ico-esp{display:inline-block;color:var(--ink)}
.item .txt .md-l{display:flex;flex-wrap:wrap;align-items:center;row-gap:6px}
.item .txt .supl{display:inline-block;margin-left:12px;padding-left:10px;border-left:2px solid currentColor;font:800 13px 'Archivo',sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--muted);vertical-align:middle}
.item .txt .ico-esp .m{color:var(--accent)}
@media (prefers-reduced-motion:reduce){.filters.tk{overflow-x:auto}}
"""

VCSS = (ambito(_mm_css(), '.v-mm')
        + ambito(_var('extra.py', 'XCSS'), '.v-x')
        + ambito(_var('metablog.py', 'MCSS') + _var('sismolive.py', 'SCSS'), '.v-b')
        + """
/* ===== móvil: mucho más ===== */
html.lite .v-mm .mm-hero .inner{display:block;padding:22px 16px 20px}
html.lite .v-mm .mm-hero .txt{gap:10px}
html.lite .v-mm .mm-hero .caps{font-size:11px!important;letter-spacing:2px!important}
html.lite .v-mm .mm-hero h1{font-size:40px;line-height:.95}
html.lite .v-mm .mm-hero .num{font-size:30px;line-height:1;-webkit-text-stroke:0;color:var(--ink)}
html.lite .v-mm .mm-hero p{font-size:16px;line-height:1.45}
html.lite .v-mm .cover-fan{display:none}
html.lite .v-mm .index .thumbs{display:flex!important;overflow-x:auto;gap:8px;padding:6px 16px;scrollbar-width:none}
html.lite .v-mm .index .thumbs a{flex:0 0 84px}
html.lite .v-mm .index .thumbs .t{height:100px}
html.lite .v-mm .index .thumbs span{font-size:9px;letter-spacing:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
html.lite .v-mm .filters{position:relative;top:auto}
html.lite .v-mm .filters .tk-r{padding:8px 10px 8px 16px;gap:8px}
html.lite .v-mm .filters button,html.lite .v-mm .tk-t{min-height:36px;padding:6px 10px;font-size:13px}
html.lite .v-mm .filters svg,html.lite .v-mm .tk-t svg{width:18px;height:18px}
.vz-bar{display:none}
html.lite .vz-bar{display:grid;grid-template-columns:44px 1fr 44px auto;align-items:center;gap:6px;padding:8px 12px 10px 8px;background:var(--ink);color:var(--paper);position:sticky;top:0;z-index:9;margin:0 calc(50% - 50vw)}
.vz-bar button{background:none;border:0;color:inherit;font:inherit;cursor:pointer}
.vz-p,.vz-s{font:900 30px/1 'Fraunces',serif!important;color:var(--yellow)!important;height:40px}
.vz-n{text-align:center;font:800 13px 'Archivo',sans-serif;letter-spacing:2px}
.vz-m{font:800 10px 'Archivo',sans-serif!important;letter-spacing:1.5px;text-transform:uppercase;border:2px solid var(--yellow)!important;color:var(--yellow)!important;padding:7px 8px!important}
.vz-pr{grid-column:1/-1;height:3px;background:#3A3731;display:block}.vz-pr i{display:block;height:100%;background:var(--yellow);width:0;transition:width .2s}
.vz-bar.lista .vz-p,.vz-bar.lista .vz-s,.vz-bar.lista .vz-pr{visibility:hidden}
html.lite .v-mm #items .item{display:flex;flex-direction:column;gap:14px;padding:22px 16px 26px;margin:0;border-bottom:1px solid #C9C4B8}
html.lite .v-mm #items .item .img{order:1;transform:none!important;box-shadow:5px 5px 0 var(--ink);padding:8px;min-height:0;grid-column:auto;border:2px solid var(--ink)}
html.lite .v-mm #items .item .img img{max-height:70vh;width:100%;object-fit:contain}
html.lite .v-mm #items .item .tape,html.lite .v-mm #items .item .zoom{display:none}
html.lite .v-mm #items .item .txt{order:2;grid-column:auto;gap:8px}
html.lite .v-mm #items .item .txt .ico,html.lite .v-mm #items .item .txt .ico-esp{display:none}
html.lite .v-mm #items .item h2{font-size:21px;line-height:1.15}
html.lite .v-mm #items .item .medio{font-size:11px;letter-spacing:1.5px;gap:8px}
html.lite .v-mm #items .item .medio .av{width:24px;height:24px}
html.lite .v-mm #items .item .supl{font-size:10px;letter-spacing:1.5px;margin-left:8px;padding-left:8px}
html.lite .v-mm #items .item .by{font-size:15px}
html.lite .v-mm #items .item .when{font-size:12px}
html.lite .v-mm #items .item .desc{font-size:16px}
html.lite .v-mm #items.visor{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain;scrollbar-width:none;align-items:flex-start}
html.lite .v-mm #items.visor::-webkit-scrollbar{display:none}
html.lite .v-mm #items.visor .item{flex:0 0 100%;width:100%;scroll-snap-align:start;scroll-snap-stop:always;border-bottom:0}
html.lite .v-mm #items.visor .item[hidden]{display:none}
html.lite .v-mm #items.visor .item .img{display:flex;align-items:center;justify-content:center;height:58vh;background:#fff}
html.lite .v-mm #items.visor .item .img img{max-height:100%;height:100%;object-fit:contain}
html.lite .v-mm .close{padding:0 16px;display:flex;flex-direction:column;gap:12px}
html.lite .v-mm .close .pn{padding:16px}html.lite .v-mm .close .pn .big{font-size:26px}
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
