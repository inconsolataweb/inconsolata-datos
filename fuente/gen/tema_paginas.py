"""Páginas propias del tema (buscador, medios, autores, estadísticas, especiales, novedades).
En Tumblr son páginas normales (/buscador, /medios…) con el contenido vacío: el tema detecta la dirección y las monta
con los datos del repositorio. Estilos tomados de las maquetas y encerrados en .v-<página>."""
import os, re
from tema_vistas import ambito
D = os.path.dirname(os.path.abspath(__file__))

def _str(fichero, nombre):
    s = open(os.path.join(D, fichero)).read()
    return re.search(nombre + r' = r?"""(.*?)"""', s, re.S).group(1)

def _sin_pie(css):
    return re.sub(r'^(footer|\.cmyk-bar|\.foot)\b[^\n]*\n', '', css, flags=re.M)

# ---------------- buscador
_bcss = _sin_pie(_str('buscador.py', 'BCSS'))
_bcss = re.sub(r'\.body\b', '.bbody', _bcss)
BUS_CSS = ambito(_bcss, '.v-buscador')
_bjs = _str('buscador.py', 'JS')
_R = [
    ("var D = __DATA__, TN = __TIPOS__, TS = __TS__;\n", ''),
    ("var P = D.posts, Y0 = 2011, Y1 = 2026;", "var P = D.posts, Y0 = 2011, Y1 = new Date().getFullYear();"),
    ("else if (st[k]) st[k] = v.split('|').map(function (x) { return /^[amhy]$/.test(k) ? +x : x; });",
     "else if (st[k]) st[k] = v.split('|').map(function (x) { if (/^[amh]$/.test(k) && isNaN(+x)) { var arr = k === 'a' ? D.autores : k === 'm' ? D.medios : D.temas, f = nz(x); return arr.findIndex(function (o) { return nz(o.n) === f; }); } return /^[amhy]$/.test(k) ? +x : x; }).filter(function (x) { return x !== -1; });"),
    ("'<a class=\"rc\" href=\"https://inconsolata.com/post/' + esc(p.u) + '\" target=\"_blank\" rel=\"noopener\">", "'<a class=\"rc\" href=\"/post/' + esc(p.u) + '\">"),
    ("'<div class=\"rel\">' + relBtns('h', topRel(all, 'h', -1, 5)) + '</div><a class=\"go\" href=\"#\">Ver ficha completa »</a></div>';",
     "'<div class=\"rel\">' + relBtns('h', topRel(all, 'h', -1, 5)) + '</div><a class=\"go\" href=\"/autores#' + encodeURIComponent(a.n) + '\">Ver ficha completa »</a></div>';"),
    ("'<p>Autores más presentes:</p><div class=\"rel\">' + relBtns('a', topRel(all, 'a', -1, 6)) + '</div><a class=\"go\" href=\"#\">Ver ficha completa »</a></div>';",
     "'<p>Autores más presentes:</p><div class=\"rel\">' + relBtns('a', topRel(all, 'a', -1, 6)) + '</div><a class=\"go\" href=\"' + fichaN(m.n) + '\">Ver ficha completa »</a></div>';"),
    ("""[].forEach.call(document.querySelectorAll('.srch'), function (f) {
  f.addEventListener('submit', function () { var v = f.querySelector('input').value.trim(); if (v) { q.value = v; st.q = v; run(); scrollTo(0, 0); } });
});""", """addEventListener('hashchange', function () { st = {q: '', k: [], s: [], y: [], m: [], a: [], h: [], o: 'new'}; readHash(); q.value = st.q; run(); scrollTo(0, 0); });"""),
]
_R += [("var head = p.t || p.b || 'Entrada sin texto';", "var head = quita(TIT[p.i] || '') || p.t || p.b || 'Entrada sin texto';"),
       ("  p.hay = ' ' + p.x + ' ' +", "  p.hay = ' ' + p.x + ' ' + (TIT[p.i] ? nz(quita(TIT[p.i])) + ' ' : '') +")]
