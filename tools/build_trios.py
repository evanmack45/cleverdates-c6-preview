# Validates every trio and writes ../trios.json. Exits non-zero on any failure.
import json,sys,urllib.parse,random
import events, events2
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
ansfirst=sum(1 for t in out if set(t['answer'])=={t['e'][0],t['e'][1]})
MAX_ANCHOR=4
MIN_TRIOS=100
ERAS=[('Deep prehistory (before 10,000 BC)',-1e12,-9999),('10,000 BC to 500 BC',-9999,-499),('500 BC to AD 500',-499,500),('AD 500 to 1500',500,1500),('1500 to 1799',1500,1800),('1800 to 1899',1800,1900),('1900 to now',1900,1e9)]
def era(e):
    m=mid(e)
    for n,lo,hi in ERAS:
        if lo<=m<hi: return n
    raise SystemExit('no era')
REGIONS=['Africa','Asia','Middle East','Latin America','Oceania','Europe','North America','Global']
cnt=Counter(i for t in out for i in t['e'])
for k,n in cnt.items():
    if n>MAX_ANCHOR: bad.append(f'anchor {k} appears in {n} trios (max {MAX_ANCHOR})')
for k in cnt:
    if not E[k].get('region') in REGIONS: bad.append(f'{k} has no region')
if len(out)<MIN_TRIOS: bad.append(f'only {len(out)} trios (need {MIN_TRIOS})')
era_slots=Counter(era(E[i]) for t in out for i in t['e'])
era_trios={n:sum(1 for t in out if any(era(E[i])==n for i in t['e'])) for n,_,_ in ERAS}
reg_slots=Counter(E[i]['region'] for t in out for i in t['e'])
reg_trios={r:sum(1 for t in out if any(E[i]['region']==r for i in t['e'])) for r in REGIONS}
for r in ['Africa','Asia','Middle East','Latin America','Oceania']:
    if reg_trios[r]<10: bad.append(f'region {r} touches only {reg_trios[r]} trios (need 10)')
for n,_,_ in ERAS:
    if era_trios[n]<10: bad.append(f'era {n!r} touches only {era_trios[n]} trios (need 10)')
slots=sum(reg_slots.values()); west=(reg_slots['Europe']+reg_slots['North America'])/slots
if west>0.5: bad.append(f'Europe + North America are {west:.0%} of event slots (max 50%)')
if bad:
    print('\n'.join(bad)); sys.exit(1)
ev={k:{x:E[k][x] for x in ('name','when','lo','hi','prec','src','region')} for k in sorted(cnt)}
cov=dict(maxAnchorRepeat=max(cnt.values()),eraSlots=dict(era_slots),eraTrios=era_trios,regionSlots=dict(reg_slots),regionTrios=reg_trios,westShare=round(west,3))
json.dump(dict(meta=dict(count=len(out),note='Years are astronomical (1 BC = 0). lo/hi bound each date; every answer holds at the worst case inside those bounds (margin = smallest other-pair gap minus largest answer-pair gap, in years). Built by tools/build_trios.py from tools/events.py and events2.py; every source page was fetched on 2026-11-25 and checked to contain the stated date. Rules enforced: 100+ trios, no event in more than 4 trios, every region and era covered.',checked='2026-11-25',coverage=cov),events=ev,trios=out),open('../trios.json','w'),ensure_ascii=False,indent=1)
print(f'OK {len(out)} trios, {len(ev)} events; tightest margins:',sorted((t['margin'],t['n']) for t in out)[:6])
print('max anchor repeat',cov['maxAnchorRepeat'],cnt.most_common(5)); print('west share',cov['westShare']); print('era trios',era_trios); print('region trios',reg_trios); print('answer = first two shown:',ansfirst)
