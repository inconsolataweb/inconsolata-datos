"""Genera una mini web estática con el tema y posts reales, para probar fuera de Tumblr."""
import json, glob, sys, os, re, zipfile
sys.path.insert(0, 'scripts'); from tumblr_sim import render, post_ctx
tema, api, out = sys.argv[1:4]
ps = sorted([p for f in glob.glob(api + '/p_*.json') for p in json.load(open(f))['response']['posts']], key=lambda p: -p['timestamp'])
import random
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
if seed:
    random.seed(seed)
    meta = json.load(open('/home/claude/inconsolata-datos/datos/meta.json'))
    sec = lambda p: meta.get(p['id_string'], [''])[0]
    serie = lambda p: any(len(re.findall(r'inconsolata\.com/post/\d+', x)) >= 3 for x in re.findall(r'<p[^>]*>(.*?)</p>', p.get('body', '') or p.get('caption', ''), re.S)[-4:])
    multi = lambda p: len(meta.get(p['id_string'], ['', [], [], []])[3]) >= 2
    grupos = [([p for p in ps if sec(p) == 'm'], 4), ([p for p in ps if sec(p) == 'x'], 3), ([p for p in ps if sec(p) in 'bo' and sec(p)], 3),
              ([p for p in ps if serie(p)], 6), ([p for p in ps if multi(p) and sec(p) == ''], 6), ([p for p in ps if sec(p) == 'd'], 2),
              ([p for p in ps if sec(p) == ''], 16)]
    sel = []
    for g, n in grupos:
        g = [p for p in g if p['id'] not in {q['id'] for q in sel}]
        sel += random.sample(g, min(n, len(g)))
    sel.sort(key=lambda p: -p['timestamp'])
elif os.environ.get('PORTADA'):
    meta = json.load(open('/home/claude/inconsolata-datos/datos/meta.json'))
    k = os.environ['PORTADA']
    i0 = next(i for i, p in enumerate(ps) if meta.get(p['id_string'], [''])[0] == k) if k in ('m', 'x') else 0
    sel = ps[i0:i0 + 15]
else:
    extra = ['y-mucho-semana-cxxxii-5my', 'carnefresca', 'electroloro', 'las-infografías-con-animales-son-un-éxito']
    sel = ps[:24] + [p for p in ps if p['slug'] in extra or (p['date'] < '2013-02' and p['date'] > '2013-01-20')][:8]
sel = list({p['id']: p for p in sel}.values())
os.makedirs(out, exist_ok=True)
tpl = open(tema).read()
base = {'Title': 'inconsolata»', 'CurrentYear': '2026', 'RSS': '#', 'Favicon': '', 'MetaDescription': ''}
loc = {p['post_url']: 'post-%s.html' % p['id'] for p in sel}
def fix(h):
    for u, f in loc.items(): h = h.replace('href="%s"' % u, 'href="%s"' % f)
    return h
files = {'index.html': render(tpl, {**base, 'block:IndexPage': True, 'block:Posts': [post_ctx(p) for p in sel], 'block:Pagination': True})}
for i, p in enumerate(sel):
    ctx = {**base, 'block:PermalinkPage': True, 'block:Posts': [post_ctx(p)], 'block:PermalinkPagination': True}
    if i > 0: ctx.update({'block:PreviousPost': True, 'PreviousPost': 'post-%s.html' % sel[i-1]['id']})
    if i < len(sel) - 1: ctx.update({'block:NextPost': True, 'NextPost': 'post-%s.html' % sel[i+1]['id']})
    files['post-%s.html' % p['id']] = render(tpl, ctx)
if os.environ.get('PAGINAS'):
    for r in ('buscador', 'medios', 'autores', 'estadisticas', 'especiales', 'novedades', 'cronologia'):
        files[r + '.html'] = render(tpl, {**base, 'block:PermalinkPage': True, 'block:Posts': [post_ctx(sel[0])]})
with zipfile.ZipFile(out + '.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for n, h in files.items():
        nav = ("<script>document.addEventListener('click',function(e){var a=e.target.closest('a[href^=\"/\"]');if(!a)return;var h=a.getAttribute('href'),"
               "m=h.match(/^\\/(buscador|medios|autores|estadisticas|especiales|novedades|cronologia)(#.*)?$/),p=h.match(/^\\/post\\/(\\d+)/);e.preventDefault();"
               "if(h==='/')location.href='index.html';else if(m)location.href=m[1]+'.html'+(m[2]||'');else if(p&&window.__POSTS&&__POSTS.indexOf(p[1])>=0)location.href='post-'+p[1]+'.html';"
               "else window.open('https://inconsolata.com'+h,'_blank');},true);document.addEventListener('submit',function(e){var f=e.target.closest('.srch');if(!f)return;e.preventDefault();e.stopImmediatePropagation();var v=f.querySelector('input').value.trim();location.href='buscador.html'+(v?'#q='+encodeURIComponent(v):'');},true);window.__POSTS=" + json.dumps([str(p['id']) for p in sel]) + ";</script>")
        h = h.replace('</body>', nav + '</body>', 1)
        h = fix(h).replace('function get(f){', 'function get(f){if(window.__D&&__D[f])return Promise.resolve(__D[f]);', 1).replace('</head>', '<script src="datos.js"></script></head>', 1)
        open(os.path.join(out, n), 'w').write(h); z.writestr(os.path.basename(out) + '/' + n, h)
    D = {k: json.load(open('/home/claude/inconsolata-datos/datos/%s.json' % k)) for k in ('meta', 'catalogo', 'titulos', 'portada')}
    import datetime
    D['efemerides/%02d' % datetime.date.today().month] = json.load(open('/home/claude/inconsolata-datos/datos/efemerides/%02d.json' % datetime.date.today().month))
    if os.environ.get('PORTADA') in ('m', 'x'):
        tope = sel[0]['date'][:10]
        D['portada']['rec'] = [r for r in D['portada']['rec'] if r[2] <= tope]
    D['portada_manual'] = json.load(open(os.environ.get('MANUAL', '/home/claude/inconsolata-datos/datos/portada_manual.json')))
    if os.environ.get('PDATOS'):
        D['portada'] = json.load(open(os.environ['PDATOS']))
    if os.environ.get('PAGINAS'):
        for k in ('indice', 'archivo', 'estadisticas', 'fichas_medios', 'especiales', 'autores_fichas', 'cronologia'):
            D[k] = json.load(open('/home/claude/inconsolata-datos/datos/%s.json' % k))
    if os.environ.get('FICHAS_EXTRA'):
        for k, v in json.load(open(os.environ['FICHAS_EXTRA'])).items(): D['fichas_medios'].setdefault(k, {}).update(v)
    D['avisos'] = json.load(open(os.environ.get('AVISOS', '/home/claude/inconsolata-datos/datos/avisos.json')))
    js = 'window.__D=' + json.dumps(D, ensure_ascii=True, separators=(',', ':')) + ';'
    open(os.path.join(out, 'datos.js'), 'w').write(js); z.writestr(os.path.basename(out) + '/datos.js', js)
print(len(files))
