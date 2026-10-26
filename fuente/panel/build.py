import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-claude/b753561d-def2-5a8d-ab88-1423c0df1d75/scratchpad/gen')
from temas_iconos import tema_symbols, TI
D = '/tmp/claude-0/-home-claude/b753561d-def2-5a8d-ab88-1423c0df1d75/scratchpad/panel/'
t = open(D + 'tpl.html').read().replace('__SPRITE__', tema_symbols()).replace('__ICONOS__', json.dumps(list(TI), ensure_ascii=False))
open(sys.argv[1], 'w').write(t)
print('ok', len(t))
