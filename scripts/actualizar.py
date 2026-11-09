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
RELEER = int(os.environ.get('RELEER') or 40)   # cuántos posts recientes se vuelven a leer siempre (ediciones); RELEER=99999 relee todo
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

def npf_web(pid):
    """Especial web: el formato antiguo de la API pierde los bloques de enlace y a veces el texto; se leen en NPF."""
    if os.environ.get('API_LOCAL'):
        return {}
    u = f'https://api.tumblr.com/v2/blog/{BLOG}.tumblr.com/posts?api_key={os.environ["TUMBLR_API_KEY"]}&id={pid}&npf=true'
    try:
        with urllib.request.urlopen(u, timeout=60) as r:
            ps = json.load(r)['response']['posts']
    except Exception as e:
        print('No se pudo leer en NPF el post', pid, e)
        return {}
    out = {'lk': '', 'tx': []}
    for b in (ps[0].get('content') or []) if ps else []:
        if b.get('type') == 'link':
            out['lk'] = out['lk'] or b.get('url', '')
            if b.get('description'):
                out['tx'].append(b['description'])
            out['lt'] = out.get('lt') or b.get('title', '')
        elif b.get('type') == 'text' and b.get('subtype') not in ('heading1', 'heading2') and b.get('text'):
            out['tx'].append(b['text'])
            for f in b.get('formatting') or []:
                if f.get('type') == 'link' and not out['lk'] and 'tumblr.com' not in f.get('url', ''):
                    out['lk'] = f['url']
    print('ESPECIAL WEB (NPF)', pid, out['lk'], ' '.join(out['tx'])[:120])
    return out

def api_post(pid):
    if os.environ.get('API_LOCAL'):
        return None
    u = f'https://api.tumblr.com/v2/blog/{BLOG}.tumblr.com/posts?api_key={os.environ["TUMBLR_API_KEY"]}&id={pid}'
    try:
        with urllib.request.urlopen(u, timeout=60) as r:
            ps = json.load(r)['response']['posts']
        return ps[0] if ps else None
    except Exception as e:
        print('No se pudo leer el post', pid, e)
        return None

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
    if p.get('link_image'):
        out.append({'url': p['link_image'], 'w': None, 'h': None, 'ss': []})
    for field in ('body', 'caption', 'description'):
        for t in IMG_RE.findall(p.get(field) or ''):
            u = attr(t, 'src')
            if u and 'media.tumblr.com' in u:
                w, h = attr(t, 'data-orig-width'), attr(t, 'data-orig-height')
                out.append({'url': u, 'w': int(w) if w else None, 'h': int(h) if h else None, 'ss': srcset(t)})
    return out

def seccion(tags, titulo):
    tl = [t.lower().replace(' ', '') for t in tags]
    if 'especialweb' in tl:
        return 'web'
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

def resumen(t, n=230):
    """Entradilla de portada: frases enteras hasta unos n caracteres (como hace la portada con los posts de la página)."""
    t = re.sub(r'\s+', ' ', re.sub(r'^[⩔\s]+', '', t or '')).strip()
    fr = re.findall(r'[^.!?]+[.!?]+(?=\s|$)', t)
    r = ''
    for x in fr:
        x = x.strip()
        if not r:
            r = x
            if len(r) >= 70:
                break
        elif len(r) + 1 + len(x) <= n:
            r += ' ' + x
            break
        else:
            break
    r = r or t
    if len(r) > n * 1.45:
        r = re.sub(r'[,;:\s]+$', '', re.sub(r'\s+\S*$', '', r[:int(n * 1.45)])) + '…'
    return r

DATE_PAT = r'(?:\d{1,2}(?: (?:y|al|-|–) \d{1,2})? de [a-záéíóú]+(?: de \d{4})?|[a-záéíóú]+ de \d{4}|\d{4})'
BOLD_RE = re.compile(r'<(b|strong)>(.*?)</\1>', re.S | re.I)
ITEM_RE = re.compile(r'<i>\s*Trabajo\s*</i>\s*:\s*(.*?)\|\s*<i>\s*Medio\s*</i>\s*:\s*<b>(.*?)</b>', re.S)

TIPO_TAG = [('carto', r'cartograf'), ('port', r'^portadas?$'), ('publi', r'^publicidad$'), ('video', r'^v[ií]deos?$'),
            ('foto', r'^fotograf'), ('ilus', r'^ilustraci'), ('graf', r'^gr[aá]ficos?$'), ('online', r'^(online|interactivos?)$'),
            ('info', r'^infograf')]
