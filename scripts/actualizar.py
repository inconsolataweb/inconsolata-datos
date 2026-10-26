"""Actualización nocturna de los datos de inconsolata».

Lee los posts recientes de la API de Tumblr, los clasifica (sección, tipo de pieza, medios, autores, temas,
especiales) y actualiza datos/indice.json, datos/estadisticas.json y datos/especiales.json.
Los posts que ya estaban se vuelven a leer si son de los últimos días (por si se han editado).

Uso: TUMBLR_API_KEY=… python3 scripts/actualizar.py
     (para probar sin red: API_LOCAL=carpeta_con_p_*.json)
"""
import html, json, os, re, sys, glob, unicodedata, urllib.request
from collections import Counter
from datetime import datetime, timezone

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda f: os.path.join(RAIZ, 'datos', f)
BLOG = 'saulcastillo'
RELEER = 40          # cuántos posts recientes se vuelven a leer siempre (ediciones)
EXCLUIR = {'xaora', 'invitados', 'talie'}
NO_AUTORES = {'Sao Paulo', 'Nobel de Medicina'}   # nombres que se colaron como autores y no lo son
SERIES = ['aquí·allí', 'a fondo', 'sala de los horrores', 'teletipos', 'epílogo', 'inconsolab', 'entrevistas', 'audios', 'medios regionales', 'invitados']

def nz(s):
    s = unicodedata.normalize('NFKD', (s or '').lower().replace('’', "'").replace('`', "'"))
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

def nzs(s):   # versión para el pajar del buscador (igual que en la web)
    s = unicodedata.normalize('NFKD', (s or '').lower())
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9ñ]+', ' ', ''.join(c for c in s if not unicodedata.combining(c)))).strip()

# ---------------------------------------------------------------- lectura de la API
def api_posts():
    local = os.environ.get('API_LOCAL')
    if local:
        for f in sorted(glob.glob(os.path.join(local, 'p_*.json')), key=lambda f: int(re.search(r'p_(\d+)', f).group(1))):
            for p in json.load(open(f))['response']['posts']:
                yield p
        return
    key = os.environ['TUMBLR_API_KEY']
    off = 0
    while True:
        u = f'https://api.tumblr.com/v2/blog/{BLOG}.tumblr.com/posts?api_key={key}&limit=20&offset={off}&reblog_info=false'
        with urllib.request.urlopen(u, timeout=60) as r:
            ps = json.load(r)['response']['posts']
        if not ps:
            return
        for p in ps:
            yield p
        off += 20

# ---------------------------------------------------------------- extracción
TAG = re.compile(r'<[^>]+>')
def txt(h):
    return re.sub(r'\s+', ' ', html.unescape(TAG.sub(' ', h or ''))).strip()

IMG_RE = re.compile(r'<img\b[^>]*>', re.I)
def attr(tag, name):
    m = re.search(name + r'="([^"]*)"', tag)
    return m.group(1) if m else None

def srcset(t):
    out = []
    for x in (attr(t, 'srcset') or '').split(','):
        q = x.split()
        if len(q) == 2 and q[1].endswith('w') and q[1][:-1].isdigit():
            out.append((q[0], int(q[1][:-1])))
    return out

def imagenes(p):
    out = []
    if p['type'] == 'photo':
        for ph in p.get('photos', []):
            o = ph.get('original_size', {})
            out.append({'url': o.get('url'), 'w': o.get('width'), 'h': o.get('height'),
                        'ss': [(a['url'], a['width']) for a in ph.get('alt_sizes', []) if a.get('url') and a.get('width')]})
    if p['type'] == 'video' and p.get('thumbnail_url'):
        out.append({'url': p['thumbnail_url'], 'w': p.get('thumbnail_width'), 'h': p.get('thumbnail_height')})
    for field in ('body', 'caption'):
        for t in IMG_RE.findall(p.get(field) or ''):
            u = attr(t, 'src')
            if u and 'media.tumblr.com' in u:
                w, h = attr(t, 'data-orig-width'), attr(t, 'data-orig-height')
                out.append({'url': u, 'w': int(w) if w else None, 'h': int(h) if h else None, 'ss': srcset(t)})
    return out

