# Validates every trio and writes ../trios.json. Exits non-zero on any failure.
import json,sys,urllib.parse,random
from events import E,T
def gap(a,b):
    lo=max(0,a['lo']-b['hi'],b['lo']-a['hi']); hi=max(a['hi']-b['lo'],b['hi']-a['lo']); return lo,hi
def mid(e): return (e['lo']+e['hi'])/2
bad=[];out=[];used=set()
for i,(a,b,c,hook) in enumerate(T):
    ids=[a,b,c]
    for k in ids:
        if k not in E: bad.append(f'{i}: unknown {k}'); continue
        e=E[k]
        if e['src']:
            t=urllib.parse.unquote(e['src'].rsplit('/wiki/',1)[1])
            txt=open('cache/'+urllib.parse.quote(t,safe='')+'.txt').read()
            if e['check'] not in txt: bad.append(f'{i}: {k} source text lacks {e["check"]!r}')
        elif k!='today': bad.append(f'{i}: {k} has no source')
        if not e['lo']<=e['hi']: bad.append(f'{i}: {k} lo>hi')
    if len(set(ids))<3: bad.append(f'{i}: repeat'); continue
    pairs=[(0,1),(0,2),(1,2)]
    g={p:gap(E[ids[p[0]]],E[ids[p[1]]]) for p in pairs}
    best=min(pairs,key=lambda p:abs(mid(E[ids[p[0]]])-mid(E[ids[p[1]]])))
    others=[p for p in pairs if p!=best]
    margin=min(g[p][0] for p in others)-g[best][1]
    if margin<=0: bad.append(f'{i}: {ids} ambiguous: answer max gap {g[best][1]:.0f} vs other min {min(g[p][0] for p in others):.0f}')
    key=frozenset(ids)
    if key in used: bad.append(f'{i}: duplicate trio')
    used.add(key)
    # display order: seeded shuffle so the answer pair is not always first
    order=ids[:]; random.Random(1000+i).shuffle(order)
    ans=sorted([ids[best[0]],ids[best[1]]],key=order.index)
    out.append(dict(n=i+1,e=order,answer=ans,hook=hook,
        gaps={f'{ids[p[0]]}-{ids[p[1]]}':[round(g[p][0]),round(g[p][1])] for p in pairs},margin=round(margin)))
from collections import Counter
cnt=Counter(i for t in out for i in t['e'])
ansfirst=sum(1 for t in out if set(t['answer'])=={t['e'][0],t['e'][1]})
if bad:
    print('\n'.join(bad)); sys.exit(1)
ev={k:{x:E[k][x] for x in ('name','when','lo','hi','prec','src')} for k in sorted(cnt)}
json.dump(dict(meta=dict(count=len(out),note='Years are astronomical (1 BC = 0). lo/hi bound each date; every answer holds at the worst case inside those bounds (margin = smallest other-pair gap minus largest answer-pair gap, in years). Built by tools/build_trios.py from tools/events.py; every source page was fetched on 2026-11-25 and checked to contain the stated date.',checked='2026-11-25'),events=ev,trios=out),open('../trios.json','w'),ensure_ascii=False,indent=1)
print(f'OK {len(out)} trios, {len(ev)} events; tightest margins:',sorted((t['margin'],t['n']) for t in out)[:5]); print('most used:',cnt.most_common(4),'answer = first two shown:',ansfirst)