for a, b in _R:
    assert a in _bjs, a[:60]
    _bjs = _bjs.replace(a, b)
BUS_JS = _bjs
_TRY = [('a', 'Josemi Benítez'), ('h', 'Guerra en Ucrania'), ('m', 'Le Monde'), ('q', 'mapa del metro'), ('a', 'Francesca Fattori'),
        ('h', 'Juegos Olímpicos'), ('m', 'La Voz de Galicia'), ('q', 'tipografía')]
BUS_HTML = ('<section class="hero"><div class="wrap"><h1 class="soft">Quince años de <em>periodismo visual</em>, a un clic</h1><div class="qbox"><div class="qrow">'
            '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2.6" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'
            '<label for="q" class="sr">Buscar en el archivo de inconsolata»</label><input id="q" type="search" placeholder="Autor, medio, tema o lo que recuerdes…" autocomplete="off" role="combobox" aria-expanded="false" aria-controls="sug" aria-autocomplete="list">'
            '<button type="button" id="qclear" aria-label="Borrar búsqueda">×</button></div><div class="sug" id="sug" role="listbox" hidden></div></div>'
            '<div class="try" id="try"><span class="caps" style="margin-right:4px">Prueba »</span>' + ''.join(f'<a href="#" data-t="{k}" data-v="{v}">{v}</a>' for k, v in _TRY) + '</div></div></section>'
            '<div class="wrap bbody"><aside class="facets" id="facets" aria-label="Filtros">'
            '<div class="fg"><h2>Años</h2><div class="years" id="f-y"></div><div class="yl"><span>2011</span><span class="y-now"></span></div></div>'
            '<div class="fg"><h2>Tipo de pieza</h2><div class="fl" id="f-k"></div></div><div class="fg"><h2>Temas</h2><div class="fl" id="f-h"></div></div>'
            '<div class="fg"><h2>Medios</h2><div class="fl" id="f-m"></div></div><div class="fg"><h2>Autores</h2><div class="fl" id="f-a"></div></div></aside>'
            '<section aria-live="polite"><div class="rhead"><div class="count" id="count"></div><div style="display:flex;gap:10px;align-items:center">'
            '<button type="button" class="ftoggle" id="ftoggle" aria-expanded="false" aria-controls="facets">Filtros</button><label class="sr" for="sort">Ordenar</label>'
            '<select id="sort"><option value="new">Más recientes</option><option value="old">Más antiguas</option><option value="rel">Más relevantes</option></select></div></div>'
            '<div class="active" id="active"></div><div class="fx" id="ficha" hidden></div><div class="grid" id="grid"></div>'
            '<button type="button" class="loadmore" id="more">Cargar más »</button></section></div>')

# ---------------- estadísticas
EST_CSS = ambito(_sin_pie(_str('estadisticas.py', 'SCSS')) + '.hb a{display:flex;align-items:center;gap:8px}.hb .hav{width:22px;height:22px;object-fit:contain;flex-shrink:0}', '.v-estadisticas')
_ejs = _str('estadisticas.py', 'JS')
_R = [
    ("var ST = __ST__, TN = __TN__, Y = 'all';", "var Y = 'all', Y1 = new Date().getFullYear();"),
    ("var BUS = 'inconsolata-buscador.html#';", "var BUS = '/buscador#';"),
    ("'\">' + esc(r[0]) + '</a><div class=\"tr\">", "'\">' + avh(key, r) + esc(r[0]) + '</a><div class=\"tr\">"),
    ("function hbars(id, rows, key) {", "function avh(key, r) { var i = key === 'm' ? r[2] : key === 'a' ? r[3] : null, c = i != null && cat0 && cat0.medios[i]; return key === 'm' || key === 'a' ? (c && c.av ? '<img class=\"hav\" src=\"' + esc(c.av) + '\" alt=\"\">' : '<span class=\"hav\"></span>') : ''; }\nfunction hbars(id, rows, key) {"),
    ("for (var y = 2026; y >= 2011; y--)", "for (var y = Y1; y >= 2011; y--)"),
    ("'en 15 años de archivo' : 'en ' + Y + (Y === 2026 ? ' (hasta hoy)' : '')", "'en ' + (Y1 - 2011) + ' años de archivo' : 'en ' + Y + (Y === Y1 ? ' (hasta hoy)' : '')"),
]
for a, b in _R:
    assert a in _ejs, a[:60]
    _ejs = _ejs.replace(a, b)
