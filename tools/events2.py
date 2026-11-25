# Second batch of events and trios, plus regions for every event. Import after events.py.
from events import E,T,ev,bc,ma,NOW
def ya(n): return NOW-n
AF,AS,ME,LA,OC,EU,NA,GL='Africa','Asia','Middle East','Latin America','Oceania','Europe','North America','Global'
REG=dict(pyramid=AF,cleo=AF,iphone=NA,trex=GL,steg=GL,today=GL,mammoth=GL,colosseum=EU,nintendo=AS,starry=EU,mario=AS,ott_end=ME,ott_start=ME,willie=NA,harvard=NA,galileo=EU,declaration=NA,satsuma=AS,phone=NA,sekigahara=AS,fax=EU,alamo=NA,email=NA,constantinople=ME,gutenberg=EU,romefall=EU,machu=LA,columbus=LA,pompeii=EU,caesar=EU,vikings=NA,hastings=EU,guillotine=EU,starwars=NA,bastille=EU,antarctica=GL,battery=EU,magellan=GL,taj=AS,mayflower=NA,sharks=GL,trees=GL,stonehenge=EU,rome=EU,wright=NA,moon=NA,civilwar=NA,gobekli=ME,titanic=EU,oreo=NA,gettysburg=NA,safety=EU,benz=EU,loco=EU,uranus=EU,neptune=EU,pluto=NA,tv=EU,sliced=NA,hero=AF,vending=EU,antikythera=EU,eniac=NA,moai=OC,notredame=EU,terracotta=AS,nokia=EU,lincoln=NA,mobile=NA,kongo=AS,oxford=EU,salem=NA,boe=EU,armada=EU,megalodon=GL,lucy=AF,glasses=EU,magna=EU,toilet=EU,hamlet=EU,dodo=AF,basketball=NA,okcorral=NA,nba=NA,tenoch=LA,concorde=EU,viking1=GL,smallpox=GL,pacman=AS,vaccine=EU,cun_last=ME,cun_first=ME,methuselah=NA,hawaii=NA,barbie=NA,alaska=NA,thylacine=OC,everest=AS,dna=EU,origin=EU)
for k,r in REG.items(): E[k]['region']=r

