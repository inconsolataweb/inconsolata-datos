"""Primera selección de hitos para la cronología (datos/cronologia.json).

Se ejecuta una vez para proponer la lista; después se edita a mano o desde el panel.
  · coberturas: todos los especiales (los largos se dibujan como «grandes historias»)
  · noticias: los días de gran noticia, en los que comparamos muchas portadas
  · piezas: los trabajos más ricos de cada año (imágenes y firmas), uno por trimestre
  · la web: nacimiento del blog y de sus secciones
"""
import json, os, statistics
from collections import Counter, defaultdict

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
A = json.load(open(os.path.join(D, 'archivo.json')))
CAT = json.load(open(os.path.join(D, 'catalogo.json')))
ESP = json.load(open(os.path.join(D, 'especiales.json')))
P = sorted(A['posts'], key=lambda p: p['d'])
TEMAS = [t['n'] for t in A['temas']]
BLOQUE = {t['n']: t.get('b') for t in CAT['temas']}
OCULTO = {t['n'] for t in CAT['temas'] if t.get('x') == 'oculto'}

hitos, usados = [], set()

# la web
def primero(f):
    return next((p for p in P if f(p)), None)
for p, t in ((P[0], 'Nace inconsolata»'), (primero(lambda p: p['s'] == 'm'), 'Primer «mucho más»'),
             (primero(lambda p: p['s'] == 'x'), 'Primer EXTRA!'), (primero(lambda p: p['s'] == 'b'), 'Primer post del metablog')):
    if p:
        hitos.append({'id': p['i'], 'tipo': 'web', 't': t}); usados.add(p['i'])

# coberturas: todos los especiales (capítulos incluidos)
for e in ESP:
    if len(e['posts']) >= 2 and e['tema'] not in OCULTO:
        hitos.append({'esp': e['slug']})

# ventanas ya cubiertas por un especial, por tema
cubierto = defaultdict(list)
for e in ESP:
    for t in {e['tema'], e.get('padre')} - {None}:
        cubierto[t].append((e['desde'][:7], e['hasta'][:7]))

# noticias de impacto: los días en que comparamos muchas portadas (muchos medios en un post)
TIT = json.load(open(os.path.join(D, 'titulos.json')))
def titulo(p):
    return TIT.get(p['i']) or p['t'] or ''
en_esp = {i for e in ESP for i in e['posts']}
ACT = {i for i, t in enumerate(TEMAS) if BLOQUE.get(t) in ('Actualidad', 'Deportes') or t == 'Titulares'}
por_y = defaultdict(list)
for p in P:
    if p['s'] == '' and p['i'] not in usados and p['i'] not in en_esp and len(p['m']) >= 5 and set(p['h']) & ACT:
        por_y[p['d'][:4]].append(p)
for y, L in por_y.items():
    for p in sorted(L, key=lambda p: (-len(p['m']), -p['n']))[:4]:
        usados.add(p['i'])
        hitos.append({'id': p['i'], 'tipo': 'noticia'})

# piezas: los trabajos más ricos de cada año (imágenes y firmas), uno por trimestre como mucho
import re
RECOP = re.compile(r'portadillas|mucho m[aá]s|extra!|semana|resumen|repaso', re.I)
por_y = defaultdict(list)
for p in P:
    if p['s'] in ('', 'b', 'o', 'd') and p['i'] not in usados and p['i'] not in en_esp and not RECOP.search(titulo(p)):
        por_y[p['d'][:4]].append(p)
for y, L in por_y.items():
    trim = set()
    for p in sorted(L, key=lambda p: (-(min(p['n'], 12) + 2.5 * len(p['a']) + len(p['k'])), p['d'])):
        q = (int(p['d'][5:7]) - 1) // 3
        if q in trim:
            continue
        trim.add(q); usados.add(p['i'])
        hitos.append({'id': p['i'], 'tipo': 'pieza'})
        if len(trim) == 4:
            break

fecha = {p['i']: p['d'] for p in P}
efecha = {e['slug']: e['desde'] for e in ESP}
hitos.sort(key=lambda h: h.get('d') or fecha.get(h.get('id')) or efecha.get(h.get('esp')) or '')

def linea(o):
    return '{' + ', '.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False) for k, v in o.items()) + '}'
open(os.path.join(D, 'cronologia.json'), 'w').write('{\n"hitos": [\n' + ',\n'.join(' ' + linea(h) for h in hitos) + '\n]\n}\n')
print(Counter(h.get('tipo', 'cobertura') for h in hitos))