EST_JS = _ejs
EST_HTML = ('<section class="wrap hero"><div class="crumbs caps" style="padding:0 0 14px"><a href="/">Portada</a><i>»</i><a href="/medios">Medios</a><i>»</i><span>Estadísticas</span></div>'
            '<h1 class="soft">Los <em>números</em> del archivo</h1><p>Qué medios, autores y temas han pasado por inconsolata» cada año desde 2011. Pulsa un año para ver solo ese año.</p></section>'
            '<nav class="ybar" aria-label="Elegir año"><div class="wrap in" id="ybar"></div></nav><section class="kpis" aria-live="polite"><div class="wrap in" id="kpis"></div></section>'
            '<div class="wrap"><section class="blk"><h2 class="soft">Entradas <em>por año</em><small>pulsa una barra</small></h2><div class="vbars" id="vb"></div><div class="vax" id="vax"></div></section>'
            '<div class="cols"><section class="blk"><h2 class="soft">Medios <em>más presentes</em><small class="ylbl"></small></h2><div class="hb" id="hm"></div>'
            '<p class="note">Número de entradas en las que aparece el medio. Un «mucho más» o un EXTRA! cuenta una vez por cada medio que incluye.</p></section>'
            '<section class="blk"><h2 class="soft">Autores <em>más citados</em><small class="ylbl"></small></h2><div class="hb" id="ha"></div></section></div>'
            '<section class="blk"><h2 class="soft">Tipos <em>de pieza</em><small class="ylbl"></small></h2><div class="tipos-row" id="tp"></div>'
            '<p class="note">Gráfico y Online solo se cuentan en los posts publicados con el nuevo diseño.</p></section>'
            '<div class="cols"><section class="blk"><h2 class="soft">Temas<small class="ylbl"></small></h2><div class="hb" id="ht"></div></section>'
            '<section class="blk" id="nv"><h2 class="soft">Se <em>estrenan</em><small>medios que aparecen por primera vez</small></h2><div class="chips" id="nvc"></div></section>'
            '<section class="blk" id="fi"><h2 class="soft">Los <em>fieles</em><small>medios presentes más años</small></h2><div class="chips" id="fic"></div></section></div></div>'
            '<div id="tip" role="presentation"></div>')

# ---------------- fichas de medio y autor
_fcss = _str('fichas.py', 'FCSS')
FICHA_CSS = ambito(_fcss + """
.idx-top{padding:20px 0 30px;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px 30px}
.idx-top h1{margin:0;font-size:clamp(64px,9vw,140px);line-height:.88;letter-spacing:-.03em}
.idx-top h1 em{color:var(--accent)}
.idx-top p{margin:10px 0 0;font-family:'Fraunces',serif;font-style:italic;font-size:21px;max-width:640px}
.idx-tools{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.idx-tools input{min-height:48px;border:3px solid var(--ink);background:#fff;font-family:'Fraunces',serif;font-style:italic;font-size:20px;padding:0 14px;width:min(360px,100%);box-shadow:5px 5px 0 var(--ink)}
.idx-tools select{min-height:48px;border:2px solid var(--ink);background:#fff;font:inherit;font-weight:700;padding:0 10px}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;padding:10px 0 90px}
.mdc{display:grid;grid-template-columns:56px minmax(0,1fr);grid-template-rows:auto auto;column-gap:12px;align-items:center;background:#fff;border:2px solid var(--ink);padding:10px;min-height:78px;transition:transform .15s,box-shadow .15s}
.mdc:hover{transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--accent);color:var(--ink)}
.mdc-av{grid-row:1/3;width:56px;height:56px;display:flex;align-items:center;justify-content:center}
.mdc-av img{width:100%;height:100%;object-fit:contain;display:block}
.mdc-av.ini{background:var(--yellow);font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:26px}
.mdc-n{font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:17px;line-height:1.1;align-self:end}
.mdc-c{font-size:11px;font-weight:700;color:var(--muted);align-self:start;margin-top:3px}
.mdc-c b{color:var(--accent);font-size:13px}
.mdc.off{background:transparent;border-style:dashed}
.wk-r.cargando{opacity:.5}
.card .tt{font-size:21px}
.card .ph{height:240px}
.finfo h1.autor{font-size:clamp(44px,5.6vw,88px);line-height:.92}
.wk-r{font-size:17px!important;line-height:1.5!important}
.chips a.ch-av{gap:8px}.chips a.ch-av img{width:22px;height:22px;object-fit:contain}
.flinks a{background:transparent}
.vacio{border:3px dashed var(--ink);padding:40px;text-align:center;font-family:'Fraunces',serif;font-style:italic;font-size:22px}
""", '.v-ficha')

