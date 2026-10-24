"""Logos, avatares y datos de ficha de cada medio. Si algo no existe, la web no muestra su hueco."""
import json, os
_D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
FM = json.load(open(os.path.join(_D, 'fichas_medios.json')))
AS = json.load(open(os.path.join(_D, 'assets.json')))
FICHAS_HECHAS = {'El País': 'ficha-medio-el-pais.html', 'The New York Times': 'ficha-medio-nyt.html', 'Libération': 'ficha-medio-liberation.html'}
FLAG = 'https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/flags/4x3/{}.svg'

def info(n):
    return FM.get(n, {})

def logo(n, width=400):
    L = AS.get('logos', {})
    if n in L or _fam(n) in L:
        return L.get(n) or L[_fam(n)]
    u = info(n).get('logo_url', '')
    return f'{u}?width={width}' if u else ''

import re as _re
def _fam(n):
    """Ediciones de una misma cabecera (… USA, … UK) comparten avatar y logo propio."""
    return _re.sub(r'\s+(USA|UK)$', '', n)

def avatar(n):
    A = AS.get('avatares', {})
    return A.get(n) or A.get(_fam(n), '')

def tiene_ficha(n):
    return bool(info(n).get('ficha'))

def ficha_href(n, buscador_idx=None):
    if n in FICHAS_HECHAS:
        return FICHAS_HECHAS[n]
    if tiene_ficha(n):
        return '#'                      # en la web real: la página de ficha con ?m=slug
    return f'inconsolata-buscador.html#m={buscador_idx}' if buscador_idx is not None else '#'

def avatar_barra(n):
    """Versión para la barra negra del final del post: silueta blanca, salvo los que tienen fondo de color."""
    B = AS.get('avatar_blanco', {})
    return B.get(n) or B.get(_fam(n)) or avatar(n)
