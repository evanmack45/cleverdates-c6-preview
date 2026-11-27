# Tile pictogram kind for each event (scan-preview). Hand-assigned; build.mjs fails if an event has no kind.
import json
K = {
 'build': 'abusimbel angkor borobudur caral colosseum forbidden gobekli hagia lalibela literature machu mohenjo notredame olmec pantheon parthenon persepolis pyramid stonehenge taj tenoch moai terracotta harvard oxford qaraw kongo rome',
 'battle': 'adwa alamo armada baghdad bastille civilwar constantinople hastings isandlwana panipat sekigahara waterloo tenochfall satsuma hannibal romefall guillotine blackdeath',
 'crown': 'alexander ashoka caesar charl cleo confucius cyrus genghis kush mansa napoleon ott_end ott_start qin qing tang republic inca hijra galileo',
 'flag': 'declaration ghana haiti india zimbabwe magna nzvote waitangi uluru domesday',
 'life': 'cockroach dodo elephantbird irhoud lucy mammoth megalodon methuselah moa quagga sahel sharks smilodon steg thylacine trees trex otzi madj',
 'make': 'antikythera battery bulb eniac glasses hero loco mobile phone tv vending wright concorde shinkansen sliced oreo pennyblack iphone',
 'write': 'cailun canon cun_first cun_last dss genji gutenberg hamlet hangul jikji khwarizmi oracle origin rosetta ishango chauvet lascaux greatwave starry jomon tomb',
 'ship': 'antarctica beagle columbus cook magellan mayflower nz vikings zhenghe everest panama suez',
 'space': 'bigbang earth moon sputnik dna smallpox',
 'fire': 'glacier krakatoa pompeii tambora titanic',
 'play': 'mario nintendo olymp776 olympics96 pacman starwars willie',
 'you': 'today',
}
kind = {}
for k, ids in K.items():
  for i in ids.split():
    assert i not in kind, i
    kind[i] = k
ev = json.load(open('trios.json'))['events']
missing = [i for i in ev if i not in kind]; extra = [i for i in kind if i not in ev]
assert not missing and not extra, (missing, extra)
json.dump(kind, open('kinds.json', 'w'), indent=0, sort_keys=True)
print(len(kind), 'kinds', {k: len(v.split()) for k, v in K.items()})
