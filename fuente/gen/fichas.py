import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from posts import CSS, T, OUT
from common import TIPOS as ICONS, icon, head_interior, HEAD_CSS, MINI_CSS, MINI_JS, TEMAS_CSS, ESPIRAL_COLOR, I18N_CSS, I18N_JS

e = html.escape
import json, re as _re
SD = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'search.json')))
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
def fdate(d):
    return f"{int(d[8:10])} {MESES[int(d[5:7]) - 1]} {d[:4]}"
def idx_of(lst, n):
    return next(i for i, x in enumerate(lst) if x['n'] == n)
def posts_of(f):
    key = 'm' if f['clase'] == 'Medio' else 'a'
    i = idx_of(SD['medios'] if key == 'm' else SD['autores'], f['nombre'])
    return key, i, [p for p in SD['posts'] if i in p[key]]
FLAG = 'https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/flags/4x3/{}.svg'
from medios_assets import info as m_info, logo as m_logo, avatar as m_avatar
def AV(n, cls='av-slot'):
    u = m_avatar(n)
    return f'<span class="{cls}" aria-hidden="true"><img src="{u}" alt=""></span>' if u else ''
CIS = dict(href='post-cis.html', tipo='graf', medio='El País', fecha='11 oct 2026', titulo='Qué preocupa a los votantes de cada partido', por='Daniele Grasso y Yolanda Clemente',
           img=T + 'ecc4f5ce19ed114d3cd95545ff3bf759/de2d9184085a3fef-5d/s1280x1920/45f6bbed7ff64ec88566e929ae4981f17445d48f.png')
GAZA = dict(href='inconsolata-mucho-mas.html#mm-15', tipo='carto', medio='El País', fecha='18 oct 2026', titulo='Las fortificaciones de Israel en Gaza', por='Luis Sevillano', nota='en «mucho más» DCCLXXXI',
            img=T + 'f6fac235ea66b66f42437467878d10fd/0a4967b287ac3b00-5c/s1280x1920/e622d48bfe91cd3e5fdf887f7d9e488441f84e12.png')
PORT = dict(href='#', tipo='port', medio='El País', fecha='8 oct 2026', titulo='Una portada llena de indignación', por='',
            img=T + '3c4792786a6ad0eb398063bf76094bd8/002b0ef65ae9bcf1-ef/s1280x1920/70537c7708bf23754db29628597fef3fdeb20451.jpg')

NYT175 = dict(href='post-nyt175.html', tipo='port', medio='The New York Times', fecha='18 sep 2026', titulo='Los 175 años del New York Times', por='',
              img=T + '313549c3182642c3311b817408cb42a1/465a726c37b7af6b-bf/s2048x3072/d01892336abe40a93736a3cd6c51d07155d90a01.png')
FOOD = dict(href='post-food101.html', tipo='ilus', medio='The New York Times', fecha='17 abr 2026', titulo='Doce chefs y un manual para comer lo difícil', por='Ryuto Miyake',
            img=T + '4544a4bfb0a98a7ed4b195eef4c2ba28/eb7f9b0849d9ebc9-79/s1280x1920/a251119d8f0827da6c6c89b88cac7f00d12ac35a.png')
LIBE = dict(href='post-liberation.html', tipo='port', medio='Libération', fecha='16 oct 2026', titulo='Libération se vuelve anárquica por Perec', por='',
            img=T + '093da2d5a18de7d40895b9ad174fe7ed/dfb73906028a5e2a-ea/s1280x1920/a1ccf50f328829da941a6c0a54c285506f0887c7.jpg')
COMMONS = 'https://commons.wikimedia.org/wiki/Special:FilePath/'

def wiki_html(f):
    w = f.get('wiki')
    if not w or not m_info(f['nombre']).get('qid'):
        return ''
    rows = ''.join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' for k, v in w['datos'])
    return (f'<div class="wk"><div class="wk-h"><span class="caps">Datos »</span>'
            f'<a class="wk-src" href="{w["url"]}" target="_blank" rel="noopener">Fuente: Wikipedia · CC BY-SA »</a></div>'
            f'<div class="wk-top">{AV(f["nombre"])}<p class="wk-r">{e(w["resumen"])}</p></div><dl>{rows}</dl>'
            '</div>')