# ---------------- especiales
ESP_CSS = ambito(_sin_pie(_str('especial.py', 'ECSS')) + """
.esp-idx{padding:20px 0 90px;display:flex;flex-direction:column;gap:30px}
.idx-top{padding:20px 0 30px}
.idx-top h1{margin:0;font-size:clamp(64px,9vw,140px);line-height:.88;letter-spacing:-.03em}
.idx-top h1 em{color:var(--accent)}
.idx-top p{margin:10px 0 0;font-family:'Fraunces',serif;font-style:italic;font-size:21px;max-width:640px}
.esp-idx h2{margin:0 0 12px;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;border-bottom:2px solid var(--ink);padding-bottom:6px}
.chips a svg{width:22px;height:22px;overflow:visible}
.btn-ink.todos{display:inline-flex;background:var(--ink);color:var(--paper);padding:14px 22px;font-family:'Archivo',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.btn-ink.todos:hover{color:var(--yellow)}
""", '.v-especiales')

NOV_CSS = ambito("""
.nov-top{padding:20px 0 30px}
.nov-top h1{margin:0;font-size:clamp(64px,9vw,140px);line-height:.88;letter-spacing:-.03em}
.nov-top h1 em{color:var(--accent)}
.nov-top p{margin:10px 0 0;font-family:'Fraunces',serif;font-style:italic;font-size:21px;max-width:640px}
.nov-list{list-style:none;margin:0;padding:0 0 90px;max-width:860px}
.nov-list li{display:grid;grid-template-columns:120px 40px minmax(0,1fr);gap:16px;align-items:start;padding:18px 0;border-bottom:1px solid #CFC8B8}
.nov-list .f{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:22px;line-height:1.1;color:var(--accent)}
.nov-list .f small{display:block;font-family:'Archivo',sans-serif;font-style:normal;font-size:11px;font-weight:800;letter-spacing:1.5px;color:var(--muted)}
.nov-list .ic{width:40px;height:40px}
.nov-list .ic svg{width:100%;height:100%;overflow:visible}
.nov-list .ic.bl{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:36px;line-height:1;color:var(--accent);text-align:center}
.nov-list .t{font-size:19px;font-weight:600;line-height:1.35}
.nov-list a.t{border-bottom:2px solid var(--accent)}
@media (max-width:600px){.nov-list li{grid-template-columns:1fr;gap:6px}}
""", '.v-novedades')

PAG_CSS = BUS_CSS + EST_CSS + FICHA_CSS + ESP_CSS + NOV_CSS + """
.es-pagina main.wrap{display:none}
.v-pag [hidden]{display:none!important}
"""
PAG_JS = (open(os.path.join(D, 'tema_paginas.js')).read()
          .replace('__BUS_JS__', BUS_JS).replace('__EST_JS__', EST_JS))
import json as _json
PAG_JS = PAG_JS.replace('__BUS_HTML__', _json.dumps(BUS_HTML, ensure_ascii=False)).replace('__EST_HTML__', _json.dumps(EST_HTML, ensure_ascii=False))
