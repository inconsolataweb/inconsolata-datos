import sys, json, os
R = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(R, '..', 'gen'))
from temas_iconos import tema_symbols, TI
t = open(os.path.join(R, 'tpl.html')).read().replace('__SPRITE__', tema_symbols()).replace('__ICONOS__', json.dumps(list(TI), ensure_ascii=False))
open(sys.argv[1], 'w').write(t)
print('ok', len(t))