SEC = {'web': 'w', 'muchomas': 'm', 'extra': 'x', 'detallitos': 'd', 'metablog': 'b', 'offtopic': 'o', 'normal': ''}

# ---------------------------------------------------------------- catálogos
IDX = json.load(open(D('indice.json')))
ALIAS = json.load(open(D('alias.json')))
REGLAS = json.load(open(D('temas_reglas.json')))
ESP = json.load(open(D('especiales.json')))
# ajustes hechos desde el panel de portada: etiquetas que se añaden o se quitan a un post (sin tocar Tumblr)
try:
    AJ = json.load(open(D('ajustes_posts.json')))
except Exception:
    AJ = {}
# etiquetas originales de Tumblr de cada post, para enseñarlas en el panel
try:
    ETQ = json.load(open(D('etiquetas.json')))
except Exception:
    ETQ = {}
# nombres nuevos que no se publican hasta que se revisen (autores y medios que no están en el catálogo)
try:
    PEND = json.load(open(D('pendientes.json')))
except Exception:
    PEND = {}
PEND.setdefault('autores', {}); PEND.setdefault('medios', {})
MED = [m['n'] for m in IDX['medios']]
AUT = [a['n'] for a in IDX['autores']]
TEM = [t['n'] for t in IDX['temas']]
# temas nuevos de temas_reglas.json que aún no están en el índice
for r in REGLAS:
    if r['tema'] not in TEM:
        IDX['temas'].append({'n': r['tema'], 'b': r.get('bloque', ''), 'p': 0, 'h': True}); TEM.append(r['tema'])
# el bloque de cada tema manda desde temas_reglas.json
_BQ = {r['tema']: r.get('bloque', '') for r in REGLAS}
for t in IDX['temas']:
    if _BQ.get(t['n']): t['b'] = _BQ[t['n']]
for r in REGLAS:
    r['tg'] = re.compile(r'^(?:' + r['etiquetas'] + r')$') if r['etiquetas'] else None
    r['kw'] = re.compile(r['texto'], re.I)

def idx_de(lista, catalogo, n, nuevo):
    if n not in lista:
        lista.append(n); catalogo.append(nuevo(n))
    return lista.index(n)

TIPO_N = {'infografia': 'info', 'cartografia': 'carto', 'mapa': 'carto', 'grafico': 'graf', 'ilustracion': 'ilus', 'portada': 'port', 'fotografia': 'foto', 'video': 'video', 'online': 'online'}
MES_N = {m: i + 1 for i, m in enumerate(['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'])}
FECHA_RE = re.compile(r'(\d{1,2})\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)(?:\s+(?:de|del)\s+(\d{4}))?', re.I)

def fecha_trabajo(texto, fecha_post):
    """Fecha de la pieza («Medio, del 1 de noviembre», «…del 30 de agosto; 6 y 13 de septiembre de 2026»): la más reciente
    que se cita; sin año se entiende la del post (o la del año anterior si quedaría muy por delante). '' si no hay."""
    from datetime import date
    try:
        fp = date.fromisoformat(fecha_post)
    except Exception:
        return ''
    mejor = None
    for d, mes, y in FECHA_RE.findall(texto or ''):
        m = MES_N.get(mes.lower().replace('setiembre', 'septiembre'))
        try:
            if y:
                f = date(int(y), m, int(d))
            else:
                f = date(fp.year, m, int(d))
                if (f - fp).days > 20:
                    f = date(fp.year - 1, m, int(d))
        except Exception:
            continue
        if (f - fp).days > 20 or (fp - f).days > 3660:
            continue
        if not mejor or f > mejor:
            mejor = f
    return mejor.isoformat() if mejor else ''