def seccion(tags, titulo):
    tl = [t.lower().replace(' ', '') for t in tags]
    if 'muchomás' in tl or 'muchomas' in tl or titulo.lower().startswith('mucho más'):
        return 'muchomas'
    if 'extra!' in tl or 'extra' in tl:
        return 'extra'
    for s in ('detallitos', 'metablog', 'offtopic'):
        if s in tl:
            return s
    return 'normal'

def es_portadilla(sec, k, im, fecha):
    if sec not in ('muchomas', 'extra') or not im.get('w') or not im.get('h'):
        return False
    r = im['w'] / im['h']
    return (r >= 4.5 and 1200 <= im['w'] <= 1400) or (sec == 'muchomas' and k == 0 and r >= 4.5) or \
           (sec == 'muchomas' and k == 0 and 2.6 <= r <= 2.9 and fecha >= '2013')

def miniatura(im, ancho=400):
    """Versión pequeña de una imagen. En las imágenes nuevas de Tumblr cada tamaño tiene otro nombre de archivo,
    así que hay que elegirla de su lista de tamaños (srcset); cambiar el tamaño en la URL da un enlace roto."""
    if isinstance(im, str):
        im = {'url': im}
    ss = sorted(im.get('ss') or [], key=lambda x: x[1])
    if ss:
        ok = [u for u, w in ss if w >= ancho]
        return ok[0] if ok else ss[-1][0]
    u = im['url']
    if re.search(r'/s\d+x\d+/', u):     # formato nuevo sin lista de tamaños: mejor la original que un enlace roto
        return u
    return re.sub(r'_(\d+)(\.\w+)$', lambda m: '_400' + m.group(2) if int(m.group(1)) > 400 else m.group(0), u)

def primera_frase(t):
    t = re.sub(r'^[⩔\s]+', '', t or '').strip()
    m = re.match(r'(.{30,160}?[.!?])(\s|$)', t)
    return (m.group(1) if m else t[:150].rsplit(' ', 1)[0] + '…') if t else ''

DATE_PAT = r'(?:\d{1,2}(?: (?:y|al|-|–) \d{1,2})? de [a-záéíóú]+(?: de \d{4})?|[a-záéíóú]+ de \d{4}|\d{4})'
BOLD_RE = re.compile(r'<(b|strong)>(.*?)</\1>', re.S | re.I)
ITEM_RE = re.compile(r'<i>\s*Trabajo\s*</i>\s*:\s*(.*?)\|\s*<i>\s*Medio\s*</i>\s*:\s*<b>(.*?)</b>', re.S)

TIPO_TAG = [('carto', r'cartograf'), ('port', r'^portadas?$'), ('publi', r'^publicidad$'), ('video', r'^v[ií]deos?$'),
            ('foto', r'^fotograf'), ('ilus', r'^ilustraci'), ('graf', r'^gr[aá]ficos?$'), ('online', r'^(online|interactivos?)$'),
            ('info', r'^infograf')]
SEC = {'muchomas': 'm', 'extra': 'x', 'detallitos': 'd', 'metablog': 'b', 'offtopic': 'o', 'normal': ''}

# ---------------------------------------------------------------- catálogos
IDX = json.load(open(D('indice.json')))
ALIAS = json.load(open(D('alias.json')))
REGLAS = json.load(open(D('temas_reglas.json')))
ESP = json.load(open(D('especiales.json')))
# nombres nuevos que no se publican hasta que se revisen (autores y medios que no están en el catálogo)
try:
    PEND = json.load(open(D('pendientes.json')))
except Exception:
    PEND = {}
PEND.setdefault('autores', {}); PEND.setdefault('medios', {})
MED = [m['n'] for m in IDX['medios']]
AUT = [a['n'] for a in IDX['autores']]
TEM = [t['n'] for t in IDX['temas']]
for r in REGLAS:
    r['tg'] = re.compile(r'^(?:' + r['etiquetas'] + r')$') if r['etiquetas'] else None
    r['kw'] = re.compile(r['texto'], re.I)

def idx_de(lista, catalogo, n, nuevo):
    if n not in lista:
        lista.append(n); catalogo.append(nuevo(n))
    return lista.index(n)