# ---- Africa ----
ev('mansa','Mansa Musa of Mali makes his pilgrimage to Mecca','1324',1324,1325.999,'year','Mansa_Musa','1324',AF)
ev('lalibela','The rock-hewn churches of Lalibela are carved','during the reign of King Lalibela, c. 1181–1221',1181,1221,'approx','Lalibela','1181–1221',AF)
ev('genghis','Genghis Khan is proclaimed ruler of the Mongols','1206',1206,1206.999,'year','Genghis_Khan','1206',AS)
ev('qaraw','The University of al-Qarawiyyin opens in Fez','859',859,859.999,'year','University_of_al-Qarawiyyin','859',AF)
ev('charl','Charlemagne is crowned emperor in Rome','800',800,800.999,'year','Charlemagne','800',EU)
ev('tomb',"Tutankhamun's tomb is found",'1922',1922,1922.999,'year','Tutankhamun','1922',AF)
ev('suez','The Suez Canal opens','1869',1869,1869.999,'year','Suez_Canal','1869',AF)
ev('periodic','Mendeleev publishes his periodic table','1869',1869,1869.999,'year','Periodic_table','1869',EU)
ev('adwa','Ethiopia beats Italy at the Battle of Adwa','1896',1896,1896.999,'year','Battle_of_Adwa','1896',AF)
ev('olympics96','The first modern Olympic Games open in Athens','1896',1896,1896.999,'year','1896_Summer_Olympics','1896',EU)
ev('ghana','Ghana becomes independent','1957',1957,1957.999,'year','Ghana','1957',AF)
ev('sputnik','Sputnik 1 is launched','1957',1957,1957.999,'year','Sputnik_1','1957',GL)
ev('kili','The first recorded climb of Mount Kilimanjaro','1889',1889,1889.999,'year','Mount_Kilimanjaro','1889',AF)
ev('ishango','The Ishango bone, a tally stick, is carved in Central Africa','c. 20,000–18,000 BC',bc(20000),bc(18000),'approx','Ishango_bone','18,000 BCE and 20,000 BCE',AF)
ev('irhoud','The oldest known Homo sapiens fossils (Jebel Irhoud, Morocco)','c. 300,000 years ago',ya(315000),ya(285000),'approx','Jebel_Irhoud','300,000',AF)
ev('quagga','The last quagga dies in a zoo in Amsterdam','1883',1883,1883.999,'year','Quagga','1883',AF)
ev('krakatoa','Krakatoa erupts','1883',1883,1883.999,'year','1883_eruption_of_Krakatoa','1883',AS)
ev('isandlwana','The Zulu army wins the Battle of Isandlwana','1879',1879,1879.999,'year','Battle_of_Isandlwana','1879',AF)
ev('bulb',"Edison's carbon-filament bulb first burns for 13.5 hours",'1879',1879,1879.999,'year','Incandescent_light_bulb','22 October 1879',NA)
ev('elephantbird','The last elephant birds die out in Madagascar','c. 1000',900,1200,'approx','Elephant_bird','1000',AF)
ev('abusimbel','The Abu Simbel temples are built for Ramesses II','c. 1264–1244 BC',bc(1264),bc(1244),'approx','Abu_Simbel_temples','1264 BC',AF)
ev('kush','Kings from Kush (Sudan) begin ruling Egypt','744 BC',bc(750),bc(738),'approx','Twenty-fifth_Dynasty_of_Egypt','744 to 656 BC',AF)
# ---- Middle East ----
ev('persepolis','Darius I begins building Persepolis','c. 518 BC',bc(520),bc(515),'approx','Persepolis','518 BC',ME)
ev('republic','Rome becomes a republic','509 BC',bc(510),bc(508)+.999,'year','Roman_Republic','509 BC',EU)
ev('cyrus','Cyrus the Great takes Babylon','539 BC',bc(539),bc(539)+.999,'year','Cyrus_the_Great','539 BC',ME)
ev('canon','Avicenna finishes The Canon of Medicine','1025',1025,1025.999,'year','The_Canon_of_Medicine','1025',ME)
ev('khwarizmi','Al-Khwarizmi writes the book that gives us the word "algebra"','c. 820',813,833,'approx','The_Compendious_Book_on_Calculation_by_Completion_and_Balancing','820',ME)
# ---- Asia ----
ev('jikji','Korea prints Jikji, the oldest surviving book printed with movable metal type','1377',1377,1377.999,'year','Jikji','1377',AS)
ev('domesday','The Domesday Book is compiled in England','1086',1086,1086.999,'year','Domesday_Book','1086',EU)
ev('hangul','King Sejong creates Hangul, the Korean alphabet','1443–1446',1443,1446.999,'year','Hangul','1443',AS)
ev('inca','The Inca Empire begins to expand','1438',1438,1438.999,'year','Inca_Empire','1438',LA)
ev('zhenghe',"Zheng He's first treasure fleet sails",'1405',1405,1405.999,'year','Zheng_He','1405',AS)
ev('forbidden','The Forbidden City is completed in Beijing','1420',1420,1420.999,'year','Forbidden_City','1420',AS)
ev('angkor','Angkor Wat is built in Cambodia','c. 1113–1150',1113,1150.999,'approx','Angkor_Wat','1113',AS)
ev('genji','Murasaki Shikibu writes The Tale of Genji','early 11th century',1000,1021,'approx','The_Tale_of_Genji','11th century',AS)
ev('confucius','Confucius is born','551 BC',bc(552),bc(551)+.999,'year','Confucius','551 BC',AS)
ev('parthenon','Work begins on the Parthenon','447 BC',bc(447),bc(447)+.999,'year','Parthenon','447 BC',EU)
ev('qin','Qin Shi Huang unifies China','221 BC',bc(221),bc(221)+.999,'year','Qin_Shi_Huang','221 BC',AS)
ev('hannibal','Hannibal sets out from Spain to invade Italy','218 BC',bc(218),bc(218)+.999,'year','Hannibal','late spring of 218 BC',EU)
ev('cailun','Cai Lun reports the invention of paper to the Chinese emperor','105',105,105.999,'year','Cai_Lun','105',AS)
ev('mohenjo','Mohenjo-daro is a thriving city in the Indus Valley','c. 2500 BC',bc(2600),bc(2450),'approx','Mohenjo-daro','2500 BC',AS)
ev('borobudur','Borobudur is built on Java','8th–9th century',750,850,'approx','Borobudur','8th century',AS)
ev('literature','The Temple of Literature is founded in Hanoi','1070',1070,1070.999,'year','Temple_of_Literature,_Hanoi','1070',AS)
ev('oracle','The earliest Chinese writing, on oracle bones','c. 1254–1197 BC',bc(1254),bc(1197),'approx','Oracle_bone_script','1254–1197 BC',AS)
ev('meiji','The Meiji Restoration ends the shogunate in Japan','1868',1868,1868.999,'year','Meiji_Restoration','1868',AS)
ev('noodles','Instant noodles are invented in Japan','1958',1958,1958.999,'year','Instant_noodle','1958',AS)
ev('greatwave','Hokusai makes The Great Wave off Kanagawa','1831',1831,1831.999,'year','The_Great_Wave_off_Kanagawa','late 1831',AS)
ev('beagle','HMS Beagle sails with Darwin aboard','1831',1831,1831.999,'year','HMS_Beagle','1831',EU)
ev('tambora','Mount Tambora erupts in Indonesia','1815',1815,1815.999,'year','1815_eruption_of_Mount_Tambora','1815',AS)
ev('waterloo','The Battle of Waterloo','1815',1815,1815.999,'year','Battle_of_Waterloo','1815',EU)
ev('qing','The last emperor of China abdicates','1912',1912,1912.999,'year','Xinhai_Revolution','12 February 1912',AS)
ev('mactan','Magellan is killed in the Philippines','1521',1521,1521.999,'year','Battle_of_Mactan','1521',AS)
ev('jomon','Jōmon potters in Japan make some of the oldest pottery','c. 14,500 BC',bc(15500),bc(13500),'approx','J%C5%8Dmon_pottery','14,500',AS)
# ---- Americas ----
ev('caral','Caral, Peru, is a thriving city','c. 2600–2000 BC',bc(2600),bc(2000),'approx','Caral','2600 BC to 2000 BC',LA)
ev('tenochfall','Tenochtitlan falls to the Spanish','1521',1521,1521.999,'year','Fall_of_Tenochtitlan','1521',LA)
ev('haiti','Haiti declares independence','1804',1804,1804.999,'year','Haitian_Declaration_of_Independence','1804',LA)
ev('panama','The Panama Canal opens','1914',1914,1914.999,'year','Panama_Canal','1914',LA)
ev('brasilia',"Brasília is inaugurated as Brazil's capital",'1960',1960,1960.999,'year','Bras%C3%ADlia','1960',LA)
ev('christ','The Christ the Redeemer statue is dedicated in Rio','1931',1931,1931.999,'year','Christ_the_Redeemer_(statue)','October 12, 1931',LA)
ev('empire','The Empire State Building opens','1931',1931,1931.999,'year','Empire_State_Building','1931',NA)
ev('smilodon','The last saber-toothed cats die out','c. 10,000 years ago',ya(12000),ya(9000),'approx','Smilodon','10,000',NA)
# ---- Oceania ----
ev('nz','Polynesians settle New Zealand','between 1250 and 1300',1250,1300,'approx','History_of_New_Zealand','between 1250 and 1300',OC)
ev('moa','The last moa die out in New Zealand','by 1445',1300,1445.999,'approx','Moa','By 1445 C.E.',OC)
ev('operahouse','The Sydney Opera House opens','1973',1973,1973.999,'year','Sydney_Opera_House','1973',OC)
ev('waitangi','The Treaty of Waitangi is signed in New Zealand','1840',1840,1840.999,'year','Treaty_of_Waitangi','1840',OC)
ev('pennyblack','The Penny Black, the first postage stamp, goes on sale','1840',1840,1840.999,'year','Penny_Black','1840',EU)
ev('firstfleet','The First Fleet reaches Australia','1788',1788,1788.999,'year','First_Fleet','1788',OC)
ev('uluru','Uluru is handed back to its Aboriginal owners','1985',1985,1985.999,'year','Uluru','1985',OC)
ev('madj','People are already living at Madjedbebe, Australia','c. 65,000 years ago',ya(70000),ya(59000),'approx','Madjedbebe','65,000',OC)
ev('hokulea',"The canoe Hōkūle'a sails from Hawaii to Tahiti with no instruments",'1976',1976,1976.999,'year','H%C5%8Dk%C5%ABle%CA%BBa','1976',OC)
# ---- deep time and prehistory ----
ev('chauvet','Painters decorate Chauvet Cave in France','c. 36,000 years ago',ya(37000),ya(28000),'approx','Chauvet_Cave','36,000',EU)
ev('lascaux','Lascaux Cave is painted','c. 22,000–17,000 years ago',ya(22000),ya(17000),'approx','Lascaux','17,000 to 22,000',EU)
ev('glacier','The last ice age ends','c. 11,700 years ago',ya(12000),ya(11500),'approx','Holocene','11,700',GL)
ev('bigbang','The Big Bang','13.8 billion years ago',ma(13900),ma(13700),'approx','Big_Bang','13.787',GL)
ev('earth','Earth forms','4.54 billion years ago',ma(4570),ma(4530),'approx','Age_of_Earth','4.54',GL)
ev('otzi','Ötzi the Iceman dies in the Alps','c. 3300 BC',bc(3359),bc(3105),'approx','%C3%96tzi','between 3359 and 3105 BC',EU)
ev('cockroach','The ancestors of cockroaches appear','c. 320 million years ago',ma(359),ma(299),'approx','Cockroach','320',GL)