def medio_de(nombre, fecha, tags):
    # fuera el número de la edición: «Negocios (El País) #2.139», «… nº 45»
    nombre = re.sub(r'\s*(?:#|n\.?º\s*|núm\.?\s*)[\d.,]+\s*$', '', nombre or '', flags=re.I)
    k = nz(nombre)
    if k not in ALIAS['medios']:
        # «Suplemento (Medio)»: si lo de dentro del paréntesis es un medio conocido, cuenta como ese medio
        m_ = re.search(r'\(([^()]+)\)\s*$', nombre)
        if m_ and nz(m_.group(1)) in ALIAS['medios'] and nz(re.sub(r'\([^()]*\)', ' ', nombre) + ' ' + m_.group(1)) in ALIAS['medios']:
            k = nz(re.sub(r'\([^()]*\)', ' ', nombre) + ' ' + m_.group(1))
        elif m_ and nz(m_.group(1)) in ALIAS['medios']:
            k = nz(m_.group(1))
    if k == 'publico':
        return 'Público (España)' if fecha[:4] <= '2012' else 'Público (Portugal)'
    if k in ('la razon',) and any(nz(t) == 'la razon mex' for t in tags):
        return 'La Razón (México)'
    return ALIAS['medios'].get(k)

MESES = {'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'}
# para buscar autores ya conocidos en el texto libre, solo los que ya han salido al menos dos veces (evita falsos positivos)
CONOCIDOS = {k: n for k, n in ALIAS['autores'].items() if n in {a['n'] for a in IDX['autores'] if a['p'] >= 2}}
AUTOR_RE = re.compile(r'(?:Autor(?:a|es|as)?|Ilustraci(?:ón|ones))\s*:\s*(.+?)(?=\s*(?:\||Medio\s*:|Fecha\s*:|$))')
def nombres(s):
    s = re.split(r'(?<=[a-zà-ÿ]{2})\.\s', s)[0]
    s = re.sub(r'\s+(?:y|e|&)\s+', ', ', s)
    return [x.strip(' .,;:') for x in s.split(',') if len(x.strip(' .,;:').split()) >= 2]

def con_ajustes(pid, tags):
    aj = AJ.get(pid) or {}
    menos = {nz(t) for t in aj.get('menos', [])}
    tags = [t for t in tags if nz(t) not in menos]
    ya = {nz(t) for t in tags}
    return tags + [t for t in aj.get('mas', []) if nz(t) not in ya]

