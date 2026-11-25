# Source of truth for C6 events and trios. Years are astronomical (1 BC = 0, 2 BC = -1).
# Ma dates are stored as years before 2026.
W='https://en.wikipedia.org/wiki/'
def bc(y): return 1-y
NOW=2026
def ma(m): return NOW-m*1e6
E={}
def ev(k,name,when,lo,hi,prec,page,check):
    E[k]=dict(id=k,name=name,when=when,lo=lo,hi=hi,prec=prec,src=(W+page if page else None),check=check)
ev('pyramid','The Great Pyramid of Giza is built','c. 2600 BC',bc(2700),bc(2500),'approx','Great_Pyramid_of_Giza','between 2700 and 2500 BC')
ev('cleo','Cleopatra is born','70 or 69 BC',bc(70),bc(69)+.999,'year','Cleopatra','70/69 BC')
ev('iphone','The first iPhone goes on sale','2007',2007,2007.999,'year','IPhone_(1st_generation)','2007')
ev('trex','Tyrannosaurus rex walks the Earth','68–66 million years ago',ma(70),ma(66),'approx','Tyrannosaurus','69.4 to 66 million')
ev('steg','Stegosaurus walks the Earth','155–145 million years ago',ma(155),ma(145),'approx','Stegosaurus','155')
ev('today','You, reading this','2026',2026,2026.999,'year',None,None)
ev('mammoth','The last woolly mammoths die out','c. 2000 BC (about 4,000 years ago)',bc(2300),bc(1650),'approx','Woolly_mammoth','4,000 years ago')
ev('colosseum','The Colosseum opens in Rome','AD 80',80,80.999,'year','Colosseum','80')
ev('nintendo','Nintendo is founded (as a playing-card maker)','1889',1889,1889.999,'year','Nintendo','1889')
ev('starry','Van Gogh paints The Starry Night','1889',1889,1889.999,'year','The_Starry_Night','1889')
ev('mario','Super Mario Bros. comes out','1985',1985,1985.999,'year','Super_Mario_Bros.','1985')
ev('ott_end','The Ottoman sultanate is abolished','1922',1922,1922.999,'year','Abolition_of_the_Ottoman_sultanate','1922')
ev('ott_start','The Ottoman Empire is founded','c. 1299',1290,1310,'approx','Ottoman_Empire','1299')
ev('willie','Mickey Mouse debuts in Steamboat Willie','1928',1928,1928.999,'year','Steamboat_Willie','1928')
ev('harvard','Harvard is founded','1636',1636,1636.999,'year','Harvard_University','1636')
ev('galileo','Galileo is put on trial by the Inquisition','1633',1633,1633.999,'year','Galileo_affair','1633')
ev('declaration','The US Declaration of Independence is signed','1776',1776,1776.999,'year','United_States_Declaration_of_Independence','1776')
ev('satsuma','The last samurai revolt (Satsuma Rebellion)','1877',1877,1877.999,'year','Satsuma_Rebellion','1877')
ev('phone','Bell patents the telephone','1876',1876,1876.999,'year','Invention_of_the_telephone','1876')
ev('sekigahara','The Battle of Sekigahara','1600',1600,1600.999,'year','Battle_of_Sekigahara','1600')
ev('fax','The fax machine is patented','1843',1843,1843.999,'year','Fax','1843')
ev('alamo','The Battle of the Alamo','1836',1836,1836.999,'year','Battle_of_the_Alamo','1836')
ev('email','The first network email is sent','1971',1971,1971.999,'year','Email','1971')
ev('constantinople','Constantinople falls to the Ottomans','1453',1453,1453.999,'year','Fall_of_Constantinople','1453')
ev('gutenberg','The Gutenberg Bible is printed','c. 1455',1454,1455.999,'approx','Gutenberg_Bible','1455')
ev('romefall','The last Western Roman emperor is deposed','476',476,476.999,'year','Fall_of_the_Western_Roman_Empire','476')
ev('machu','Machu Picchu is built','c. 1450',1420,1470,'approx','Machu_Picchu','1450')
ev('columbus','Columbus reaches the Americas','1492',1492,1492.999,'year','Voyages_of_Christopher_Columbus','1492')
ev('pompeii','Vesuvius buries Pompeii','AD 79',79,79.999,'year','Eruption_of_Mount_Vesuvius_in_79_AD','79')
ev('caesar','Julius Caesar is assassinated','44 BC',bc(44),bc(44)+.999,'year','Assassination_of_Julius_Caesar','44 BC')
ev('vikings','Vikings are cutting wood in Newfoundland','1021',1021,1021.999,'year',"L%27Anse_aux_Meadows",'1021')
ev('hastings','The Battle of Hastings','1066',1066,1066.999,'year','Battle_of_Hastings','1066')
ev('guillotine',"France's last execution by guillotine",'1977',1977,1977.999,'year','Guillotine','1977')
ev('starwars','Star Wars opens in cinemas','1977',1977,1977.999,'year','Star_Wars_(film)','1977')
ev('bastille','The storming of the Bastille','1789',1789,1789.999,'year','Storming_of_the_Bastille','1789')
ev('antarctica','People first see Antarctica','1820',1820,1820.999,'year','Antarctica','1820')
ev('battery','Volta builds the first battery','1799–1800',1799,1800.999,'year','Voltaic_pile','1800, Volta stacked')
ev('magellan',"Magellan's crew finishes the first trip around the world",'1522',1522,1522.999,'year','Magellan_expedition','1522')
ev('taj','Work begins on the Taj Mahal','1632',1632,1632.999,'year','Taj_Mahal','1632')
ev('mayflower','The Mayflower lands at Plymouth','1620',1620,1620.999,'year','Mayflower','1620')
ev('sharks','The earliest shark relatives swim the seas','over 420 million years ago',ma(458),ma(419),'approx','Shark','458–444 million')
ev('trees','The first trees','c. 385 million years ago',ma(395),ma(380),'approx','Wattieza','385')
ev('stonehenge',"Stonehenge's big sarsen circle goes up",'c. 2500 BC',bc(2600),bc(2400),'approx','Stonehenge','2600 BC and 2400 B')
ev('rome','Rome is founded (by tradition)','753 BC',bc(800),bc(700),'approx','Founding_of_Rome','753 BC')
ev('wright','The Wright brothers make the first powered flight','1903',1903,1903.999,'year','Wright_Flyer','1903')
ev('moon','Apollo 11 lands on the Moon','1969',1969,1969.999,'year','Apollo_11','1969')
ev('civilwar','The American Civil War ends','1865',1865,1865.999,'year','American_Civil_War','1865')
ev('gobekli','Göbekli Tepe, the oldest known temple, is built','c. 9500 BC',bc(9500),bc(8000),'approx','G%C3%B6bekli_Tepe','9500')
ev('titanic','The Titanic sinks','1912',1912,1912.999,'year','Titanic','1912')
ev('oreo','The first Oreo cookie is sold','1912',1912,1912.999,'year','Oreo','1912')
ev('gettysburg','The Battle of Gettysburg','1863',1863,1863.999,'year','Battle_of_Gettysburg','1863')
ev('safety','The modern-shape bicycle (the Rover) appears','1885',1885,1885.999,'year','Safety_bicycle','1885')
ev('benz','Benz builds the first car','1885–86',1885,1886.999,'year','Benz_Patent-Motorwagen','1886')
ev('loco','The first steam railway locomotive runs','1804',1804,1804.999,'year','Steam_locomotive','1804')
ev('uranus','Uranus is discovered','1781',1781,1781.999,'year','Uranus','1781')
ev('neptune','Neptune is discovered','1846',1846,1846.999,'year','Discovery_of_Neptune','1846')
ev('pluto','Pluto is discovered','1930',1930,1930.999,'year','Pluto','1930')
ev('tv','Television is first shown to the public','1926',1926,1926.999,'year','John_Logie_Baird','1926')
ev('sliced','Sliced bread is first sold','1928',1928,1928.999,'year','Sliced_bread','1928')
ev('hero','Hero of Alexandria describes a coin-operated vending machine','1st century AD',10,85,'century','Vending_machine','1st century AD')
ev('vending','The first modern coin vending machines appear in London','early 1880s',1880,1885,'approx','Vending_machine','1880s')
ev('antikythera','The Antikythera mechanism (an ancient Greek analog computer) is made','c. 150–100 BC',bc(205),bc(60),'approx','Antikythera_mechanism','BC')
ev('eniac','ENIAC, the first general-purpose electronic computer, is finished','1945',1945,1946.999,'year','ENIAC','1945')
ev('moai','The Easter Island statues (moai) are carved','c. 1250–1500',1250,1500,'approx','Moai','1250')
ev('notredame','The first stone of Notre-Dame de Paris is laid','1163',1163,1163.999,'year','Notre-Dame_de_Paris','1163')
ev('terracotta',"China's Terracotta Army is made",'c. 246–208 BC',bc(246),bc(208),'approx','Terracotta_Army','210')
ev('nokia','Nokia starts out as a paper mill','1865',1865,1865.999,'year','Nokia','1865')
ev('lincoln','Abraham Lincoln is assassinated','1865',1865,1865.999,'year','Assassination_of_Abraham_Lincoln','1865')
ev('mobile','The first handheld mobile phone call','1973',1973,1973.999,'year','Mobile_phone','1973')
ev('kongo','Kongo Gumi, a Japanese temple-building firm, is founded','6th century AD',500,600.999,'century','Kong%C5%8D_Gumi','6th century')
ev('oxford','Teaching begins at Oxford','1096 (by 1167 at the latest)',1096,1167,'approx','University_of_Oxford','1096')
ev('salem','The Salem witch trials','1692',1692,1693.4,'year','Salem_witch_trials','1692')
ev('boe','The Bank of England opens','1694',1694,1694.999,'year','Bank_of_England','1694')
ev('armada','The Spanish Armada sails against England','1588',1588,1588.999,'year','Spanish_Armada','1588')
ev('megalodon','Megalodon goes extinct','c. 3.6 million years ago',ma(3.7),ma(2.6),'approx','Megalodon','3.6')
ev('lucy','Lucy, an early human ancestor, lives in Ethiopia','3.2 million years ago',ma(3.25),ma(3.15),'approx','Lucy_(Australopithecus)','3.2 million')
ev('glasses','Eyeglasses are invented in Italy','c. 1290',1280,1300,'approx','Glasses','by about 1290')
ev('magna','Magna Carta is sealed','1215',1215,1215.999,'year','Magna_Carta','1215')
ev('toilet','The first flush toilet is built in England','1596',1596,1596.999,'year','Flush_toilet','1596')
ev('hamlet','Shakespeare writes Hamlet','c. 1600',1599,1601.999,'approx','Hamlet','1601')
ev('dodo','The last confirmed dodo sighting','1662',1662,1662.999,'year','Dodo','1662')
ev('basketball','Basketball is invented','1891',1891,1891.999,'year','Basketball','1891')
ev('okcorral','The Gunfight at the O.K. Corral','1881',1881,1881.999,'year','Gunfight_at_the_O.K._Corral','1881')
ev('nba','The first season of what became the NBA','1946',1946,1946.999,'year','1946%E2%80%9347_BAA_season','1946')
ev('tenoch','The Aztecs found their capital, Tenochtitlan','1325',1325,1325.999,'year','Tenochtitlan','1325')
ev('concorde','Concorde starts carrying passengers','1976',1976,1976.999,'year','Concorde','1976')
ev('viking1','Viking 1 lands on Mars','1976',1976,1976.999,'year','Viking_1','1976')
ev('smallpox','Smallpox is declared wiped out','1980',1980,1980.999,'year','Smallpox','1980')
ev('pacman','Pac-Man comes out','1980',1980,1980.999,'year','Pac-Man','1980')
ev('vaccine','The first vaccine (for smallpox)','1796',1796,1796.999,'year','Smallpox_vaccine','1796')
ev('cun_last','The last known cuneiform tablet is written','AD 75–80',75,80.999,'approx','Cuneiform','dates to 75 AD')
ev('cun_first','Cuneiform writing begins in Sumer','c. 3300 BC',bc(3500),bc(3100),'approx','Cuneiform','c. 3300 BC')
ev('methuselah','Methuselah, a bristlecone pine still alive today, sprouts','c. 2833 BC',bc(2900),bc(2800),'approx','Methuselah_(pine_tree)','4,858-year-old')
ev('hawaii','Hawaii becomes the 50th US state','1959',1959,1959.999,'year','Hawaii_Admission_Act','1959')
ev('barbie','Barbie goes on sale','1959',1959,1959.999,'year','Barbie','1959')
ev('alaska','The US buys Alaska from Russia','1867',1867,1867.999,'year','Alaska_Purchase','1867')
ev('thylacine','The last known Tasmanian tiger dies','1936',1936,1936.999,'year','Thylacine','1936')
ev('everest','First people on top of Everest','1953',1953,1953.999,'year','1953_British_Mount_Everest_expedition','1953')
ev('dna','The shape of DNA (the double helix) is published','1953',1953,1953.999,'year','Nucleic_acid_double_helix','1953')
ev('origin',"Darwin publishes On the Origin of Species",'1859',1859,1859.999,'year','On_the_Origin_of_Species','1859')

