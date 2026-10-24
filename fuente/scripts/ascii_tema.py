import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
def js(t): return ''.join(c if ord(c) < 128 else ''.join('\\u%04x' % u for u in [ord(c)] if ord(c) < 0x10000) or c.encode('utf-16-be').hex() for c in t)
def jsx(t):
    o=[]
    for c in t:
        if ord(c)<128: o.append(c)
        else:
            b=c.encode('utf-16-be'); o+=['\\u'+b[i:i+2].hex() for i in range(0,len(b),2)]
    return ''.join(o)
def css(t): return ''.join(c if ord(c) < 128 else '\\%x ' % ord(c) for c in t)
def htm(t): return ''.join(c if ord(c) < 128 else '&#x%x;' % ord(c) for c in t)
out, i = [], 0
for m in re.finditer(r'(<script\b[^>]*>)(.*?)(</script>)|(<style\b[^>]*>)(.*?)(</style>)', s, re.S):
    out.append(htm(s[i:m.start()]))
    if m.group(1): out.append(m.group(1) + jsx(m.group(2)) + m.group(3))
    else: out.append(m.group(4) + css(m.group(5)) + m.group(6))
    i = m.end()
out.append(htm(s[i:]))
r = ''.join(out); assert r.isascii()
open(sys.argv[2], 'w', encoding='ascii').write(r)