FICHAS = [
 dict(file='ficha-medio-nyt.html', clase='Medio', nombre='The New York Times', pais='Estados Unidos', cc='us', tipo_m='diario', fund=1851,
      visual='<div class="logo-big logo-wk"><img src="' + COMMONS + 'NewYorkTimes.svg?width=700" alt="Logo de The New York Times" onerror="this.parentNode.classList.add(\'nologo\');this.replaceWith(\'[ logo · The New York Times ]\')"></div>',
      texto='[Aquí va tu texto sobre el medio, si quieres añadir algo más allá de los datos de Wikipedia.]',
      links=[('nytimes.com', 'https://www.nytimes.com'), ('Wikipedia', 'https://en.wikipedia.org/wiki/The_New_York_Times')],
      rel_t='Autores más citados', rel=[('Ryuto Miyake', '#'), ('[más autores]', '#')],
      wiki=dict(url='https://en.wikipedia.org/wiki/The_New_York_Times',
                resumen='Periódico con sede en Manhattan (Nueva York) que cubre información local, nacional e internacional y publica artículos de opinión y críticas.',
                datos=[('Fundación', '18 de septiembre de 1851'), ('Fundadores', 'Henry Jarvis Raymond, George Jones y Edward B. Wesley'),
                       ('Sede', 'The New York Times Building, Manhattan'), ('Propietario', 'The New York Times Company'),
                       ('Formato', 'Diario · sábana'), ('Idioma', 'Inglés'), ('ISSN', '0362-4331'), ('Web', 'nytimes.com')],
                estado='<span class="ok">✓ Logo libre en Wikimedia Commons</span><span class="ok">✓ Datos de Wikipedia</span>'),
      posts=[NYT175, FOOD]),
 dict(file='ficha-medio-liberation.html', clase='Medio', nombre='Libération', pais='Francia', cc='fr', tipo_m='diario', fund=1973,
      visual='<div class="logo-big nologo">[ logo · Libération ]<span class="need">Pendiente: no he encontrado un logo libre en Commons. Me lo pasas tú.</span></div>',
      texto='[Aquí va tu texto sobre el medio: por ejemplo, sus portadas y ediciones especiales más recordadas.]',
      links=[('liberation.fr', 'https://www.liberation.fr'), ('Wikipedia', 'https://en.wikipedia.org/wiki/Lib%C3%A9ration')],
      rel_t='Autores más citados', rel=[('[autores del índice]', '#')],
      wiki=dict(url='https://en.wikipedia.org/wiki/Lib%C3%A9ration',
                resumen='Diario francés fundado en París en 1973 por Jean-Paul Sartre y Serge July, tras los movimientos de protesta de mayo del 68. Popularmente conocido como Libé.',
                datos=[('Fundación', '1973'), ('Fundadores', 'Jean-Paul Sartre y Serge July'), ('Sede', 'París'),
                       ('Propietario', 'Bruno Ledoux'), ('Formato', 'Diario · compacto'), ('Línea', 'Centroizquierda'),
                       ('Idioma', 'Francés'), ('ISSN', '0335-1793'), ('Web', 'liberation.fr')],
                estado='<span class="ok">✓ Datos de Wikipedia</span><span class="ko">✗ Logo: no encontrado, pendiente de que lo envíes</span>'),
      posts=[LIBE]),
 dict(file='ficha-medio-el-pais.html', clase='Medio', nombre='El País', pais='España', cc='es', tipo_m='diario', fund=1976,
      visual='<div class="logo-big">[ logo · El País ]</div>',
      texto='[Aquí va tu texto sobre el medio: su historia gráfica, el equipo de infografía, qué te gusta de su trabajo, enlaces a su sección de gráficos…]',
      links=[('Web del medio', '#'), ('Sección de gráficos', '#'), ('X', '#')],
      rel_t='Autores más citados', rel=[('Daniele Grasso', 'ficha-autor-daniele-grasso.html'), ('Yolanda Clemente', '#'), ('Luis Sevillano', '#'), ('[más autores]', '#')],
      wiki=dict(url='https://es.wikipedia.org/wiki/El_Pa%C3%ADs',
                resumen='Diario español de información general fundado en Madrid en 1976, en plena Transición. Es uno de los periódicos de referencia en España y tiene ediciones para América y Brasil.',
                datos=[('Fundación', '4 de mayo de 1976'), ('Fundador', 'José Ortega Spottorno'), ('Sede', 'Madrid'), ('Propietario', 'PRISA'),
                       ('Formato', 'Diario · berlinés'), ('Idioma', 'Español'), ('Web', 'elpais.com')],
                estado='<span class="ok">✓ Datos de Wikipedia</span><span class="ko">✗ Logo: pendiente de que lo envíes</span>'),
      posts=[CIS, PORT, GAZA]),
 dict(file='ficha-autor-daniele-grasso.html', clase='Periodista', nombre='Daniele Grasso', sub='Datos e infografía', medio='El País', medio_href='ficha-medio-el-pais.html',
      visual='',
      texto='[Aquí va tu texto sobre el periodista: dónde trabaja, en qué está especializado, trabajos suyos que destacarías, su web o perfil…]',
      links=[('Web o perfil', '#'), ('X', '#')],
      rel_t='Medios', rel=[('El País', 'ficha-medio-el-pais.html')],
      rel2_t='Suele firmar con', rel2=[('Yolanda Clemente', '#'), ('[más colaboradores]', '#')],
      posts=[CIS]),
]