# (a, b, c, hook). The hook states the fact the reveal teaches.
T=[
('cleo','pyramid','iphone','Cleopatra lived closer in time to the iPhone than to the building of the Great Pyramid.'),
('trex','steg','today','T. rex is closer in time to you than to Stegosaurus.'),
('mammoth','pyramid','colosseum','Woolly mammoths were still alive when the Great Pyramid went up.'),
('nintendo','starry','mario','Nintendo is as old as The Starry Night.'),
('ott_end','ott_start','willie','The Ottoman Empire was still around 6 years before Mickey Mouse.'),
('harvard','galileo','declaration','Harvard was founded 3 years after Galileo was put on trial.'),
('satsuma','phone','sekigahara','Samurai were still fighting a year after the telephone was patented.'),
('fax','alamo','email','The fax machine is 7 years younger than the Alamo.'),
('constantinople','gutenberg','romefall','The Roman Empire (its eastern half) lasted until the age of the printing press.'),
('machu','columbus','colosseum','Machu Picchu was only about 40 years old when Columbus sailed.'),
('pompeii','colosseum','caesar','The Colosseum opened one year after Pompeii was buried.'),
('vikings','hastings','columbus','Vikings were in America 471 years before Columbus.'),
('guillotine','starwars','bastille','France still used the guillotine the year Star Wars came out.'),
('antarctica','battery','magellan','People had batteries before anyone had seen Antarctica.'),
('taj','mayflower','machu','The Taj Mahal is younger than the Mayflower landing.'),
('sharks','trees','trex','The shark family tree is older than trees.'),
('stonehenge','pyramid','rome','Stonehenge and the Great Pyramid went up at about the same time.'),
('wright','moon','civilwar','The first powered flight is closer to the Civil War than to the Moon landing.'),
('gobekli','pyramid','today','The Great Pyramid is closer to us than to Göbekli Tepe.'),
('titanic','oreo','gettysburg','Oreos and the Titanic are the same age.'),
('safety','benz','loco','The modern bicycle and the car showed up within a year of each other.'),
('uranus','neptune','pluto','Neptune was found closer to Uranus than to Pluto.'),
('tv','sliced','wright','Television is older than sliced bread.'),
('hero','vending','pyramid','There was a coin-operated vending machine in Roman Egypt.'),
('antikythera','eniac','pyramid','An ancient Greek computer is closer to ENIAC than to the Great Pyramid.'),
('moai','notredame','stonehenge','The Easter Island statues were carved after work began on Notre-Dame.'),
('terracotta','pyramid','moon',"China's Terracotta Army is closer in time to the Moon landing than to the Great Pyramid."),
('nokia','lincoln','mobile','Nokia started out the year Lincoln was shot.'),
('kongo','romefall','oxford','A Japanese building firm was founded in the century after the fall of Rome, five centuries before Oxford.'),
('salem','boe','armada','The Salem witch trials ended a year before the Bank of England opened.'),
('megalodon','lucy','trex','Megalodon and our ancestor Lucy are close in time.'),
('glasses','magna','gutenberg','Eyeglasses are more than 150 years older than the printing press.'),
('toilet','hamlet','constantinople','The flush toilet is a few years older than Hamlet.'),
('dodo','moon','mammoth','The dodo is closer in time to the Moon landing than to the woolly mammoth.'),
('basketball','okcorral','nba','Basketball was invented 10 years after the O.K. Corral gunfight.'),
('oxford','hastings','tenoch','Oxford was teaching more than 150 years before the Aztecs founded Tenochtitlan.'),
('concorde','viking1','wright','Concorde started flying passengers the year a probe first landed on Mars.'),
('smallpox','pacman','vaccine','Smallpox was wiped out the year Pac-Man came out.'),
('cun_last','cun_first','today','The last cuneiform tablet is closer to us than to the first.'),
('methuselah','pyramid','rome','A tree alive today is older than the Great Pyramid.'),
('hawaii','barbie','alaska','Barbie is as old as the 50-state United States.'),
('thylacine','moon','dodo','The last Tasmanian tiger died 33 years before the Moon landing.'),
('everest','dna','origin','People first stood on Everest the year DNA\'s shape was published.'),
]
