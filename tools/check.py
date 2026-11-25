import urllib.parse,re
import events, events2
from events import E
for k,e in E.items():
    if not e['src']: continue
    t=urllib.parse.unquote(e['src'].rsplit('/wiki/',1)[1])
    s=open('cache/'+urllib.parse.quote(t,safe='')+'.txt').read()
    i=s.find(e['check'])
    if i<0: print('FAIL',k,e['check']); continue
    print(f"{k:12} | {s[max(0,i-110):i+70]!r}"[:230])