FCSS = """
.logo-wk{background:#fff;border:2px solid var(--ink);padding:28px}
.logo-wk img{max-width:100%;max-height:100%;object-fit:contain;display:block}
.logo-big.nologo{flex-direction:column;gap:12px;text-align:center;padding:20px}
.logo-big .need{font-size:13px;font-weight:700;color:var(--accent);max-width:220px}
.wk{background:#fff;border:2px solid var(--ink);padding:20px 22px;max-width:820px;display:flex;flex-direction:column;gap:12px}
.wk-h{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px}
.wk-src{font-size:12px;font-weight:700;color:var(--muted);border-bottom:1px solid var(--muted)}
.wk-r{margin:0;font-family:'Fraunces',serif;font-style:italic;font-size:19px;line-height:1.45}
.wk dl{margin:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px 20px}
.wk dt{font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)}
.wk dd{margin:2px 0 0;font-size:15px;font-weight:600}
.wk-st{display:flex;flex-wrap:wrap;gap:8px;border-top:1px dashed var(--ink);padding-top:12px}
.wk-st span{font-size:12px;font-weight:800;padding:6px 10px}
.wk-st .ok{background:#DDEFD9;color:#1C4D17}.wk-st .ko{background:#F8D9E7;color:#7A0041}

.fhero{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:40px;padding:20px 0 56px;align-items:start}
.fvis{grid-column:1/4}
.fhero.novis .finfo{grid-column:1/13}
.logo-big{background:#fff;border:2px dashed var(--ink);aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:var(--muted);box-shadow:10px 10px 0 var(--ink);transform:rotate(-2deg)}
.mono{background:var(--yellow);aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:clamp(90px,11vw,170px);line-height:1;box-shadow:10px 10px 0 var(--accent);transform:rotate(-2deg)}
.finfo{grid-column:4/13;display:flex;flex-direction:column;gap:18px}
.finfo h1{margin:0;font-size:clamp(64px,9vw,148px);line-height:.88;letter-spacing:-.03em}
.ftext{position:relative;border:2px dashed var(--ink);background:rgba(255,255,255,.55);padding:26px 24px 22px;font-family:'Fraunces',serif;font-size:21px;line-height:1.5;max-width:820px}
.ftext .lbl{position:absolute;top:-13px;left:18px;background:var(--accent);color:#fff;font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;padding:4px 8px}
.flinks{display:flex;flex-wrap:wrap;gap:8px}
.flinks a{border:2px solid var(--ink);padding:10px 14px;font-size:13px;font-weight:700;min-height:44px;display:inline-flex;align-items:center}
.band{background:var(--ink);color:var(--paper);position:relative;overflow:hidden}
.band .wm-av{position:absolute;top:-36px;right:-10px;width:290px;height:290px;object-fit:contain;opacity:.12;filter:blur(.4px);transform:rotate(-14deg);pointer-events:none}
.band .in{position:relative}
@media (max-width:700px){.band .wm-av{width:200px;height:200px;top:-24px;right:-40px}}
.band .in{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:36px;padding:40px 24px}
.stat{display:flex;flex-direction:column;gap:6px}
.stat b{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-variation-settings:'SOFT' 100,'WONK' 1,'opsz' 144;font-size:56px;line-height:1;color:var(--yellow)}
.stat span{font-size:13px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips a{border:2px solid var(--paper);color:var(--paper);padding:8px 12px;font-family:'Fraunces',serif;font-style:italic;font-size:17px;min-height:40px;display:inline-flex;align-items:center}
.chips a:hover{background:var(--paper);color:var(--ink)}
.tipos{display:grid;grid-template-columns:repeat(9,minmax(0,1fr));gap:6px}
.tipos a{display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;align-items:center;column-gap:6px;color:var(--paper);border:1px solid #4A463D;padding:8px 7px;min-height:44px;min-width:0}
.tipos a svg{grid-row:1/3;width:26px;height:26px}
.tipos a b{font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:24px;line-height:1;color:var(--yellow)}
.tipos a span{grid-column:2;font-size:10px;font-weight:800;letter-spacing:0;text-transform:uppercase;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tipos a:hover{background:#2C2922;color:var(--paper)}
@media (max-width:980px){.tipos{display:flex;overflow-x:auto;padding-bottom:4px}.tipos a{flex:0 0 120px}}
.fl-dates{display:flex;flex-wrap:wrap;gap:6px 26px;margin-top:14px;padding-top:12px;border-top:1px dashed #4A463D}
.fl-dates span{font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase}
.fl-dates a{color:var(--yellow);font-family:'Fraunces',serif;font-style:italic;font-size:18px;text-transform:none;letter-spacing:0;border-bottom:1px solid var(--yellow)}
.ante{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.flag{width:24px;height:18px;object-fit:cover;box-shadow:0 0 0 1px rgba(22,20,15,.25);display:inline-block}
.wk-top{display:flex;gap:18px;align-items:flex-start}
.av-slot{width:84px;height:84px;flex-shrink:0;outline:1px dashed #B9B2A3;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:var(--muted);font-family:'Archivo',sans-serif;font-style:normal}
.av-slot img{width:100%;height:100%;object-fit:contain}
.name-row{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;flex-wrap:wrap}
.av-medio{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase}
.av-medio .av-slot{width:96px;height:96px;outline:0}
.av-slot:has(img){outline:0}
.av-medio:hover .av-slot{outline-color:var(--accent)}
.work{position:relative;margin:0;display:flex;flex-direction:column;gap:10px;background:#fff;padding:12px 12px 16px;box-shadow:10px 10px 0 var(--ink);transform:rotate(-2deg)}
.wph{display:block;aspect-ratio:4/5;overflow:hidden;background:#DAD4C6 radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px}
.wph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform .4s}
.wph:hover img{transform:scale(1.03)}
.work figcaption{display:flex;flex-direction:column;gap:3px;padding-right:70px}
.wn{font-family:'Fraunces',serif;font-style:italic;font-size:18px;line-height:1.2}
.wn b{font-weight:900;color:var(--accent)}
.wm{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:var(--muted)}
.wnext{position:absolute;right:-16px;bottom:22px;width:76px;height:76px;border-radius:50%;border:0;background:var(--accent);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;cursor:pointer;box-shadow:4px 4px 0 var(--ink);transform:rotate(8deg);transition:transform .25s;font-family:'Fraunces',serif;font-style:italic;font-weight:900;font-size:17px}
.wnext:hover{transform:rotate(-12deg) scale(1.06)}
.wnext:active{transform:rotate(-200deg)}
.chart .bar.real{background:var(--ink);border:0;border-radius:3px 3px 0 0;position:relative}
.chart .bar.real span{position:absolute;bottom:100%;left:0;right:0;text-align:center;font-size:11px;font-weight:800;padding-bottom:3px}
.chart .bar.real:hover{background:var(--accent)}
.tipos .k{color:var(--paper)}
.years{padding:56px 0 8px}
.chart{border-bottom:2px solid var(--ink);height:190px;display:grid;grid-template-columns:repeat(16,minmax(0,1fr));align-items:end;gap:6px;padding:16px 16px 0;position:relative}
.chart .bar{background:repeating-linear-gradient(45deg,rgba(22,20,15,.18) 0 4px,transparent 4px 9px);height:40%;border:1px solid rgba(22,20,15,.25);border-bottom:0}
.chart .note{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:var(--muted)}
.yax{display:grid;grid-template-columns:repeat(16,minmax(0,1fr));gap:6px;padding:6px 16px 0;font-size:11px;font-weight:700;text-align:center}
.entries{padding:56px 0 96px;display:flex;flex-direction:column;gap:36px}
.entries .fbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;border-bottom:2px solid var(--ink);padding-bottom:16px}
.entries .fbar button{font-family:'Archivo',sans-serif;font-size:14px;font-weight:700;background:transparent;color:var(--ink);border:2px solid var(--ink);padding:8px 14px;min-height:44px;cursor:pointer}
.entries .fbar button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,270px),1fr));gap:56px 40px;padding-top:30px}
.card .note{font-size:12px;font-weight:700;color:var(--accent);letter-spacing:1px;text-transform:uppercase}
.card.ph-card .ph{background:#DAD4C6 radial-gradient(#16140F 1.1px,transparent 1.3px) 0 0/7px 7px}
.card .by{font-family:'Fraunces',serif;font-style:italic;font-size:16px}
.more-btn{align-self:center;background:var(--ink);color:var(--paper);padding:16px 26px;font-size:15px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;border:0;min-height:44px;cursor:pointer;font-family:'Archivo',sans-serif}
@media (max-width:860px){.fhero{display:flex;flex-direction:column}.fvis{width:60%}}
"""