def clasificar(p):
    ETQ[str(p['id'])] = p.get('tags', [])
    tags = con_ajustes(str(p['id']), p.get('tags', []))
    tl = [t.lower().strip() for t in tags]
    if EXCLUIR & set(tl):
        return None
    cuerpo = (p.get('body') or '') + (p.get('caption') or '') + (p.get('description') or '')
    if os.environ.get('DEPURA') and str(p['id']) == os.environ['DEPURA']:
        print('DEPURA_JSON', json.dumps(p, ensure_ascii=False))
    # piezas con tipo y etiquetas delante: «cartografía | elecciones 29-N, encuestas | Trabajo: … | Autor: … | Medio: …»
    tipos_pz, etq_pz = [], []
    for para in re.findall(r'<p>(.*?)</p>', cuerpo, re.S):
        pt = txt(para)
        if not re.search(r'Trabajo\s*:', pt):
            continue
        segs = [x.strip(' .') for x in pt.split('Trabajo', 1)[0].split('|')]
        segs = [x for x in segs if x and ':' not in x and len(x) < 120]
        if segs:
            tipos_pz.append(segs[0].lower())
        if len(segs) > 1:
            etq_pz += [e.strip().lower() for e in segs[1].split(',') if e.strip()]
    if etq_pz:
        tl = tl + [e for e in dict.fromkeys(etq_pz) if e not in tl]
    titulo_raw = (p.get('title') or '').strip()
    texto = txt(cuerpo.replace('[[MORE]]', ' '))
    texto = re.sub(r'<([^<>\s][^<>]{0,118})>', r'\1', texto)   # <palabras> subrayadas a mano
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
        m = re.search(r'semana\s+([IVXLCDM]+)(?![A-Za-zÁÉÍÓÚáéíóúÑñ])', titulo_raw + ' ' + texto[:200])
        titulo = 'Mucho más · semana ' + m.group(1).upper() if m else 'Mucho más'
    elif sec == 'web' and not titulo:
        m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', cuerpo, re.S)
        titulo = txt(m.group(1)).strip() if m else titulo
    elif sec == 'extra':
        titulo = 'EXTRA! nº ' + str(1 + sum(1 for q in IDX['posts'] if q['s'] == 'x' and q['d'] < fecha))
    # medios: líneas de fuente en negrita, campos «Medio:» y etiquetas
    fuentes = []
    lineas_fuente = []
    for para in re.findall(r'<(?:p|li)>(.*?)</(?:p|li)>', cuerpo, re.S):
        if re.search(DATE_PAT, txt(para).lower()) and BOLD_RE.search(para):
            fuentes += [txt(b).strip(' »,.:') for _, b in BOLD_RE.findall(para)]
            lineas_fuente.append(txt(para))
    fuentes += [b for _, b in items] + tags
    medios = sorted({m for m in (medio_de(f, fecha, tags) for f in fuentes) if m})
    for f in fuentes[:len(fuentes) - len(tags)]:
        if f and not medio_de(f, fecha, tags) and len(f) < 60 and re.search(r'[A-Za-zÀ-ÿ]{3}', f) \
                and nz(f) not in MESES and not re.match(r'(?i)(ver|leer|extra|mucho|the$|el$|la$)', f.strip()):
            PEND['medios'].setdefault(f, []).append(p['post_url'])
    # autores: campos «Autor:» (se aceptan nombres nuevos) y nombres ya conocidos en el texto
    autores = set()
    for para in re.findall(r'<(?:p|li)>(.*?)</(?:p|li)>', cuerpo, re.S):
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
    temas |= {n for n in TEM if nz(n) in {nz(t) for t in tl}}
    tipos = [c for c, rx in TIPO_TAG if any(re.search(rx, t) for t in tl)]
    # tipo indicado a mano en cada pieza de mucho más y EXTRA!: «Tipo: cartografía»
    for w in re.findall(r'\bTipo\s*:\s*([A-Za-zÀ-ÿ ]+)', txt(cuerpo)) + tipos_pz:
        w = w.strip().lower()
        for c, rx in TIPO_TAG:
            if re.search(rx.replace('$', ''), w) and c not in tipos:
                tipos.append(c)
                break
    th = next((im for im in ims if not im['cover']), ims[0] if ims else None)
    # piezas de mucho más y EXTRA!: imagen, tipo, medios, autores y etiquetas de cada trabajo (para las fichas y los especiales)
    piezas = []
    if sec in ('muchomas', 'extra'):
        por_url = {im['url']: im for im in ims}
        ult = None
        for mt_ in re.finditer(r'<img\b[^>]*>|<p>(.*?)</p>', cuerpo, re.S):
            if mt_.group(0).startswith('<img'):
                u = attr(mt_.group(0), 'src')
                if u in por_url and not por_url[u].get('cover'):
                    ult = ult or por_url[u]
                continue
            para = mt_.group(1)
            pt = txt(para)
            if not re.search(r'Trabajo\s*:', pt):
                continue
            segs = [x.strip(' .') for x in pt.split('Trabajo', 1)[0].split('|')]
            segs = [x for x in segs if x and ':' not in x and len(x) < 120]
            tp = ''
            if segs:
                for c, rx in TIPO_TAG:
                    if re.search(rx.replace('$', ''), segs[0].lower()):
                        tp = c; break
            et = [e.strip().lower() for e in segs[1].split(',') if e.strip()] if len(segs) > 1 else []
            pm = sorted({MED.index(m) for m in (medio_de(txt(b).strip(' »,.:'), fecha, []) for _, b in BOLD_RE.findall(para)) if m in MED})
            pa = set()
            for m in AUTOR_RE.finditer(pt):
                for n in nombres(m.group(1)):
                    a_ = ALIAS['autores'].get(nz(n))
                    if a_ in AUT and a_ not in NO_AUTORES:
                        pa.add(AUT.index(a_))
            mt_t = re.search(r'Trabajo\s*:\s*(.*?)\s*(?:\||$)', pt)
            tit = mt_t.group(1).strip(' «»"\'“”.') if mt_t else ''
            piezas.append([miniatura(ult, 640) if ult else '', tp, pm, sorted(pa), et, fecha_trabajo(pt.split('Trabajo', 1)[-1], fecha), tit])
            ult = None
    # EXTRA! con la lista «[n] texto<br>tipo | etiquetas | Autor: … | Medio, del 24 de septiembre»: una pieza por imagen, según su número
    if sec == 'extra' and not piezas:
        vis = [im for im in ims if not im.get('cover')] or ims
        for li in re.findall(r'<li>(.*?)</li>', cuerpo, re.S):
            mn = re.match(r'\s*\[(\d+)(?:\s*[-–]\s*(\d+))?\]', txt(li))
            partes = re.split(r'<br\s*/?>', li)
            if not mn or len(partes) < 2 or '|' not in partes[-1]:
                continue
            F = [txt(f).strip() for f in partes[-1].split('|')]
            tp, et, au, md, fe = '', [], '', '', ''
            for k, f in enumerate(F):
                mf = re.match(r'(.*?),?\s+del?\s+(\d{1,2}\s+de\s+\w+(?:\s+de\s+\d{4})?)\s*$', f)
                if mf:
                    md, fe = mf.group(1).strip(), mf.group(2)
                elif re.match(r'Autor(?:a|es|as)?\s*:', f):
                    au = f.split(':', 1)[1]
                elif k == 0:
                    tp = next((c for c, rx in TIPO_TAG if re.search(rx.replace('$', ''), f.lower())), '') or TIPO_N.get(nz(f.split(',')[0]), '')
                elif ':' not in f and len(f) < 120:
                    et += [e.strip().lower() for e in f.split(',') if e.strip()]
            m_ = medio_de(md, fecha, []) if md else None
            pa = set()
            for n in nombres(au):
                a_ = ALIAS['autores'].get(nz(n))
                if a_ in AUT and a_ not in NO_AUTORES:
                    pa.add(AUT.index(a_))
            a0, a1 = int(mn.group(1)), int(mn.group(2) or mn.group(1))
            for k in range(a0, a1 + 1):
                im = vis[k - 1] if 0 < k <= len(vis) else None
                piezas.append([miniatura(im, 640) if im else '', tp, [MED.index(m_)] if m_ in MED else [], sorted(pa), et, fecha_trabajo('del ' + fe, fecha) if fe else ''])
    # posts normales con trabajos de varios medios: cada imagen es una pieza con su medio y sus autores. Sale del pie de la imagen
    # puesto en el panel («Medio (Autor y Autor)») o, si no lo hay, de la lista de trabajos «Medio, del … | Autor: …» en el mismo orden
    if sec not in ('muchomas', 'extra', 'web') and len(medios) > 1:
        vis = [im for im in ims if not im.get('cover')] or ims
        pies = {int(k): v for k, v in ((AJ.get(str(p['id'])) or {}).get('pies') or {}).items() if str(k).isdigit() and v}
        lis = re.findall(r'<li>(.*?)</li>', cuerpo, re.S)
        lis = [l for l in lis if BOLD_RE.search(l) and (re.search(DATE_PAT, txt(l).lower()) or '|' in l)]
        # fecha común («» Todos los trabajos se han publicado el 4 de noviembre de 2026»)
        fecha_comun = ' '.join(txt(x) for x in re.findall(r'<p>(.*?)</p>', cuerpo, re.S) if txt(x).lstrip().startswith('»') and not BOLD_RE.search(x))
        def pieza_de(md_txt, au_txt, fe_txt, im, tp=''):
            md = medio_de(md_txt.strip(' »,.:'), fecha, [])
            fe_txt = fe_txt if fecha_trabajo(fe_txt, fecha) else fecha_comun
            pa = set()
            for n in nombres(au_txt or ''):
                a_ = ALIAS['autores'].get(nz(n))
                if a_ in AUT and a_ not in NO_AUTORES:
                    pa.add(AUT.index(a_))
            return [miniatura(im, 640) if im else '', tp or (tipos[0] if tipos else ''), [MED.index(md)] if md in MED else [], sorted(pa), [], fecha_trabajo(fe_txt, fecha)]
        fecha_li, tipo_li = {}, {}
        for l in lis:
            b = BOLD_RE.findall(l)
            m_ = medio_de(txt(b[0][1]).strip(' »,.:'), fecha, []) if b else None
            if m_:
                fecha_li[m_] = ' '.join(f for f in txt(l).split('|') if re.search(DATE_PAT, f.lower()))
                tipo_li[m_] = TIPO_N.get(nz(txt(l).split('|')[0]), '') if '|' in txt(l) else ''
        if pies:
            for k, im in enumerate(vis, 1):
                pie = pies.get(k)
                if not pie:
                    continue
                mt = re.match(r'\s*([^()]+?)\s*(?:\((.*)\))?\s*$', pie)
                if mt:
                    md = medio_de(mt.group(1), fecha, [])
                    piezas.append(pieza_de(mt.group(1), mt.group(2), fecha_li.get(md, ''), im, tipo_li.get(md, '')))
        elif lis and len(lis) == len(vis):
            for l, im in zip(lis, vis):
                t_ = txt(l); b = BOLD_RE.findall(l); F = t_.split('|')
                au = ', '.join(f.split(':', 1)[1] for f in F if re.match(r'\s*Autor', f) and ':' in f)
                fe = ' '.join(f for f in F if re.search(DATE_PAT, f.lower()))
                tp = TIPO_N.get(nz(F[0]), '') if len(F) > 1 else ''
                piezas.append(pieza_de(txt(b[0][1]) if b else t_.split(',')[0], au, fe, im, tp))
        piezas = [z for z in piezas if z[2]]
    # fecha del trabajo (la del cuadro negro); en mucho más y EXTRA!, la de la pieza más reciente
    ftr = max([z[5] for z in piezas if z[5]] or ['']) if piezas else ''
    ftr = ftr or fecha_trabajo(' '.join(lineas_fuente), fecha)
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
        **({'f': ftr} if ftr and ftr != fecha else {}),
        '_res': resumen(texto),
        '_im2': miniatura(th, 640) if th else '',
        '_pz': piezas or None,
        '_tags': tl,
        '_fr': [[miniatura(im, 640), (items[k][1] if k < len(items) else '')] for k, im in enumerate([im for im in ims if not im['cover']][:40])] if sec in ('muchomas', 'extra') else None,
    }
    if sec == 'web':
        # especial web: enlace, imagen principal a tamaño grande (un GIF sigue animado) y el resto para la tira, con los pies del panel
        pies = (AJ.get(str(p['id'])) or {}).get('pies') or {}
        nw = npf_web(p['id'])
        lk = p.get('url') or nw.get('lk') or next((h for h in re.findall(r'href="([^"]+)"', cuerpo) if 'tumblr.com' not in h), '')
        lk = (AJ.get(str(p['id'])) or {}).get('enlace') or lk
        bt = (AJ.get(str(p['id'])) or {}).get('texto') or ' '.join(nw.get('tx') or []).strip() or texto
        if bt and titulo_raw == '' and bt.startswith(titulo):
            bt = bt[len(titulo):].strip()
        post['_web'] = {'lk': lk, 'g': ims[0]['url'] if ims else '', 'b': bt[:400],
                        'fr': [[miniatura(im, 640), str(pies.get(str(k + 2), ''))] for k, im in enumerate(ims[1:12])]}
    return post

