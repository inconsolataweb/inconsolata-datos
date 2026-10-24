"""Simulador mínimo del motor de temas de Tumblr para probar el tema con posts reales de la API.
Uso: python3 tumblr_sim.py <tema.html> <carpeta_api> <slug|index> <salida.html>
"""
import sys, re, json, glob, html as H

def render(tpl, ctx):
    out, i = [], 0
    pat = re.compile(r'\{block:([A-Za-z]+)\}')
    while True:
        m = pat.search(tpl, i)
        if not m:
            out.append(sub(tpl[i:], ctx)); break
        out.append(sub(tpl[i:m.start()], ctx))
        name = m.group(1)
        # buscar el cierre correspondiente (con anidamiento del mismo nombre)
        depth, j = 1, m.end()
        op, cl = '{block:%s}' % name, '{/block:%s}' % name
        while depth:
            a, b = tpl.find(op, j), tpl.find(cl, j)
            if b == -1:
                raise ValueError('sin cierre ' + name)
            if a != -1 and a < b:
                depth += 1; j = a + len(op)
            else:
                depth -= 1; j = b + len(cl)
        inner = tpl[m.end():j - len(cl)]
        v = ctx.get('block:' + name)
        if isinstance(v, list):
            for c in v:
                out.append(render(inner, {**ctx, **c}))
        elif v:
            out.append(render(inner, ctx))
        i = j
    return ''.join(out)

def sub(s, ctx):
    return re.sub(r'\{([A-Z][A-Za-z0-9\-]*)\}', lambda m: str(ctx.get(m.group(1), '')), s)

def post_ctx(p):
    d = p['date'][:10]
    c = {'PostID': p['id'], 'Year': d[:4], 'MonthNumberWithZero': d[5:7], 'DayOfMonthWithZero': d[8:10], 'DayOfMonth': int(d[8:10]),
         'ShortMonth': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(d[5:7]) - 1],
         'Permalink': p['post_url'], 'URLEncodedPermalink': p['post_url'], 'ReblogURL': '#'}
    c['block:Tags'] = [{'Tag': H.escape(t)} for t in p.get('tags', [])]
    if p.get('title'):
        c['block:Title'] = True; c['Title'] = H.escape(p['title'])
    t = p['type']
    if t == 'text':
        c['block:Text'] = True; c['Body'] = p.get('body', ''); c['PlaintextBody'] = H.escape(re.sub('<[^>]+>', ' ', p.get('body', '')))[:400]
    elif t == 'photo':
        ph = p.get('photos', [])
        cap = p.get('caption', '')
        if len(ph) == 1:
            o = ph[0]['original_size']
            c.update({'block:Photo': True, 'PhotoURL-HighRes': o['url'], 'PhotoWidth-HighRes': o['width'], 'PhotoHeight-HighRes': o['height'], 'PhotoURL-500': o['url'], 'Caption': cap})
        else:
            c.update({'block:Photoset': True, 'Caption': cap, 'block:Photos': [{'PhotoURL-500': x['original_size']['url'], 'PhotoURL-HighRes': x['original_size']['url'], 'PhotoWidth-HighRes': x['original_size']['width'], 'PhotoHeight-HighRes': x['original_size']['height']} for x in ph]})
        c['PlaintextCaption'] = H.escape(re.sub('<[^>]+>', ' ', cap))[:400]
    elif t == 'video':
        c.update({'block:Video': True, 'Video-700': '<div style="background:#000;height:300px"></div>', 'Caption': p.get('caption', '')})
    return c

if __name__ == '__main__':
    tema, api, which, out = sys.argv[1:5]
    posts = [p for f in glob.glob(api + '/p_*.json') for p in json.load(open(f))['response']['posts']]
    posts.sort(key=lambda p: -p['timestamp'])
    tpl = open(tema).read()
    base = {'Title': 'inconsolata»', 'CurrentYear': '2026', 'RSS': '#', 'Favicon': '', 'MetaDescription': ''}
    if which == 'index':
        ctx = {**base, 'block:IndexPage': True, 'block:Posts': [post_ctx(p) for p in posts[:12]], 'block:Pagination': True, 'block:NextPage': True, 'NextPage': '#'}
    else:
        p = next(p for p in posts if p['slug'] == which or str(p['id']) == which)
        ctx = {**base, 'block:PermalinkPage': True, 'block:Posts': [post_ctx(p)], 'block:PermalinkPagination': True,
               'block:NextPost': True, 'NextPost': '#', 'block:PreviousPost': True, 'PreviousPost': '#',
               'block:PostTitle': bool(p.get('title')), 'PostTitle': p.get('title', '')}
    open(out, 'w').write(render(tpl, ctx))