YEARS = list(range(2011, 2027))

def card(p):
    note = f'<span class="note">{e(p["nota"])}</span>' if p.get('nota') else ''
    por = f'<span class="by">por {e(p["por"])}</span>' if p.get('por') else ''
    return (f'<a href="{p["href"]}" class="card" data-tipo="{p["tipo"]}"><span class="tape" aria-hidden="true"></span>{icon(p["tipo"], "ico")}'
            f'<div class="ph"><img loading="lazy" src="{p["img"]}" alt="" onerror="this.remove()"></div>'
            f'<span class="caps">» {e(p["medio"])} · {e(p["fecha"])}</span><span class="tt">{e(p["titulo"])}</span>{por}{note}</a>')

def ph_card():
    return ('<div class="card ph-card" aria-hidden="true"><span class="tape"></span><div class="ph"></div>'
            '<span class="caps">» [medio · fecha]</span><span class="tt">[otra entrada del archivo]</span></div>')

def page(f):
    key, mi, ps = posts_of(f)
    from collections import Counter
    ck = Counter(k for p in ps for k in p['k'])
    cy = Counter(int(p['d'][:4]) for p in ps)
    mx = max(cy.values())
    first, last = ps[-1], ps[0]
    # relaciones reales del índice
    if key == 'm':
        ca = Counter(a for p in ps for a in p['a'] if f['nombre'] in SD['autores'][a]['m'])
        f['rel'] = [(SD['autores'][a]['n'], 'ficha-autor-daniele-grasso.html' if SD['autores'][a]['n'] == 'Daniele Grasso' else '#') for a, _ in ca.most_common(6)]
    else:
        cm = Counter(m for p in ps for m in p['m'])
        ca = Counter(a for p in ps for a in p['a'] if a != mi)
        f['rel'] = [(n, 'ficha-medio-el-pais.html' if n == 'El País' else '#') for n in SD['autores'][mi]['m']]
        f['rel2'] = [(SD['autores'][a]['n'], '#') for a, _ in ca.most_common(5)]
    chips = lambda items: ''.join(f'<a href="{h}">{e(n)}</a>' for n, h in items)
    rel2 = (f'<div class="stat"><span>{e(f["rel2_t"])}</span><div class="chips">{chips(f["rel2"])}</div></div>' if f.get('rel2') else '')
    tipos = ''.join(f'<a href="inconsolata-buscador.html#{key}={mi}&k={t}">{icon(t)}<b>{ck.get(t, 0)}</b><span>{ICONS[t][0]}</span></a>'
                    for t in ('info', 'carto', 'port', 'graf', 'ilus', 'foto', 'video', 'publi', 'online'))
    bars = ''.join(f'<div class="bar real" style="height:{max(2, cy.get(y, 0) / mx * 100):.0f}%" title="{y}: {cy.get(y, 0)} entradas"><span>{cy.get(y, 0) or ""}</span></div>' for y in YEARS)
    ylab = ''.join(f'<span>{str(y)[2:]}</span>' for y in YEARS)
    entries = ''.join(card(p) for p in f['posts']) + ''.join(ph_card() for _ in range(6 - len(f['posts'])))
    plink = lambda p: f'<a href="https://inconsolata.com/post/{p["u"]}">{fdate(p["d"])}</a>'
    primera = (f'<div class="fl-dates"><span>Primera entrada en inconsolata»: {plink(first)}</span>'
               f'<span>Última: {plink(last)}</span></div>')
    if key == 'm':
        fm = m_info(f['nombre'])
        f['cc'] = fm.get('cc', ''); f['pais'] = fm.get('pais', ''); f['fund'] = int(fm['fundacion']) if fm.get('fundacion') else None
        lg = m_logo(f['nombre'], 700)
        f['visual'] = (f'<div class="logo-big logo-wk"><img src="{lg}" alt="Logo de {e(f["nombre"])}" onerror="this.closest(\'.fhero\').classList.add(\'novis\');this.closest(\'.fvis\').remove()"></div>' if lg else '')
        ante = (f'{e(f["clase"])} » ' + (f'<img class="flag" src="{FLAG.format(f["cc"])}" alt="" width="24" height="18">' if f['cc'] else '') +
                f'{e(f["pais"])} · {e(f["tipo_m"])}')
        big2 = (f'<div class="stat"><b>{2026 - f["fund"]}</b><span>años publicándose · desde {f["fund"]}</span></div>' if f['fund'] else '')
        name_row = f'<h1 class="soft">{e(f["nombre"])}</h1>'
        visual = f['visual']
    else:
        ante = f'{e(f["clase"])} » {e(f["sub"])}'
        big2 = f'<div class="stat"><b>{len(cy)}</b><span>años apareciendo en inconsolata» · de {min(cy)} a {max(cy)}</span></div>'
        name_row = (f'<div class="name-row"><h1 class="soft">{e(f["nombre"])}</h1>'
                    f'<a class="av-medio" href="{f["medio_href"]}" aria-label="Trabaja en {e(f["medio"])}">{AV(f["medio"])}<span>{e(f["medio"])} »</span></a></div>')
        works = [dict(img=_re.sub(r'/s400x600/', '/s1280x1920/', p['im']), u=p['u'], d=fdate(p['d']),
                      m=', '.join(SD['medios'][m]['n'] for m in p['m'][:2]), s=p['d'])
                 for p in ps if p['im'] and len(p['a']) <= 6]
        works.sort(key=lambda w: w['s'])
        visual = ('<figure class="work"><span class="tape" aria-hidden="true"></span>'
                  '<a class="wph" id="work-a" href="#" aria-label="Abrir esta pieza en inconsolata»"><img id="work-img" alt="" src=""></a>'
                  '<button type="button" class="wnext" id="work-next" aria-label="Ver otra pieza al azar">'
                  '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 7h11l-3-3M20 17H9l3 3M15 4l3 3-3 3M9 20l-3-3 3-3" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><span>otra</span></button>'
                  '<figcaption><span class="wn">Pieza <b id="work-n"></b> de <b>' + str(len(works)) + '</b> en el archivo</span><span class="wm" id="work-m"></span></figcaption></figure>'
                  '<script>(function(){var W=' + json.dumps(works, ensure_ascii=False) + ',i=Math.floor(Math.random()*W.length);'
                  'function show(){var w=W[i%W.length];document.getElementById("work-a").href="https://inconsolata.com/post/"+w.u;'
                  'document.getElementById("work-img").src=w.img;document.getElementById("work-n").textContent=(i%W.length)+1;'
                  'document.getElementById("work-m").textContent="» "+w.m+" · "+w.d;}'
                  'show();document.getElementById("work-next").addEventListener("click",function(){i+=1+Math.floor(Math.random()*(W.length-1));show();});})();</script>')
    n_total = len(ps)
    from medios_assets import avatar_barra as _avb
    _w = _avb(f['nombre']) if key == 'm' else ''
    wm = f'<img class="wm-av" src="{_w}" alt="" aria-hidden="true">' if _w else ''
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(f['nombre'])} · inconsolata» (maqueta)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,100..900,0..100,0..1;1,9..144,100..900,0..100,0..1&display=swap">
<style>{CSS}{HEAD_CSS}{MINI_CSS}{TEMAS_CSS}{I18N_CSS}{FCSS}</style>
</head>
<body>
<div class="page">
{head_interior()}
<main>
<div class="wrap">
<div class="crumbs caps"><a href="inconsolata-portada.html">Portada</a><i>»</i><a href="#">{'Medios' if f['clase']=='Medio' else 'Autores'}</a><i>»</i><span>{e(f['nombre'])}</span></div>
<section class="fhero{'' if visual else ' novis'}">
{f'<div class="fvis">{visual}</div>' if visual else ''}
<div class="finfo">
<span class="caps ante" style="color:var(--accent)">{ante}</span>
{name_row}
<div class="ftext"><span class="lbl">Tu texto</span>{e(f['texto'])}</div>
{wiki_html(f)}
<div class="flinks">{''.join(f'<a href="{h}">{e(n)} »</a>' for n, h in f['links'])}</div>
</div>
</section>
</div>
<section class="band">{wm}<div class="wrap in">
<div class="stat"><b>{n_total}</b><span>entradas en inconsolata»</span></div>
{big2}
<div class="stat"><span>{e(f['rel_t'])}</span><div class="chips">{chips(f['rel'])}</div></div>
{rel2}
<div class="stat" style="grid-column:1/-1"><span>Tipos de pieza</span><div class="tipos">{tipos}</div>{primera}</div>
</div></section>
<div class="wrap">
<section class="years">
<div class="caps" style="margin-bottom:14px">Entradas por año »</div>
<div class="chart">{bars}</div>
<div class="yax">{ylab}</div>
</section>
<section class="entries">
<div class="fbar"><span class="caps" style="margin-right:6px">Todas las entradas »</span>
<button type="button" aria-pressed="true" data-f="todas">Todas</button>
<button type="button" aria-pressed="false" data-f="info">Infografía</button>
<button type="button" aria-pressed="false" data-f="carto">Cartografía</button>
<button type="button" aria-pressed="false" data-f="graf">Gráfico</button>
<button type="button" aria-pressed="false" data-f="port">Portada</button>
</div>
<div class="grid">{entries}</div>
<button type="button" class="more-btn">Cargar más »</button>
</section>
</div>
</main>
<footer>
<div class="cmyk-bar" aria-hidden="true"><span style="background:#00A0DC"></span><span style="background:#66C6EA"></span><span style="background:#E5007E"></span><span style="background:#EF66B2"></span><span style="background:#FFD400"></span><span style="background:#FFE566"></span><span style="background:#16140F"></span><span style="background:#7A766C"></span></div>
<div class="wrap foot"><span class="soft" style="font-size:56px;line-height:1">inc<span style="color:#EF66B2">»</span></span><span>© inconsolata» 2011–2026 · un blog de Saúl Castillo</span></div>
</footer>
</div>
<script>
document.querySelectorAll('.fbar button').forEach(function(b){{
 b.addEventListener('click', function(){{
  document.querySelectorAll('.fbar button').forEach(function(x){{x.setAttribute('aria-pressed','false');}});
  b.setAttribute('aria-pressed','true');
  var f=b.getAttribute('data-f');
  document.querySelectorAll('.grid .card').forEach(function(c){{
   var t=c.getAttribute('data-tipo'); c.hidden = !(f==='todas' || t===f);
  }});
 }});
}});
</script>
{MINI_JS}
{I18N_JS}
</body>
</html>
"""

for f in FICHAS:
    with open(os.path.join(OUT, f['file']), 'w') as fh:
        fh.write(page(f))
print('ok')