ev('zimbabwe','Zimbabwe becomes independent','1980',1980,1980.999,'year','Zimbabwe','1980',AF)
ev('india','India becomes independent','1947',1947,1947.999,'year','Indian_independence_movement','1947',AS)
ev('dss','The Dead Sea Scrolls are first found','1946–1947',1946,1947.999,'year','Dead_Sea_Scrolls','1947',ME)
ev('nzvote','New Zealand women win the right to vote','1893',1893,1893.999,'year','Women%27s_suffrage_in_New_Zealand','1893',OC)
ev('cook',"James Cook's ship reaches the coast of Australia",'1770',1770,1770.999,'year','James_Cook','19 April 1770',OC)
ev('olmec','The Olmec city of San Lorenzo is at its height','c. 1200–900 BC',bc(1200),bc(900),'approx','San_Lorenzo_Tenochtitl%C3%A1n','1200',LA)
ev('sahel','Sahelanthropus, the oldest known fossil on the human line, lives in Chad','c. 7 million years ago',ma(7.5),ma(6.5),'approx','Sahelanthropus','7 million',AF)
ev('ashoka',"Ashoka rules India and carves his edicts",'c. 268–232 BC',bc(268),bc(232),'approx','Edicts_of_Ashoka','Ashoka of the Mauryan Empire who ruled',AS)
ev('rosetta','The Rosetta Stone is carved in Egypt','196 BC',bc(196),bc(196)+.999,'year','Rosetta_Stone','196 BC',AF)
ev('shinkansen',"Japan's first bullet train starts running",'1964',1964,1964.999,'year','Shinkansen','1964',AS)
ev('panipat','Babur wins at Panipat and founds the Mughal Empire','1526',1526,1526.999,'year','First_Battle_of_Panipat','1526',AS)
T+=[
('mansa','tenoch','columbus','Mansa Musa of Mali made his pilgrimage to Mecca within a year of the Aztecs founding Tenochtitlan.'),
('lalibela','genghis','hastings',"The rock churches of Lalibela in Ethiopia were being carved in Genghis Khan's day."),
('qaraw','charl','oxford','A university opened in Fez, Morocco, about 60 years after Charlemagne became emperor.'),
('tomb','ott_end','nintendo',"Tutankhamun's tomb was found the same year the Ottoman sultanate ended."),
('suez','periodic','hawaii','The Suez Canal opened the same year Mendeleev published the periodic table.'),
('adwa','olympics96','dodo','Ethiopia beat Italy at Adwa the same year the modern Olympics began.'),
('ghana','sputnik','pacman','Ghana became independent the same year Sputnik went up.'),
('kili','starry','barbie','Kilimanjaro was first climbed the same year Van Gogh painted The Starry Night.'),
('kush','rome','cun_last','Kings from Kush ruled Egypt about when Rome was supposedly founded.'),
('ishango','lascaux','cun_first','The Ishango bone, a tally stick from Central Africa, is closer in time to the Lascaux paintings than to the first writing.'),
('madj','chauvet','irhoud','People reached Australia closer in time to the Chauvet cave painters than to the oldest known Homo sapiens fossils.'),
('glacier','gobekli','lascaux','Göbekli Tepe was built as the last ice age was ending, thousands of years after Lascaux.'),
('bigbang','earth','today','Earth is closer in time to today than to the Big Bang.'),
('otzi','cun_first','rome','The Iceman died around the time writing was invented in Sumer.'),
('cockroach','trees','steg','Cockroaches are closer in time to the first trees than to Stegosaurus.'),
('jikji','gutenberg','domesday',"Korea printed a book with movable metal type 78 years before Gutenberg's Bible."),
('hangul','inca','notredame','The Inca Empire began expanding in the same decade King Sejong gave Korea its alphabet.'),
('genghis','magna','constantinople','Genghis Khan became ruler of the Mongols 9 years before Magna Carta.'),
('zhenghe','forbidden','magellan',"Zheng He's first treasure fleet sailed 15 years before the Forbidden City was finished."),
('angkor','notredame','hamlet','Angkor Wat and Notre-Dame were built within decades of each other.'),
('canon','genji','domesday','Avicenna finished The Canon of Medicine within about 25 years of the writing of The Tale of Genji.'),
('khwarizmi','charl','magna','The book that gave us the word "algebra" came about 20 years after Charlemagne became emperor.'),
('persepolis','republic','caesar','Persepolis was begun about nine years before Rome became a republic.'),
('confucius','cyrus','parthenon','Confucius was born 12 years before Cyrus took Babylon.'),
('qin','hannibal','cleo','China was unified three years before Hannibal set out to invade Italy.'),
('cailun','colosseum','romefall','Paper was reported to the Chinese emperor 25 years after the Colosseum opened.'),
('mohenjo','stonehenge','parthenon',"Mohenjo-daro's streets and Stonehenge's big stone circle date from the same few centuries."),
('caral','stonehenge','caesar',"Caral in Peru was a thriving city in the era when Stonehenge's big stones went up."),
('tenochfall','mactan','hamlet','Magellan was killed in the Philippines the same year Tenochtitlan fell.'),
('haiti','loco','bastille','Haiti became independent the same year the first steam locomotive ran.'),
('panama','titanic','gettysburg','The Panama Canal opened two years after the Titanic sank.'),
('brasilia','hawaii','sliced','Brazil inaugurated Brasília one year after Hawaii became a state.'),
('meiji','alaska','galileo','Japan\'s shogunate fell the year after the US bought Alaska.'),
('noodles','barbie','tv','Instant noodles were invented one year before Barbie went on sale.'),
('greatwave','beagle','civilwar',"Hokusai made The Great Wave the same year Darwin's Beagle set sail."),
('operahouse','mobile','oreo','The Sydney Opera House opened the same year as the first handheld mobile phone call.'),
('waitangi','pennyblack','magellan',"New Zealand's founding treaty was signed the same year the first postage stamp went on sale."),
('firstfleet','bastille','declaration','The First Fleet reached Australia the year before the Bastille fell.'),
('nz','glasses','hastings','People reached New Zealand about when eyeglasses were invented.'),
('moa','gutenberg','taj','The last moa were gone by about the time Gutenberg printed his Bible.'),
('uluru','mario','eniac','Uluru was handed back to its Aboriginal owners the year Super Mario Bros. came out.'),
('smilodon','gobekli','chauvet','Saber-toothed cats were still around when Göbekli Tepe was built.'),
('elephantbird','vikings','galileo','Elephant birds were dying out in Madagascar about when Vikings reached Newfoundland.'),
('quagga','krakatoa','harvard','The last quagga died the year Krakatoa erupted.'),
('borobudur','charl','magna','Borobudur was built about when Charlemagne became emperor.'),
('qing','titanic','civilwar','The last emperor of China abdicated the year the Titanic sank.'),
('jomon','lascaux','cleo',"Japanese potters were firing pots about when Lascaux was painted, long before Cleopatra's time."),
('hokulea','concorde','boe',"A canoe sailed from Hawaii to Tahiti with no instruments the year Concorde began carrying passengers."),
('christ','empire','smallpox','Christ the Redeemer in Rio was dedicated the same year the Empire State Building opened.'),
('literature','domesday','notredame',"Hanoi's Temple of Literature was founded 16 years before the Domesday Book."),
('abusimbel','oracle','caesar','The Abu Simbel temples were built about when the first Chinese writing appeared on oracle bones.'),
('tambora','waterloo','alamo','Mount Tambora erupted the same year as the Battle of Waterloo.'),
('isandlwana','bulb','armada',"The Zulu army won at Isandlwana the year Edison's bulb first burned for 13 hours."),
('zimbabwe','smallpox','tv','Zimbabwe became independent the year smallpox was declared wiped out.'),
('india','dss','mobile','The Dead Sea Scrolls were first found about the time India won independence.'),
('nzvote','nintendo','phone','New Zealand women won the vote four years after Nintendo was founded.'),
('cook','declaration','harvard',"James Cook's ship reached Australia six years before the US Declaration of Independence."),
('olmec','abusimbel','parthenon','The Olmec city of San Lorenzo was rising while Abu Simbel was being built.'),
('sahel','lucy','irhoud','Lucy lived closer in time to the oldest Homo sapiens than to Sahelanthropus.'),
('ashoka','qin','cleo','Ashoka carved his edicts in India a few decades before China was unified.'),
('rosetta','qin','cailun','The Rosetta Stone was carved a generation after China was unified.'),
('shinkansen','concorde','titanic',"Japan's bullet train began 12 years before Concorde carried passengers."),
('panipat','tenochfall','mayflower','The Mughal Empire began five years after Tenochtitlan fell.'),
]