def medio_de(nombre, fecha, tags):
    k = nz(nombre)
    if k == 'publico':
        return 'Público (España)' if fecha[:4] <= '2012' else 'Público (Portugal)'
    if k in ('la razon',) and any(nz(t) == 'la razon mex' for t in tags):
        return 'La Razón (México)'
    return ALIAS['medios'].get(k)

MESES = {'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'}
# para buscar autores ya conocidos en el texto libre, solo los que ya han salido al menos dos veces (evita falsos positivos)
CONOCIDOS = {k: n for k, n in ALIAS['autores'].items() if n in {a['n'] for a in IDX['autores'] if a['p'] >= 2}}
AUTOR_RE = re.compile(r'Autor(?:a|es|as)?\s*:\s*(.+?)(?=\s*(?:\||Medio\s*:|Fecha\s*:|$))')
def nombres(s):
    s = re.split(r'(?<=[a-zà-ÿ]{2})\.\s', s)[0]
    s = re.sub(r'\s+(?:y|e|&)\s+', ', ', s)
    return [x.strip(' .,;:') for x in s.split(',') if len(x.strip(' .,;:').split()) >= 2]

def clasificar(p):
    tags = p.get('tags', [])
    tl = [t.lower().strip() for t in tags]
    if EXCLUIR & set(tl):
        return None
    cuerpo = (p.get('body') or '') + (p.get('caption') or '')
    titulo_raw = (p.get('title') or '').strip()
    texto = txt(cuerpo.replace('[[MORE]]', ' '))
    if titulo_raw and texto.startswith(titulo_raw):
        texto = texto[len(titulo_raw):].strip()
    fecha = p['date'][:10]
    sec = seccion(tags, titulo_raw or texto[:40])
    ims = imagenes(p)
    for k, im in enumerate(ims):
        im['cover'] = es_portadilla(sec, k, im, fecha)
    items = [(txt(a), txt(b)) for a, b in ITEM_RE.findall(cuerpo)]
    # título
    titulo = re.sub(r'^\{(?:y mucho \+|a fondo|aquí·allí)\}:\s*', '', titulo_raw)
    if sec == 'muchomas':
        m = re.search(r'semana\s+([IVXLCDM]+)', titulo_raw + ' ' + texto[:80], re.I)
        titulo = 'Mucho más · semana ' + m.group(1).upper() if m else 'Mucho más'
    elif sec == 'extra':
        titulo = 'EXTRA! nº ' + str(1 + sum(1 for q in IDX['posts'] if q['s'] == 'x' and q['d'] < fecha))
    # medios: líneas de fuente en negrita, campos «Medio:» y etiquetas
    fuentes = []
    for para in re.findall(r'<p>(.*?)</p>', cuerpo, re.S):
        if re.search(DATE_PAT, txt(para).lower()) and BOLD_RE.search(para):
            fuentes += [txt(b).strip(' »,.:') for _, b in BOLD_RE.findall(para)]
    fuentes += [b for _, b in items] + tags
    medios = sorted({m for m in (medio_de(f, fecha, tags) for f in fuentes) if m})
    for f in fuentes[:len(fuentes) - len(tags)]:
        if f and not medio_de(f, fecha, tags) and len(f) < 60 and re.search(r'[A-Za-zÀ-ÿ]{3}', f) \
                and nz(f) not in MESES and not re.match(r'(?i)(ver|leer|extra|mucho|the$|el$|la$)', f.strip()):
            PEND['medios'].setdefault(f, []).append(p['post_url'])
    # autores: campos «Autor:» (se aceptan nombres nuevos) y nombres ya conocidos en el texto
    autores = set()
    for para in re.findall(r'<p>(.*?)</p>', cuerpo, re.S):
        for m in AUTOR_RE.finditer(txt(para)):
            for n in nombres(m.group(1)):
                if nz(n) in ALIAS['autores']:
                    autores.add(ALIAS['autores'][nz(n)])
                elif not ALIAS['medios'].get(nz(n)):
                    PEND['autores'].setdefault(n, []).append(p['post_url'])
    pajar = ' ' + nz(texto) + ' '
    for k, n in CONOCIDOS.items():
        if len(k) > 8 and ' ' in k and (' ' + k + ' ') in pajar:
            autores.add(n)
    # temas
    textos = [i[0] for i in items] if sec in ('muchomas', 'extra') else [titulo_raw + ' ' + texto]
    temas = {r['tema'] for r in REGLAS if (r['tg'] and any(r['tg'].match(t) for t in tl)) or any(r['kw'].search(x) for x in textos)}
    tipos = [c for c, rx in TIPO_TAG if any(re.search(rx, t) for t in tl)]
    th = next((im for im in ims if not im['cover']), ims[0] if ims else None)
    post = {
        'i': str(p['id']), 'u': p['post_url'].split('/post/', 1)[-1], 'd': fecha, 's': SEC[sec], 'k': tipos,
        't': titulo, 'b': primera_frase(texto),
        'x': nzs(titulo + ' ' + texto)[:700] + ((' ' + nzs(' '.join(i[0] for i in items))) if items else ''),
        'm': sorted(MED.index(m) for m in medios if m in MED),
        'a': sorted(AUT.index(a) for a in autores if a in AUT and a not in NO_AUTORES),
        'h': sorted(TEM.index(t) for t in temas if t in TEM),
        'g': [s for s in SERIES if s in tl],
        'im': miniatura(th) if th else '', 'r': round(th['w'] / th['h'], 2) if th and th.get('w') and th.get('h') else 1.3,
        'n': len(ims),
        '_tags': tl,
        '_fr': [[miniatura(im), (items[k][1] if k < len(items) else '')] for k, im in enumerate([im for im in ims if not im['cover']][:10])] if sec in ('muchomas', 'extra') else None,
    }
    return post

