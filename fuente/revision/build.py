import json
R='/home/claude/inconsolata-datos/datos/'
I=json.load(open(R+'indice.json'));F=json.load(open(R+'fichas_medios.json'));C=json.load(open(R+'catalogo.json'))
AX=json.load(open(R+'autores_fichas.json'))
med=[]
for i,m in enumerate(I['medios']):
    if m['p']<=0: continue
    f=F.get(m['n'],{})
    med.append({'n':m['n'],'p':m['p'],'av':C['medios'][i].get('av',''),'r':m.get('r',''),
      'ficha':bool(f.get('ficha')),'tipo':f.get('tipo',''),'pais':f.get('pais',''),'cc':f.get('cc',''),'fundacion':f.get('fundacion',''),'cierre':f.get('cierre',''),
      'fundador':f.get('fundador',''),'sede':f.get('sede',''),'director':f.get('director',''),'director_desde':f.get('director_desde',''),'propietario':f.get('propietario',''),'formato':f.get('formato',''),'idioma':f.get('idioma',''),
      'web':f.get('web',''),'x':f.get('x',''),'bsky':f.get('bsky',''),'ig':f.get('ig',''),'wikipedia':f.get('wikipedia',''),'qid':f.get('qid',''),'nota':f.get('nota','')})
med.sort(key=lambda m:-m['p'])
pais_m={m['n']:(F.get(m['n'],{}).get('pais',''),F.get(m['n'],{}).get('cc','')) for m in I['medios']}
aut=[]
for a in I['autores']:
    if a['p']<=0: continue
    x=AX.get(a['n'],{}); md=(a.get('m') or [''])[0]
    aut.append({'n':a['n'],'p':a['p'],'m':a.get('m',[]),'y':a.get('y',[]),'genero':x.get('genero',''),'pais':x.get('pais',''),'cc':x.get('cc',''),
      'pais_s':pais_m.get(md,('',''))[0],'cc_s':pais_m.get(md,('',''))[1],'oficio':x.get('oficio',''),'texto':x.get('texto',''),
      'web':x.get('web',''),'x':x.get('x',''),'bsky':x.get('bsky',''),'ig':x.get('ig',''),'linkedin':x.get('linkedin',''),'otros':x.get('otros','')})
aut.sort(key=lambda a:-a['p'])
tpl=open('tpl.html').read()
open('../out/revision-fichas.html','w').write(tpl.replace('__MED__',json.dumps(med,ensure_ascii=False)).replace('__AUT__',json.dumps(aut,ensure_ascii=False)))
print(len(med),len(aut))