# ---------------------------------------------------------------- actualización
def main():
    if os.environ.get('ETIQUETAS_TODAS'):
        # una pasada por todo el archivo solo para guardar las etiquetas originales (no reclasifica nada)
        for p in api_posts():
            ETQ[str(p['id'])] = p.get('tags', [])
        print('Etiquetas leídas:', len(ETQ))
    existentes = {p['i']: p for p in IDX['posts']}
    nuevos, releidos = 0, 0
    vistos = 0
    leidos = set()
    def mas_ajustados():
        # los posts con etiquetas cambiadas desde el panel se releen siempre, aunque sean antiguos
        for pid in AJ:
            if pid not in leidos and pid in existentes and (AJ[pid].get('mas') or AJ[pid].get('menos')):
                q = api_post(pid)
                if q:
                    yield q
    def todos():
        nonlocal vistos
        for p in api_posts():
            vistos += 1
            if os.environ.get('DEPURA') == 'ultimos' and vistos <= 5:
                print('ULTIMO', p['id'], p.get('date'), p.get('state'), p.get('type'), p.get('tags'))
            if str(p['id']) in existentes and vistos > RELEER:
                break
            yield p
        yield from mas_ajustados()
    for p in todos():
        pid = str(p['id'])
        leidos.add(pid)
        if p.get('state', 'published') != 'published':
            continue
        q = clasificar(p)
        if q is None:
            existentes.pop(pid, None); continue
        if pid in existentes:
            releidos += 1
            # lo ya revisado a mano se conserva: se suma a lo detectado ahora, nunca se pierde
            old = existentes[pid]
            aj = AJ.get(pid) or {}
            for key in (('a', 'm') if (aj.get('mas') or aj.get('menos')) else ('a', 'm', 'h', 'k')):
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
        quitados = {pid for pid, aj in AJ.items() if ks & {nz(t).replace(' ', '') for t in aj.get('menos', [])}}
        e['posts'] = [i for i in e['posts'] if i not in quitados]
        for q in posts:
            if '_tags' in q and ks & {nz(t).replace(' ', '') for t in q['_tags']} and q['i'] not in e['posts']:
                e['posts'].append(q['i'])
        fechas = sorted(q['d'] for q in posts if q['i'] in set(e['posts']))
        if fechas:
            e['desde'], e['hasta'] = fechas[0], fechas[-1]
    frames = {q['i']: q.pop('_fr') for q in posts if q.get('_fr')}
    webs = {q['i']: q.pop('_web') for q in posts if q.get('_web')}
    RES.update({q['i']: q.pop('_res') for q in posts if q.get('_res')})
    IM2.update({q['i']: q.pop('_im2') for q in posts if q.get('_im2')})
    for q in posts: q.pop('_im2', None)
    PZ.update({q['i']: q.pop('_pz') for q in posts if q.get('_pz')})
    for q in posts:
        q.pop('_tags', None); q.pop('_fr', None); q.pop('_res', None); q.pop('_pz', None)
    aplicar_estructura(posts)
    recontar(posts)
    IDX['posts'] = posts
    json.dump(IDX, open(D('indice.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    json.dump(ESP, open(D('especiales.json'), 'w'), ensure_ascii=False, indent=0)
    estadisticas(posts)
    escribir_meta(IDX)
    escribir_portada(IDX, frames, webs)
    for k in PEND:
        for n in PEND[k]:
            PEND[k][n] = sorted(set(PEND[k][n]))
    json.dump(PEND, open(D('pendientes.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(ETQ, open(D('etiquetas.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
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
                y = int((q.get('f') or q['d'])[:4]); lo, hi = ys.get(i, (y, y)); ys[i] = (min(lo, y), max(hi, y))
        for i, it in enumerate(cat):
            it['p'] = c.get(i, 0)
            if 'y' in it and i in ys:
                it['y'] = list(ys[i])

CDN = 'https://cdn.jsdelivr.net/gh/inconsolataweb/inconsolata-datos@main/'
def escribir_meta(idx):
    global ESP_DE_TEMA
    ESP_DE_TEMA = {e['de_tema']: e['slug'] for e in ESP if e.get('de_tema')}
    """Archivos ligeros para el tema: qué medio, autores, temas y tipo tiene cada post, y el catálogo de nombres."""
    # especial de cada post (el más concreto: un capítulo gana a su especial madre)
    ESP_POST = {}
    for e in sorted(ESP, key=lambda e: (bool(e.get('cap_de')), -len(e['posts']))):
        for i in e['posts']:
            ESP_POST[i] = e['slug']
    meta = {q['i']: [q['s'], q['k'], q['m'], q['a'], q['h']] + ([ESP_POST[q['i']]] if q['i'] in ESP_POST else []) for q in idx['posts']}
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
           'esp': {e['slug']: e['titulo'] for e in ESP},
           'espi': iconos_especiales(),
           # etiquetas de cada especial (para reconocer las piezas sueltas de los mucho más/EXTRA!): {slug: [tema, etiqueta, …]}
           'espt': {e['slug']: [e.get('padre') or e.get('tema', '')] + [nz(t) for t in e.get('tags', [])] for e in ESP if e.get('tags')},
           'temas': [dict({'n': t['n'], 'b': t['b']}, **({'x': t['x']} if t.get('x') else {}), **({'e': ESP_DE_TEMA[t['n']]} if t['n'] in ESP_DE_TEMA else {})) for t in idx['temas']]}
    json.dump(cat, open(D('catalogo.json'), 'w'), ensure_ascii=False, separators=(',', ':'))

def iconos_especiales():
    """Iconos propios de los especiales (datos/especiales_iconos.json, desde el panel): {slug: [icono, texto]}.
    Los capítulos sin icono propio heredan el del especial del que forman parte."""
    try:
        EI = json.load(open(D('especiales_iconos.json')))
    except (FileNotFoundError, ValueError):
        EI = {}
    by = {e['slug']: e for e in ESP}
    out = {}
    for e in ESP:
        x, vistos = e, set()
        while x and x['slug'] not in EI and x.get('cap_de') and x['slug'] not in vistos:
            vistos.add(x['slug']); x = by.get(x['cap_de'])
        o = EI.get(x['slug']) if x else None
        if o and o.get('i'):
            out[e['slug']] = [o['i'], str(o.get('t', ''))[:6]]
    return out

RES = {}
IM2 = {}   # miniatura más grande (640 px) para la versión móvil de la portada
PZ = {}
def escribir_portada(idx, frames, webs=None):
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
    viejos = {r[0]: r[6] for r in (old.get('rec') or []) + (old.get('man') or [])}
    viejos2 = {r[0]: r[9] for r in (old.get('rec') or []) + (old.get('man') or []) if len(r) > 9}
    def corto(q):
        return [q['i'], q['u'], q['d'], q['s'], q['k'], titulo(q), RES.get(q['i']) or viejos.get(q['i']) or q['b'], [MN[i] for i in q['m'][:3]], q['im'], IM2.get(q['i']) or viejos2.get(q['i']) or q['im']]
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
    # especial web (etiqueta «especial web»): el más reciente, con su enlace, su GIF y la tira
    q = next((q for q in posts if q['s'] == 'w'), None)
    if q:
        wb = (webs or {}).get(q['i']) or ((old.get('w') or {}) if (old.get('w') or {}).get('i') == q['i'] else {})
        out['w'] = {'i': q['i'], 'u': q['u'], 'd': q['d'], 't': titulo(q), 'b': wb.get('b') or q['b'], 'lk': wb.get('lk', ''),
                    'g': wb.get('g') or q['im'], 'fr': wb.get('fr', [])}
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
    cy = Counter(i for q in posts if (q.get('f') or q['d']).startswith(y) for i in q['m'])
    ct = Counter(i for q in posts for i in q['m'])
    # entradillas escritas a mano en el panel (Posts › Entradilla del destacado)
    out['ent'] = {k: v['entradilla'].strip() for k, v in AJ.items() if isinstance(v, dict) and str(v.get('entradilla') or '').strip()}
    out['med'] = {'y': y, 'posts': sum(1 for q in posts if (q.get('f') or q['d']).startswith(y)),
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
    try:
        viejo = {q['i']: q['pz'] for q in json.load(open(D('archivo.json')))['posts'] if q.get('pz')}
    except Exception:
        viejo = {}
    def con_pz(q):
        o = {k: v for k, v in q.items() if k not in ('x', 'b', 'r')}
        pz = PZ.get(q['i']) or viejo.get(q['i'])
        if pz:
            o['pz'] = pz
        return o
    arch = {'posts': [con_pz(q) for q in posts],
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
    # cuenta la fecha del trabajo (la del cuadro negro), no la de publicación
    fd = lambda p: p.get('f') or p['d']
    M, A, T = MED, AUT, TEM
    global MEDIO_AUT     # medio principal de cada autor, para poner su avatar junto al nombre
    MEDIO_AUT = {i: M.index(a['m'][0]) for i, a in enumerate(IDX['autores']) if a.get('m') and a['m'][0] in M}
    first = {}
    for p in sorted(P, key=fd):
        for i in p['m']:
            first.setdefault(i, int(fd(p)[:4]))
    def block(ps, year=None):
        cm, ca, ck, ct = Counter(), Counter(), Counter(), Counter()
        for p in ps:
            cm.update(p['m']); ca.update(p['a']); ck.update(p['k']); ct.update(p['h'])
        out = {'posts': len(ps), 'n_medios': len(cm), 'n_autores': len(ca),
               'medios': [[M[i], c, i] for i, c in cm.most_common(25)], 'autores': [[A[i], c, i, MEDIO_AUT.get(i)] for i, c in ca.most_common(15)],
               'tipos': dict(ck), 'temas': [[T[i], c, i] for i, c in ct.most_common(24)], 'imgs': sum(p['n'] for p in ps)}
        if year:
            out['meses'] = [sum(1 for p in ps if fd(p)[5:7] == '%02d' % m) for m in range(1, 13)]
            out['nuevos'] = sorted([[M[i], cm[i], i] for i in cm if first[i] == year], key=lambda x: -x[1])[:16]
        return out
    y1 = datetime.now(timezone.utc).year
    years = {y: block([p for p in P if fd(p).startswith(str(y))], y) for y in range(2011, y1 + 1)}
    total = block(P)
    pres = Counter()
    for i in range(len(M)):
        pres[i] = len({fd(p)[:4] for p in P if i in p['m']})
    total['fieles'] = [[M[i], c, i] for i, c in pres.most_common(12)]
    total['per_year'] = {y: years[y]['posts'] for y in years}
    total['medios_year'] = {y: years[y]['n_medios'] for y in years}
    json.dump({'total': total, 'years': years}, open(D('estadisticas.json'), 'w'), ensure_ascii=False)

if __name__ == '__main__':
    main()
