"""Iconos propios de cada tema (64x64, mismo trazo que los iconos de tipo y la urna)."""
S4 = 'stroke="currentColor" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
F = 'fill="currentColor"'

def g(body, fill='none'):
    return f'<g {S4} fill="{fill}">{body}</g>'

TI = {
 'Elecciones': g('<path d="M22 30 V6 H42 V30"/><path d="M27 16 L31 21 L38 12"/><path d="M4 30 H60"/><path d="M8 30 V58 H56 V30"/><path d="M20 30 H44" stroke-width="7"/>'
                 f'<rect x="22" y="40" width="20" height="9" {F}/>'),
 'Elecciones en EEUU': g(f'<path d="M10 60 V6"/><path d="M10 8 H54 V38 H10"/><rect x="10" y="8" width="18" height="15" {F}/><path d="M28 16 H54 M28 24 H54 M10 31 H54"/>'),
 'Guerras y conflictos': g(f'<path d="M14 14 L50 50 M50 14 L14 50"/><path d="M38 54 L54 38 M10 38 L26 54"/><circle cx="14" cy="14" r="4" {F}/><circle cx="50" cy="14" r="4" {F}/>'),
 'Guerra en Ucrania': g(f'<circle cx="32" cy="24" r="8" {F}/><path d="M32 6 V10 M32 38 V42 M14 24 H18 M46 24 H50 M19 11 L22 14 M45 11 L42 14 M19 37 L22 34 M45 37 L42 34"/><path d="M32 42 V60"/><path d="M32 54 C24 52 20 48 18 44 C26 44 30 48 32 54"/>'),
 'Conflicto palestino-israelí': g(f'<path d="M10 56 C26 46 38 30 54 10"/><path d="M22 47 C16 44 14 38 16 34 C21 37 23 42 22 47 Z" {F}/><path d="M33 36 C34 30 39 26 44 26 C42 31 38 35 33 36 Z" {F}/><path d="M40 26 C36 22 36 16 38 12 C42 16 42 21 40 26 Z"/><path d="M27 41 C30 36 36 34 40 36 C36 40 31 42 27 41 Z"/>'),
 'Guerra en Siria': g(f'<path d="M8 58 H56"/><path d="M14 58 V22 L22 16 L26 24 L32 14 L36 22 L42 18 L50 26 V58"/><rect x="21" y="32" width="7" height="8" {F}/><rect x="36" y="32" width="7" height="8"/><path d="M28 58 V48 H36 V58"/>'),
 'Guerra en Irán': g(f'<path d="M32 4 C40 12 42 24 42 34 V46 H22 V34 C22 24 24 12 32 4 Z"/><path d="M22 38 L12 50 V54 H22 M42 38 L52 50 V54 H42"/><path d="M26 50 L32 60 L38 50 Z" {F}/><circle cx="32" cy="24" r="4" {F}/>'),
 'Terrorismo y atentados': g(f'<path d="M32 4 L37 22 L54 14 L44 30 L60 36 L42 40 L48 58 L32 46 L16 58 L22 40 L4 36 L20 30 L10 14 L27 22 Z"/><circle cx="32" cy="32" r="6" {F}/>'),
 'Catástrofes y accidentes': g('<path d="M4 34 H16 L22 14 L30 54 L38 20 L44 34 H60"/><path d="M8 58 H56" stroke-dasharray="2 8"/>'),
 'COVID-19': g(f'<circle cx="32" cy="32" r="14"/><circle cx="27" cy="29" r="3.5" {F}/><circle cx="37" cy="36" r="3" {F}/><path d="M32 18 V8 M32 46 V56 M18 32 H8 M46 32 H56 M22 22 L15 15 M42 42 L49 49 M42 22 L49 15 M22 42 L15 49"/><circle cx="32" cy="6" r="3" {F}/><circle cx="32" cy="58" r="3" {F}/><circle cx="6" cy="32" r="3" {F}/><circle cx="58" cy="32" r="3" {F}/>'),
 'Salud': g(f'<path d="M24 8 H40 V24 H56 V40 H40 V56 H24 V40 H8 V24 H24 Z"/><path d="M14 32 H24 L28 24 L34 40 L38 32 H50"/>'),
 'Economía': g(f'<circle cx="32" cy="32" r="24"/><path d="M42 20 C38 16 34 15 30 16 C22 18 18 25 18 32 C18 39 22 46 30 48 C34 49 38 48 42 44"/><path d="M12 28 H34 M12 36 H34" stroke-width="5"/>'),
 'Brexit y Europa': g(''.join(f'<circle cx="{30 + 20 * __import__("math").cos(i * 3.14159 / 6):.1f}" cy="{32 + 20 * __import__("math").sin(i * 3.14159 / 6):.1f}" r="3.4" {F}/>' for i in range(1, 12)) + '<circle cx="58" cy="30" r="3.4"/><path d="M48 32 H52" stroke-width="2.5"/>'),
 'Monarquía y realeza': g(f'<path d="M8 46 L6 18 L20 30 L32 10 L44 30 L58 18 L56 46 Z"/><path d="M8 54 H56"/><circle cx="32" cy="34" r="5" {F}/><circle cx="6" cy="16" r="3" {F}/><circle cx="58" cy="16" r="3" {F}/><circle cx="32" cy="8" r="3" {F}/>'),
 'El Papa y el Vaticano': g(f'<path d="M16 58 V30 C16 18 24 10 32 4 C40 10 48 18 48 30 V58 Z"/><path d="M32 22 V44 M24 30 H40" stroke-width="5"/><path d="M16 50 H48"/>'),
 'Cataluña y el procés': g(f'<rect x="8" y="10" width="48" height="44"/><rect x="8" y="16" width="48" height="5" {F}/><rect x="8" y="26" width="48" height="5" {F}/><rect x="8" y="36" width="48" height="5" {F}/><rect x="8" y="46" width="48" height="5" {F}/>'),
 'Necrológicas': g(f'<rect x="22" y="30" width="20" height="28"/><path d="M32 30 V24"/><path d="M32 4 C38 12 40 16 38 20 C36 24 28 24 26 20 C24 16 26 12 32 4 Z" {F}/><path d="M14 58 H50"/>'),
 'Historia': g(f'<path d="M14 6 H50 M14 58 H50"/><path d="M18 6 C18 22 30 26 30 32 C30 38 18 42 18 58 M46 6 C46 22 34 26 34 32 C34 38 46 42 46 58"/><path d="M24 52 C26 46 30 44 32 44 C34 44 38 46 40 52 Z" {F}/>'),
 'Resúmenes del año': g(f'<rect x="8" y="12" width="48" height="44"/><path d="M8 24 H56" stroke-width="7"/><path d="M20 6 V16 M44 6 V16"/><path d="M18 38 L23 34 V50"/><path d="M32 38 C32 33 44 33 44 38 C44 42 33 45 32 50 H45"/>'),
 'Ciencia y espacio': g(f'<circle cx="32" cy="32" r="14" {F}/><ellipse cx="32" cy="32" rx="28" ry="9" transform="rotate(-20 32 32)"/><circle cx="54" cy="10" r="2.5" {F}/><circle cx="8" cy="54" r="2" {F}/>'),
 'Clima y medio ambiente': g(f'<path d="M26 40 V10 C26 6 34 6 34 10 V40"/><circle cx="30" cy="48" r="9"/><circle cx="30" cy="48" r="5" {F}/><path d="M30 44 V22"/><path d="M42 14 H50 M42 22 H48 M42 30 H50"/>'),
 'Biodiversidad': g(f'<path d="M12 52 C10 30 24 12 54 10 C54 38 38 54 12 52 Z"/><path d="M12 52 L40 24 M22 42 H34 M30 34 V22"/><circle cx="12" cy="52" r="3" {F}/>'),
 'Viajes': g(f'<path d="M30 6 C34 6 35 10 35 14 V26 L56 38 V44 L35 38 V50 L42 56 V60 L32 57 L22 60 V56 L29 50 V38 L8 44 V38 L29 26 V14 C29 10 30 6 30 6 Z"/>'),
 'Tecnología': g(f'<rect x="16" y="16" width="32" height="32"/><rect x="24" y="24" width="16" height="16" {F}/><path d="M24 16 V8 M32 16 V8 M40 16 V8 M24 48 V56 M32 48 V56 M40 48 V56 M16 24 H8 M16 32 H8 M16 40 H8 M48 24 H56 M48 32 H56 M48 40 H56"/>'),
 'Deportes': g(f'<path d="M18 8 H46 V22 C46 32 40 38 32 38 C24 38 18 32 18 22 Z"/><path d="M18 14 H8 C8 24 12 28 18 28 M46 14 H56 C56 24 52 28 46 28"/><path d="M32 38 V48"/><rect x="20" y="48" width="24" height="10" {F}/>'),
 'Fútbol': g(f'<circle cx="32" cy="32" r="25"/><path d="M32 22 L41 29 L38 40 H26 L23 29 Z" {F}/><path d="M32 22 V8 M41 29 L55 25 M38 40 L46 52 M26 40 L18 52 M23 29 L9 25"/>'),
 'Juegos Olímpicos': g(f'<path d="M22 22 H42 L36 58 H28 Z"/><path d="M18 22 H46"/><path d="M32 4 C40 10 40 16 36 20 H28 C24 16 24 10 32 4 Z" {F}/>'),
 'Mundiales y Eurocopas': g('<path d="M6 54 V14 H58 V54"/><path d="M6 14 L14 24 H50 L58 14 M14 24 V54 M50 24 V54"/><path d="M14 34 H50 M14 44 H50 M26 24 V54 M38 24 V54" stroke-width="2"/><path d="M2 54 H62"/>'),
 'Motor y ciclismo': g(f'<path d="M12 60 V6"/><path d="M12 8 H54 V38 H12"/><rect x="12" y="8" width="10.5" height="7.5" {F}/><rect x="33" y="8" width="10.5" height="7.5" {F}/><rect x="22.5" y="15.5" width="10.5" height="7.5" {F}/><rect x="43.5" y="15.5" width="10.5" height="7.5" {F}/><rect x="12" y="23" width="10.5" height="7.5" {F}/><rect x="33" y="23" width="10.5" height="7.5" {F}/><rect x="22.5" y="30.5" width="10.5" height="7.5" {F}/><rect x="43.5" y="30.5" width="10.5" height="7.5" {F}/>'),
 'Tenis': g(f'<ellipse cx="26" cy="24" rx="16" ry="18" transform="rotate(-35 26 24)"/><path d="M16 14 L36 34 M12 24 L28 40 M22 8 L40 26 M14 32 L36 12 M20 38 L40 18" stroke-width="2"/><path d="M36 38 L54 58"/><circle cx="52" cy="14" r="6" {F}/>'),
 'Cine': g(f'<path d="M8 26 H56 V56 H8 Z"/><path d="M8 26 L6 14 L54 6 L56 18 Z"/><path d="M18 12 L24 22 M30 10 L36 20 M42 8 L48 18" stroke-width="3.5"/><path d="M20 38 H44 M20 46 H36"/>'),
 'Música': g(f'<path d="M24 48 V12 L54 6 V40"/><path d="M24 20 L54 14"/><ellipse cx="16" cy="48" rx="9" ry="7" {F}/><ellipse cx="46" cy="40" rx="9" ry="7" {F}/>'),
 'Televisión y series': g(f'<rect x="6" y="20" width="52" height="36" rx="4"/><path d="M22 6 L32 18 L44 4"/><rect x="14" y="28" width="28" height="20" {F}/><circle cx="50" cy="32" r="2.5" {F}/><circle cx="50" cy="42" r="2.5" {F}/>'),
 'Libros y literatura': g(f'<path d="M32 16 C24 10 14 10 6 12 V54 C14 52 24 52 32 58 C40 52 50 52 58 54 V12 C50 10 40 10 32 16 Z"/><path d="M32 16 V58"/><path d="M38 24 C44 22 48 22 52 23 M38 32 C44 30 48 30 52 31" stroke-width="3"/><path d="M12 20 C18 19 22 19 26 21 L26 40 C22 38 18 38 12 39 Z" {F}/>'),
 'Arte y arquitectura': g(f'<path d="M6 16 L32 4 L58 16 Z" {F}/><path d="M8 16 H56 M8 56 H56 M4 60 H60"/><path d="M14 22 V50 M26 22 V50 M38 22 V50 M50 22 V50"/>'),
 'Gastronomía': g(f'<path d="M16 6 V22 C16 28 26 28 26 22 V6 M21 6 V60"/><path d="M44 60 V6 C52 10 54 22 52 34 H44" {F}/>'),
 'Rediseños': g(f'<path d="M44 6 L58 20 L22 56 L6 58 L8 42 Z"/><path d="M38 12 L52 26"/><path d="M8 42 L22 56" stroke-width="3"/><path d="M6 58 L14 50" stroke-width="6"/><rect x="34" y="44" width="22" height="14" {F}/>'),
 'Tipografía': g(f'<path d="M4 56 L20 10 H24 L40 56"/><path d="M10 40 H34"/><path d="M0 56 H12 M32 56 H44"/><circle cx="51" cy="47" r="8" {F}/><path d="M59 34 V56"/>'),
 'Humor gráfico': g(f'<path d="M8 10 H56 V42 H30 L16 56 V42 H8 Z"/><circle cx="22" cy="26" r="3.5" {F}/><circle cx="32" cy="26" r="3.5" {F}/><circle cx="42" cy="26" r="3.5" {F}/>'),
 'Titulares': g(f'<rect x="6" y="8" width="52" height="48"/><rect x="12" y="14" width="40" height="12" {F}/><path d="M12 34 H52 M12 42 H52 M12 50 H36" stroke-width="3"/>'),
 'Industria y crisis de medios': g(f'<path d="M6 12 H46 V56 H12 C8 56 6 54 6 50 Z"/><path d="M46 22 H56 V50 C56 54 54 56 50 56 H46"/><path d="M12 20 H40" stroke-width="6"/><path d="M14 32 L22 40 L30 34 L38 46"/><path d="M32 46 H38 V40" {F}/>'),
 'Datos y visualización': g(f'<path d="M8 6 V56 H58"/><circle cx="18" cy="44" r="4" {F}/><circle cx="28" cy="34" r="4" {F}/><circle cx="38" cy="38" r="4" {F}/><circle cx="48" cy="18" r="4" {F}/><path d="M14 50 L56 12" stroke-width="2.5" stroke-dasharray="4 5"/>'),
}

def slug(n):
    import unicodedata, re
    s = unicodedata.normalize('NFKD', n.lower())
    return 't-' + re.sub(r'[^a-z0-9]+', '-', ''.join(c for c in s if not unicodedata.combining(c))).strip('-')

def tema_symbols():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">' +
            ''.join(f'<symbol id="{slug(n)}" viewBox="0 0 64 64" overflow="visible">{b}</symbol>' for n, b in TI.items()) + '</svg>')
