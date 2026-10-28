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
_R += [("list('f-h', 'h', cnt(base, 'h', function (p) { return p.h; })", "list('f-h', 'h', cnt(base, 'h', function (p) { return p.h.filter(function (v) { return !D.temas[v].x; }); })"),
       ("var head = p.t || p.b || 'Entrada sin texto';", "var head = quita(TIT[p.i] || '') || p.t || p.b || 'Entrada sin texto';"),
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
EST_CSS = ambito(_sin_pie(_str('estadisticas.py', 'SCSS')) + '''.vbars .mb{flex:1;position:relative;background:var(--accent);border-radius:4px 4px 0 0;min-width:0}.vbars .mb .v{position:absolute;bottom:100%;left:50%;transform:translateX(-50%);font-size:13px;font-weight:800;padding-bottom:4px;white-space:nowrap}#vb-h{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}.vb-back{margin-left:auto;align-self:center;font:800 12px Archivo,sans-serif;letter-spacing:1.5px;text-transform:uppercase;border:2px solid var(--ink);background:none;padding:6px 10px;cursor:pointer;color:var(--ink)}.vb-back:hover{background:var(--ink);color:var(--paper)}''' + '.hb a{display:flex;align-items:center;gap:8px}.hb .hav{width:22px;height:22px;object-fit:contain;flex-shrink:0}', '.v-estadisticas')
_ejs = _str('estadisticas.py', 'JS')
_R = [
    ("var ST = __ST__, TN = __TN__, Y = 'all';", "var Y = 'all', Y1 = new Date().getFullYear();"),
    ("var BUS = 'inconsolata-buscador.html#';", "var BUS = '/buscador#';"),
    ("hbars('ht', d.temas.slice(0, 12), 'h');", "hbars('ht', d.temas.filter(function (r) { var t = cat0 && cat0.temas[r[2]]; return !(t && t.x); }).slice(0, 12), 'h');"),
    ("'\">' + esc(r[0]) + '</a><div class=\"tr\">", "'\">' + avh(key, r) + esc(r[0]) + '</a><div class=\"tr\">"),
    ("function hbars(id, rows, key) {", "function avh(key, r) { var i = key === 'm' ? r[2] : key === 'a' ? r[3] : null, c = i != null && cat0 && cat0.medios[i]; return key === 'm' || key === 'a' ? (c && c.av ? '<img class=\"hav\" src=\"' + esc(c.av) + '\" alt=\"\">' : '<span class=\"hav\"></span>') : ''; }\nfunction hbars(id, rows, key) {"),
    ("  var h = '', ax = '', mx = Math.max.apply(null, Object.values(T.per_year));", "  var h = '', ax = '', mx = Math.max.apply(null, Object.values(T.per_year)), MS = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];\n  var vh = document.getElementById('vb-h');\n  if (Y !== 'all' && d.meses) {\n    var mm = Math.max.apply(null, d.meses.concat([1]));\n    d.meses.forEach(function (v, i) { h += '<span class=\"mb\" data-tip=\"' + MS[i] + ' de ' + Y + ': ' + fmt(v) + ' entradas\" style=\"height:' + (v / mm * 100) + '%\"><span class=\"v\">' + v + '</span></span>'; ax += '<span>' + MS[i].slice(0, 3) + '</span>'; });\n    vh.innerHTML = 'Entradas <em>por mes</em><small>' + Y + '</small><button type=\"button\" class=\"vb-back\" data-y=\"all\">« Todos los años</button>';\n    document.getElementById('vb').innerHTML = h; document.getElementById('vax').innerHTML = ax; T = { per_year: {} };\n  } else vh.innerHTML = 'Entradas <em>por año</em><small>pulsa una barra</small>';"),
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
            '<div class="wrap"><section class="blk"><h2 class="soft" id="vb-h">Entradas <em>por año</em><small>pulsa una barra</small></h2><div class="vbars" id="vb"></div><div class="vax" id="vax"></div></section>'
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
.tops{list-style:none;margin:6px 0 0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2px 22px;min-width:min(100%,420px)}
.tops a{display:flex;justify-content:space-between;align-items:baseline;gap:10px;color:var(--paper);font-family:'Fraunces',serif;font-style:italic;font-size:17px;padding:6px 0;border-bottom:1px solid #4A463D}
.tops a:hover{color:var(--yellow)}
.tops small{font-family:'Archivo',sans-serif;font-style:normal;font-size:12px;font-weight:800;color:var(--yellow)}
.nac{display:flex;align-items:center;gap:10px;margin:-4px 0 0;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.nac .flag{width:30px;height:22px}
.wk dl .ancho{grid-column:1/-1}
.prop{list-style:none;margin:4px 0 0;padding:0;display:flex;flex-direction:column;gap:4px}
.prop li{display:flex;align-items:center;gap:10px;position:relative;font-size:15px;font-weight:600}
.prop .pnom{display:inline-flex;align-items:center;gap:8px}
.prop .flag{width:20px;height:15px}
.prop li.nv1{padding-left:26px}.prop li.nv2{padding-left:52px}.prop li.nv3{padding-left:78px}
.prop .rama{position:absolute;top:-6px;width:14px;height:18px;border-left:2px solid var(--muted);border-bottom:2px solid var(--muted)}
.prop li.nv1 .rama{left:8px}.prop li.nv2 .rama{left:34px}.prop li.nv3 .rama{left:60px}
.prop .pct{display:inline-flex;align-items:center;gap:6px}
.prop .pct i{display:block;height:8px;background:var(--accent);min-width:2px;max-width:80px}
.prop .pct{width:130px}.prop .pct i{flex:none}
.prop .pct b{font-size:12px;color:var(--accent)}
.fmt{display:flex;align-items:flex-end;gap:14px;margin-top:8px;flex-wrap:wrap}
.fmt svg{display:block;max-width:100%;height:auto}
.fmt rect{fill:none;stroke:#B9B2A3;stroke-width:1.2;stroke-dasharray:3 3}
.fmt rect.on{fill:var(--yellow);stroke:var(--ink);stroke-width:2;stroke-dasharray:none}
.fmt text{font:800 11px Archivo,sans-serif;fill:var(--ink)}
.fmt small{font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px}
.fmt small b{font-size:13px;color:var(--ink)}
.fmt small i{font-style:normal}.fmt small i.on{color:var(--ink);background:var(--yellow);padding:0 3px}
.coronas{display:flex;flex-wrap:wrap;gap:4px;margin-top:10px;max-width:260px}
.cor:hover::after,.cor:focus::after{content:attr(data-tip);position:absolute;left:0;bottom:calc(100% + 8px);width:max-content;max-width:230px;background:var(--yellow);color:var(--ink);font-family:'Archivo',sans-serif;font-style:normal;font-size:12px;font-weight:700;letter-spacing:0;text-transform:none;line-height:1.35;padding:6px 9px;z-index:5;box-shadow:3px 3px 0 var(--accent);white-space:normal}
.cor{position:relative;width:36px;height:27px;display:inline-block;cursor:help}
.cor svg{position:absolute;inset:0;width:100%;height:100%}
.cor b{position:absolute;left:0;right:0;bottom:3px;text-align:center;font-family:'Archivo',sans-serif;font-style:normal;font-size:8.5px;font-weight:900;color:var(--ink);letter-spacing:0}
.cor.oro svg{fill:#E2B33C}.cor.plata svg{fill:#C9CDD2}.cor.bronce svg{fill:#C27C47}
.cor.prov{animation:parpa 1.4s ease-in-out infinite}
@keyframes parpa{50%{opacity:.35}}
@media (prefers-reduced-motion:reduce){.cor.prov{animation:none;outline:2px dashed var(--yellow)}}
.finfo .ftext{border:0;background:transparent;padding:0;font-size:19px;line-height:1.55;max-width:820px}
.wk{max-width:none!important}
.wk{margin-top:22px}
.fvis{display:flex;flex-direction:column;gap:34px}
.fmt-box:empty{display:none}
.fmt-box{display:flex;flex-direction:column;gap:10px;align-self:flex-start;width:100%;max-width:300px;padding:0}
.fmt-box>b{font-size:15px}
.fmt-box .fmt{margin:0;flex-wrap:nowrap;align-items:flex-end;gap:16px}
.fmt-box .fmt svg{width:84px;flex:0 0 auto}
.fmt-box .fmt small{display:flex;flex-direction:column;gap:3px;line-height:1.25}
.fmt-box .fmt small br{display:none}
.fmt-box .fmt small em{font-style:normal;font-size:14px;font-weight:800;color:var(--ink);text-transform:none;letter-spacing:0;margin-bottom:4px}
.fmt-box .fmt small b{font-size:12px;letter-spacing:1px}
.fmt-box .fmt small i{align-self:flex-start}
.fmt-box .fmt small .sep{display:none}
.wk-r.propio{font-style:italic!important}
.wk dd small.dd{font-size:.78em;font-weight:700;color:var(--muted);margin-left:4px}
.wk-top{margin-bottom:30px!important}
.tipos{grid-template-columns:repeat(8,minmax(0,1fr))!important}
.wk dl{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))!important;gap:12px 22px!important}
.wk dl .ancho{grid-column:span 2}
.wk-top{align-items:flex-start}
.wk-r.propio{font-size:16px!important;line-height:1.5!important}
.flinks a.red{display:inline-flex;align-items:center;gap:8px}
.flinks a.red svg{flex-shrink:0}
@media (max-width:700px){.wk dl .ancho{grid-column:1/-1}}
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
.esp-g h2 a:hover{color:var(--accent)}
.esp-l{display:flex;flex-direction:column;gap:8px}
.esp-i{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.esp-a{border:2px solid var(--ink);border-radius:999px;padding:5px 14px;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:17px;min-height:40px;display:inline-flex;align-items:center;gap:8px;background:#fff}
.esp-a:hover{background:var(--yellow)}
.esp-a svg{width:22px;height:22px;overflow:visible}
.esp-a small{font-family:'Archivo',sans-serif;font-style:normal;font-size:11px;font-weight:800;color:var(--accent)}
.esp-caps{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:13px;font-weight:700}
.esp-caps a{border-bottom:1px solid var(--accent)}
.esp-caps:before{content:"capítulos »";font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)}
.caps-nav{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:40px 0 0}
.caps-nav a{background:var(--ink);color:var(--paper);padding:8px 14px;font-family:'Fraunces',serif;font-style:italic;font-weight:700;font-size:17px;display:inline-flex;gap:8px;align-items:baseline}
.caps-nav a small{font-family:'Archivo',sans-serif;font-style:normal;font-size:11px;font-weight:800;color:var(--yellow)}
.caps-nav a:hover{background:var(--accent)}
.cap{margin-top:30px}
.cap-h{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 18px;background:var(--yellow);padding:12px 18px;border:2px solid var(--ink)}
.cap-h h2{margin:0;font-size:clamp(28px,3vw,40px);line-height:1}
.cap-h span{font-size:12px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
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

CRONO_CSS = ambito("""
.cr-top{padding:20px 0 18px}
.cr-top h1{margin:0;font-size:clamp(64px,9vw,140px);line-height:.88;letter-spacing:-.03em}
.cr-top h1 em{color:var(--accent)}
.cr-top p{margin:12px 0 0;font-family:'Fraunces',serif;font-style:italic;font-size:21px;max-width:700px}
.cr-ctl{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;padding:10px 0 18px}
.cr-f,.cr-nav{display:flex;gap:8px;flex-wrap:wrap}
.cr-ctl button{font:800 12px 'Archivo',sans-serif;letter-spacing:1.5px;text-transform:uppercase;border:2px solid var(--ink);background:var(--paper);color:var(--ink);padding:8px 12px;min-height:40px;cursor:pointer;display:inline-flex;align-items:center;gap:8px}
.cr-ctl button:hover{background:var(--ink);color:var(--paper)}
.cr-f button i{width:12px;height:12px;border:2px solid var(--ink);background:var(--ink)}
.cr-f .t-noticia i,.cr-f .t-cobertura i{background:var(--accent)}
.cr-f .t-web i{background:var(--yellow)}
.cr-f button small{font-size:11px;color:var(--muted)}
.cr-f button[aria-pressed=false]{opacity:.45;text-decoration:line-through}
.cr-sc{overflow-x:auto;overflow-y:hidden;position:relative;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);cursor:grab;scrollbar-color:var(--accent) #DCD5C6;scrollbar-width:auto;outline:0}
.cr-sc:focus-visible{box-shadow:inset 0 0 0 3px var(--accent)}
.cr-sc.arr{cursor:grabbing;user-select:none}
.cr-sc::-webkit-scrollbar{height:16px}.cr-sc::-webkit-scrollbar-track{background:#DCD5C6}.cr-sc::-webkit-scrollbar-thumb{background:var(--accent);border:3px solid #DCD5C6}
.cr-in{position:relative}
.cr-intro{position:absolute;left:48px;top:0;width:320px;display:flex;flex-direction:column;justify-content:center;gap:10px;z-index:1}
.cr-intro p{margin:0;font-size:46px;line-height:.95}
.cr-intro .caps{font-size:12px;letter-spacing:2px;color:var(--accent)}
.cr-y{position:absolute;top:0;bottom:0;border-left:1px dashed #BDB5A3}
.cr-y .big{position:absolute;left:10px;top:4px;font-size:200px;line-height:.8;color:rgba(22,20,15,.06);pointer-events:none;white-space:nowrap}
.cr-y b{position:absolute;left:-2px;top:calc(var(--sp) + 10px);background:var(--ink);color:var(--yellow);font-size:13px;letter-spacing:1.5px;padding:3px 7px}
.cr-m{position:absolute;top:calc(var(--sp) + 12px);font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--muted);transform:translateX(-50%)}
.cr-m::before{content:'';position:absolute;left:50%;top:-12px;width:1px;height:8px;background:var(--ink)}
.cr-sp{position:absolute;left:0;right:0;height:4px;background:var(--ink)}
.cr-act{position:absolute;left:0;right:0;height:34px;pointer-events:none}
.cr-act i{position:absolute;top:0;width:12px;background:rgba(209,0,111,.22)}
.cr-p{position:absolute;width:170px;z-index:2}
.cr-p:hover{z-index:5}
.cr-c{position:relative;display:flex;flex-direction:column;gap:3px;background:#fff;border:2px solid var(--ink);padding:7px 8px 9px;box-shadow:4px 4px 0 var(--ink);transition:transform .12s,box-shadow .12s}
.cr-c:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--ink)}
.cr-c .ph{display:block;height:66px;margin:-7px -8px 4px;overflow:hidden;background:#DCD5C6;border-bottom:2px solid var(--ink)}
.cr-c .ph img{width:100%;height:100%;object-fit:cover;display:block}
.cr-c .k{font-size:10px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.t-noticia .cr-c .k{color:var(--accent)}
.t-noticia .cr-c{border-top-width:6px;border-top-color:var(--accent)}
.t-web .cr-c{background:var(--yellow)}
.cr-c .f{font-size:11px;font-weight:700;color:var(--muted)}
.cr-c .tt{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:16px;line-height:1.08;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.cr-c .tt em{color:var(--accent);font-style:inherit}
.cr-c .nt{font-size:12px;line-height:1.35}
.cr-p .ld{position:absolute;left:10px;top:0;width:2px;background:var(--ink);z-index:-1}
.cr-p .ld::after{content:'';position:absolute;bottom:-4px;left:-5px;width:12px;height:12px;border-radius:50%;background:var(--paper);border:2px solid var(--ink)}
.t-noticia .ld::after{background:var(--accent)}
.cr-p .ld-h{position:absolute;height:2px;background:var(--ink);z-index:-1}
.cr-p .ld-v{position:absolute;left:10px;width:2px;background:var(--ink);z-index:-1}
.t-web .ld::after{background:var(--yellow)}
.cr-lab{position:absolute;left:48px;font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;color:var(--accent)}
.cr-b{position:absolute;display:flex;align-items:center;height:26px;z-index:3}
.cr-b span{background:var(--ink);color:var(--paper);font-size:12px;font-weight:800;letter-spacing:.5px;padding:0 9px 0 0;height:26px;display:inline-flex;align-items:center;white-space:nowrap}
.cr-b svg{width:26px;height:26px;padding:4px;background:var(--accent);color:#fff;flex-shrink:0;margin-right:7px}
.cr-b i{position:absolute;left:0;top:28px;height:5px;background:var(--accent)}
.cr-b:hover span{background:var(--accent)}
.cr-h{position:absolute;height:20px;background:linear-gradient(var(--accent),var(--accent)) 0 50%/100% 3px no-repeat;border-left:3px solid var(--accent);border-right:3px solid var(--accent)}
.cr-h span{position:sticky;left:8px;display:inline-flex;align-items:center;gap:6px;height:20px;background:var(--paper);padding:0 8px;font-size:11px;font-weight:800;letter-spacing:1px;text-transform:uppercase;white-space:nowrap}
.cr-h span svg{width:16px;height:16px;color:var(--accent)}
.cr-h small{color:var(--muted);font-size:10px}
.cr-h:hover span{color:var(--accent)}
.cr-hoy{position:absolute;top:0;width:0;border-left:3px solid var(--accent)}
.cr-hoy span{position:absolute;top:8px;left:6px;background:var(--accent);color:#fff;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:3px 7px}
.sin-noticia .t-noticia,.sin-pieza .t-pieza,.sin-web .t-web,.sin-cobertura .cr-b,.sin-cobertura .cr-h,.sin-cobertura .cr-lab{display:none}
.cr-mm{position:relative;height:48px;border:2px solid var(--ink);margin:14px 0 8px;background:#fff;cursor:pointer;touch-action:none}
.cr-mm i{position:absolute;top:6px;width:2px;height:16px;background:var(--ink);pointer-events:none}
.cr-mm i.t-noticia{background:var(--accent)}.cr-mm i.t-web{background:#C9A800}
.cr-mm button{position:absolute;bottom:2px;transform:translateX(-50%);border:0;background:none;font:800 10px 'Archivo',sans-serif;color:var(--muted);cursor:pointer;padding:2px}
.cr-mm button:hover{color:var(--accent)}
.cr-mm .vw{position:absolute;top:-2px;bottom:-2px;border:3px solid var(--accent);background:rgba(209,0,111,.08);pointer-events:none}
.cr-nota{font-size:14px;color:var(--muted);margin:0 0 70px}
.cr-pronto{position:relative;overflow:hidden}
.cr-pronto .cr-sc{filter:blur(3px) grayscale(.35);opacity:.55;pointer-events:none;overflow:hidden;max-height:640px}
.cr-velo{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;text-align:center;padding:0 16px;background:radial-gradient(closest-side,rgba(236,231,220,.92),rgba(236,231,220,.55) 70%,transparent)}
.cr-velo .caps{font-size:14px;letter-spacing:3px;color:var(--accent);font-weight:800}
.cr-velo p{margin:0;font-size:clamp(32px,4.6vw,64px);line-height:.98;max-width:820px}
.cr-velo .btn-ink{display:inline-flex;background:var(--ink);color:var(--paper);padding:14px 22px;font-family:'Archivo',sans-serif;font-size:14px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase}
.cr-velo .btn-ink:hover{color:var(--yellow)}
@media (max-width:600px){.cr-top h1{font-size:64px}.cr-intro{width:280px}.cr-intro p{font-size:36px}}
""", '.v-cronologia')

PAG_CSS = BUS_CSS + EST_CSS + FICHA_CSS + ESP_CSS + NOV_CSS + CRONO_CSS + """
.es-pagina main.wrap{display:none}
.v-pag [hidden]{display:none!important}
"""
PAG_JS = (open(os.path.join(D, 'tema_paginas.js')).read()
          .replace('__BUS_JS__', BUS_JS).replace('__EST_JS__', EST_JS))
import json as _json
PAG_JS = PAG_JS.replace('__BUS_HTML__', _json.dumps(BUS_HTML, ensure_ascii=False)).replace('__EST_HTML__', _json.dumps(EST_HTML, ensure_ascii=False))