# ---------------------------------------------------------------- actualización
def main():
    existentes = {p['i']: p for p in IDX['posts']}
    nuevos, releidos = 0, 0
    vistos = 0
    for p in api_posts():
        vistos += 1
        pid = str(p['id'])
        if pid in existentes and vistos > RELEER:
            break
        if p.get('state', 'published') != 'published':
            continue
        q = clasificar(p)
        if q is None:
            existentes.pop(pid, None); continue
        if pid in existentes:
            releidos += 1
            # lo ya revisado a mano se conserva: se suma a lo detectado ahora, nunca se pierde
            old = existentes[pid]
            for key in ('a', 'm', 'h', 'k'):
                q[key] = sorted(set(q[key]) | set(old.get(key, [])), key=lambda x: (str(type(x)), x))
        else:
            nuevos += 1
        existentes[pid] = q
    posts = sorted(existentes.values(), key=lambda q: q['d'], reverse=True)
    malos = {AUT.index(n) for n in NO_AUTORES if n in AUT}
    for q in posts:
        q['a'] = [i for i in q['a'] if i not in malos]
    # especiales: posts con su etiqueta
    for e in ESP:
        ks = {nz(t).replace(' ', '') for t in e['tags']}
        for q in posts:
            if '_tags' in q and ks & {nz(t).replace(' ', '') for t in q['_tags']} and q['i'] not in e['posts']:
                e['posts'].append(q['i'])
        fechas = sorted(q['d'] for q in posts if q['i'] in set(e['posts']))
        if fechas:
            e['desde'], e['hasta'] = fechas[0], fechas[-1]
    frames = {q['i']: q.pop('_fr') for q in posts if q.get('_fr')}
    for q in posts:
        q.pop('_tags', None); q.pop('_fr', None)
    aplicar_estructura(posts)
    recontar(posts)
    IDX['posts'] = posts
    json.dump(IDX, open(D('indice.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    json.dump(ESP, open(D('especiales.json'), 'w'), ensure_ascii=False, indent=0)
    estadisticas(posts)
    escribir_meta(IDX)
    escribir_portada(IDX, frames)
    for k in PEND:
        for n in PEND[k]:
            PEND[k][n] = sorted(set(PEND[k][n]))
    json.dump(PEND, open(D('pendientes.json'), 'w'), ensure_ascii=False, indent=1)
    print('Pendientes de revisar:', {k: len(v) for k, v in PEND.items()})
    print(f'Posts nuevos: {nuevos} · releídos: {releidos} · total: {len(posts)}')

def aplicar_estructura(posts):
    """Jerarquía (datos/estructura.json): especiales hechos de un tema o de otros especiales, posts que heredan el tema
    padre de sus subtemas y especiales, temas ocultos y exclusiones."""
    EST = json.load(open(D('estructura.json')))
    TN = [t['n'] for t in IDX['temas']]
    ix = {n: i for i, n in enumerate(TN)}
    for t in IDX['temas']:
        t.pop('x', None)
    for n in EST.get('subtemas', {}):
        if n in ix: IDX['temas'][ix[n]]['x'] = 'sub'
    for n in EST.get('ocultos', []):
        if n in ix: IDX['temas'][ix[n]]['x'] = 'oculto'
    by = {e['slug']: e for e in ESP}
    LIM = EST.get('limpieza', {})
    for e in ESP:                                  # especiales hechos de un tema antiguo
        t = ix.get(e.get('de_tema'))
        if t is None:
            continue
        lim = LIM.get(e['slug'])
        if lim is not None:                        # fuera los recopilatorios sueltos y lo anterior a la fecha de inicio
            en_caps = set().union(*[set(by[c]['posts']) for c in e.get('capitulos', []) if c in by]) if e.get('capitulos') else set()
            for q in posts:
                if t in q['h'] and q['i'] not in en_caps and ((lim.get('desde') and q['d'] < lim['desde']) or q['s'] in ('m', 'x')):
                    q['h'] = [x for x in q['h'] if x != t]
            e['posts'] = sorted({q['i'] for q in posts if t in q['h']})
        else:
            e['posts'] = sorted(set(e['posts']) | {q['i'] for q in posts if t in q['h']})
    for e in ESP:                                  # especiales hechos de otros (sus capítulos)
        for c in e.get('capitulos', []):
            if c in by:
                e['posts'] = sorted(set(e['posts']) | set(by[c]['posts']))
    fecha = {q['i']: q['d'] for q in posts}
    for e in ESP:
        fs = sorted(fecha[i] for i in e['posts'] if i in fecha)
        if fs:
            e['desde'], e['hasta'] = fs[0], fs[-1]
    padre_de = {ix[k]: ix[v] for k, v in EST.get('subtemas', {}).items() if k in ix and v in ix}
    en_esp = {}
    for e in ESP:
        if e.get('padre') in ix:
            for i in e['posts']:
                en_esp.setdefault(i, set()).add(ix[e['padre']])
    exc = {ix[k]: {ix[x] for x in v if x in ix} for k, v in EST.get('excluye', {}).items() if k in ix}
    for q in posts:
        h = set(q['h'])
        for t in list(h):
            if t in padre_de: h.add(padre_de[t])
        h |= en_esp.get(q['i'], set())
        for t, otros in exc.items():
            if t in h and h & otros: h.discard(t)
        q['h'] = sorted(h)

def recontar(posts):
    for key, cat in (('m', IDX['medios']), ('a', IDX['autores']), ('h', IDX['temas'])):
        c = Counter(i for q in posts for i in q[key])
        ys = {}
        for q in posts:
            for i in q[key]:
                y = int(q['d'][:4]); lo, hi = ys.get(i, (y, y)); ys[i] = (min(lo, y), max(hi, y))
        for i, it in enumerate(cat):
            it['p'] = c.get(i, 0)
            if 'y' in it and i in ys:
                it['y'] = list(ys[i])

CDN = 'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/'
def escribir_meta(idx):
    global ESP_DE_TEMA
    ESP_DE_TEMA = {e['de_tema']: e['slug'] for e in ESP if e.get('de_tema')}
    """Archivos ligeros para el tema: qué medio, autores, temas y tipo tiene cada post, y el catálogo de nombres."""
    meta = {q['i']: [q['s'], q['k'], q['m'], q['a'], q['h']] for q in idx['posts']}
    json.dump(meta, open(D('meta.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    FM = json.load(open(D('fichas_medios.json')))
    AS = json.load(open(D('assets.json')))
    fam = lambda n: re.sub(r'\s+(USA|UK)$', '', n)
    def asset(kind, n):
        d = AS.get(kind, {})
        v = d.get(n) or d.get(fam(n))
        return CDN + v if v else ''
    med = []
    for m in idx['medios']:
        f = FM.get(m['n'], {})
        logo = asset('logos', m['n']) or (f.get('logo_url', '') + '?width=500' if f.get('logo_url') else '')
        med.append({'n': m['n'], 'slug': f.get('slug', ''), 'ficha': bool(f.get('ficha')), 'logo': logo,
                    'av': asset('avatares', m['n']), 'avw': asset('avatar_blanco', m['n']) or asset('avatares', m['n']),
                    'pais': f.get('pais', ''), 'cc': f.get('cc', '')})
    MI = {m['n']: i for i, m in enumerate(idx['medios'])}
    cat = {'medios': med, 'autores': [a['n'] for a in idx['autores']], 'am': [MI.get((a.get('m') or [''])[0], -1) for a in idx['autores']],
           'temas': [dict({'n': t['n'], 'b': t['b']}, **({'x': t['x']} if t.get('x') else {}), **({'e': ESP_DE_TEMA[t['n']]} if t['n'] in ESP_DE_TEMA else {})) for t in idx['temas']]}
    json.dump(cat, open(D('catalogo.json'), 'w'), ensure_ascii=False, separators=(',', ':'))

def escribir_portada(idx, frames):
    """Datos ligeros de la portada: lo último, el último mucho más y EXTRA! con sus fotogramas, el escaparate de temas,
    los medios del año y las efemérides («tal día como hoy», un archivo por mes)."""
    posts = idx['posts']
    try:
        TIT = json.load(open(D('titulos.json')))
    except Exception:
        TIT = {}
    try:
        old = json.load(open(D('portada.json')))
    except Exception:
        old = {}
    MN = [m['n'] for m in idx['medios']]
    def titulo(q):
        return TIT.get(q['i']) or q['t'] or q['b']
    def corto(q):
        return [q['i'], q['u'], q['d'], q['s'], q['k'], titulo(q), q['b'], [MN[i] for i in q['m'][:3]], q['im']]
    out = {'rec': [corto(q) for q in posts[:40]]}
    for sec in ('m', 'x'):
        q = next((q for q in posts if q['s'] == sec), None)
        if not q:
            continue
        fr = frames.get(q['i'])
        if not fr and (old.get(sec) or {}).get('i') == q['i']:
            fr = old[sec].get('fr')
        out[sec] = {'i': q['i'], 'u': q['u'], 'd': q['d'], 't': titulo(q), 'n': q['n'], 'fr': fr or ([[q['im'], '']] if q['im'] else []),
                    'm': [MN[i] for i in q['m']]}
        if sec == 'x':
            out[sec]['num'] = 1 + sum(1 for p in posts if p['s'] == 'x' and p['d'] < q['d'])
    # escaparate de temas: recuento y tres imágenes recientes de cada uno
    TE = idx['temas']
    vit = []
    for i, t in enumerate(TE):
        ims = [q['im'] for q in posts if i in q['h'] and q['im'] and q['s'] not in ('m', 'x')][:3]
        vit.append([i, t['n'], t['p'], t.get('b', ''), ims, t.get('x', '')])
    out['temas'] = vit
    out['esp'] = [[e['titulo'], e['slug'], e.get('tema', ''), len(e['posts']), e.get('hasta', ''), e.get('padre', ''), e.get('cap_de', '')] for e in ESP]
    # medios: los del año en curso (y los de siempre para el desplegable)
    y = str(datetime.now(timezone.utc).year)
    cy = Counter(i for q in posts if q['d'].startswith(y) for i in q['m'])
    ct = Counter(i for q in posts for i in q['m'])
    out['med'] = {'y': y, 'posts': sum(1 for q in posts if q['d'].startswith(y)),
                  'l': [[MN[i], cy.get(i, 0), ct[i]] for i in sorted(ct, key=lambda i: (-cy.get(i, 0), -ct[i]))]}
    out['anios'] = sorted({q['d'][:4] for q in posts})[0]
    # posts elegidos a mano en portada_manual.json, aunque ya no estén entre los recientes
    try:
        M = json.load(open(D('portada_manual.json')))
    except Exception:
        M = {}
    ids = set()
    for k in ('apertura', 'destacado'):
        o = M.get(k)
        if o:
            ids.add(str(o if isinstance(o, str) else o.get('id', '')))
    for o in M.get('fijos', []):
        ids.add(str(o if isinstance(o, str) else o.get('id', '')))
    rec = {r[0] for r in out['rec']}
    out['man'] = [corto(q) for q in posts if q['i'] in ids and q['i'] not in rec]
    json.dump(out, open(D('portada.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    # archivo ligero para las fichas de medios y autores y los especiales (el índice sin el texto de búsqueda)
    arch = {'posts': [{k: v for k, v in q.items() if k not in ('x', 'b', 'r')} for q in posts],
            'medios': idx['medios'], 'autores': idx['autores'], 'temas': idx['temas']}
    json.dump(arch, open(D('archivo.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    # efemérides: hasta tres posts de años distintos para cada día del año
    os.makedirs(D('efemerides'), exist_ok=True)
    por_dia = {}
    for q in posts:
        if q['s'] in ('m',) or not q['im']:
            continue
        por_dia.setdefault(q['d'][5:], {}).setdefault(q['d'][:4], q)
    for mes in range(1, 13):
        mm = '%02d' % mes
        res = {}
        for md, ys in por_dia.items():
            if not md.startswith(mm):
                continue
            años = sorted(ys)
            if len(años) > 3:      # repartidos: el más antiguo, uno intermedio y el más reciente
                años = [años[0], años[len(años) // 2], años[-1]]
            res[md[3:]] = [[a, ys[a]['u'], titulo(ys[a]), [MN[i] for i in ys[a]['m'][:1]], ys[a]['im']] for a in años]
        json.dump(res, open(D('efemerides/%s.json' % mm), 'w'), ensure_ascii=False, separators=(',', ':'))

def estadisticas(P):
    M, A, T = MED, AUT, TEM
    global MEDIO_AUT     # medio principal de cada autor, para poner su avatar junto al nombre
    MEDIO_AUT = {i: M.index(a['m'][0]) for i, a in enumerate(IDX['autores']) if a.get('m') and a['m'][0] in M}
    first = {}
    for p in sorted(P, key=lambda p: p['d']):
        for i in p['m']:
            first.setdefault(i, int(p['d'][:4]))
    def block(ps, year=None):
        cm, ca, ck, ct = Counter(), Counter(), Counter(), Counter()
        for p in ps:
            cm.update(p['m']); ca.update(p['a']); ck.update(p['k']); ct.update(p['h'])
        out = {'posts': len(ps), 'n_medios': len(cm), 'n_autores': len(ca),
               'medios': [[M[i], c, i] for i, c in cm.most_common(25)], 'autores': [[A[i], c, i, MEDIO_AUT.get(i)] for i, c in ca.most_common(15)],
               'tipos': dict(ck), 'temas': [[T[i], c, i] for i, c in ct.most_common(24)], 'imgs': sum(p['n'] for p in ps)}
        if year:
            out['meses'] = [sum(1 for p in ps if p['d'][5:7] == '%02d' % m) for m in range(1, 13)]
            out['nuevos'] = sorted([[M[i], cm[i], i] for i in cm if first[i] == year], key=lambda x: -x[1])[:16]
        return out
    y1 = datetime.now(timezone.utc).year
    years = {y: block([p for p in P if p['d'].startswith(str(y))], y) for y in range(2011, y1 + 1)}
    total = block(P)
    pres = Counter()
    for i in range(len(M)):
        pres[i] = len({p['d'][:4] for p in P if i in p['m']})
    total['fieles'] = [[M[i], c, i] for i, c in pres.most_common(12)]
    total['per_year'] = {y: years[y]['posts'] for y in years}
    total['medios_year'] = {y: years[y]['n_medios'] for y in years}
    json.dump({'total': total, 'years': years}, open(D('estadisticas.json'), 'w'), ensure_ascii=False)

if __name__ == '__main__':
    main()
