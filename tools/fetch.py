import json,os,sys,urllib.parse,urllib.request,time
from events import E
os.makedirs('cache',exist_ok=True)
pages=sorted({e['src'] for e in E.values() if e['src']})
for u in pages:
    t=urllib.parse.unquote(u.rsplit('/wiki/',1)[1])
    f='cache/'+urllib.parse.quote(t,safe='')+'.txt'
    if os.path.exists(f): continue
    q=urllib.parse.urlencode(dict(action='query',prop='extracts',explaintext=1,titles=t,format='json',redirects=1,formatversion=2))
    r=urllib.request.Request('https://en.wikipedia.org/w/api.php?'+q,headers={'User-Agent':'cleverdates-c6-sourcecheck/1.0 (evanmack45 preview)'})
    d=json.load(urllib.request.urlopen(r,timeout=30))
    p=d['query']['pages'][0]
    if p.get('missing'): print('MISSING',u); continue
    open(f,'w').write(p['title']+'\n'+p.get('extract',''))
    time.sleep(0.2)
print('fetched',len(pages))
