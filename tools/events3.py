# Third batch: events added to build long-gap, cross-world trios. Import after events2.py.
from events import E,T,ev,bc,ma,NOW
from events2 import AF,AS,ME,LA,OC,EU,NA,GL,ya
ev('hammurabi','Hammurabi rules Babylon and issues his law code','c. 1792–1750 BC',bc(1792),bc(1750),'approx','Code_of_Hammurabi','from around 1792 to around 1750 BC',ME)
ev('olymp776','The first ancient Olympic Games are held','776 BC',bc(776),bc(776)+.999,'year','Ancient_Olympic_Games','776 BC',EU)
ev('alexander','Alexander the Great dies in Babylon','323 BC',bc(323),bc(323)+.999,'year','Alexander_the_Great','323 BC',ME)
ev('pantheon','The Pantheon in Rome is rebuilt in the form we see today','c. AD 118–128',118,128,'approx','Pantheon,_Rome','AD 126',EU)
ev('hagia','Hagia Sophia is completed in Constantinople','537',537,537.999,'year','Hagia_Sophia','537',ME)
ev('tang','The Tang dynasty is founded in China','618',618,618.999,'year','Tang_dynasty','618',AS)
ev('hijra','Muhammad migrates from Mecca to Medina (the Hijra)','622',622,622.999,'year','Hijrah','622',ME)
ev('baghdad','The Mongols sack Baghdad','1258',1258,1258.999,'year','Siege_of_Baghdad_(1258)','1258',ME)
ev('blackdeath','The Black Death reaches Europe','1347',1347,1347.999,'year','Black_Death','1347',EU)
ev('joan','Joan of Arc is burned at the stake','1431',1431,1431.999,'year','Joan_of_Arc','1431',EU)
ev('monalisa','Leonardo begins painting the Mona Lisa','1503',1503,1503.999,'year','Mona_Lisa','1503',EU)
ev('jamestown','Jamestown, the first lasting English colony in America, is founded','1607',1607,1607.999,'year','Jamestown,_Virginia','1607',NA)
ev('tokugawa','Tokugawa Ieyasu becomes shogun and the Edo period begins','1603',1603,1603.999,'year','Tokugawa_shogunate','1603',AS)
ev('principia','Newton publishes the Principia','1687',1687,1687.999,'year','Philosophi%C3%A6_Naturalis_Principia_Mathematica','1687',EU)
ev('napoleon','Napoleon dies on Saint Helena','1821',1821,1821.999,'year','Napoleon','1821',EU)
ev('sequoyah','Sequoyah completes the Cherokee syllabary','1821',1821,1821.999,'year','Sequoyah','1821',NA)
ev('kamehameha','Kamehameha I unites the Hawaiian Islands','1810',1810,1810.999,'year','Kamehameha_I','1810',OC)
ev('pigeon','Martha, the last passenger pigeon, dies in a zoo','1914',1914,1914.999,'year','Passenger_pigeon','1914',NA)
ev('auk','The last great auks are killed','1844',1844,1844.999,'year','Great_auk','1844',EU)
ev('steller',"Steller's sea cow is hunted to extinction",'by 1768',1765,1768.999,'approx',"Steller%27s_sea_cow",'by 1768',AS)

# Trios dropped in the surprise pass: plain "same year / same decade" coincidences whose pair also FEELS close (no illusion), plus the old Oxford trio.
# Replaced by the NEW trios below, each "X is closer in time to M than to A" (X feels old, M is the nearer, later event, A the older decoy).
DROP=[('mario', 'nintendo', 'starry'), ('declaration', 'galileo', 'harvard'), ('caesar', 'colosseum', 'pompeii'), ('gettysburg', 'oreo', 'titanic'), ('benz', 'loco', 'safety'), ('sliced', 'tv', 'wright'), ('constantinople', 'hamlet', 'toilet'), ('concorde', 'viking1', 'wright'), ('pacman', 'smallpox', 'vaccine'), ('alaska', 'barbie', 'hawaii'), ('hawaii', 'periodic', 'suez'), ('barbie', 'kili', 'starry'), ('hamlet', 'mactan', 'tenochfall'), ('gettysburg', 'panama', 'titanic'), ('brasilia', 'hawaii', 'sliced'), ('alaska', 'galileo', 'meiji'), ('barbie', 'noodles', 'tv'), ('mobile', 'operahouse', 'oreo'), ('bastille', 'declaration', 'firstfleet'), ('boe', 'concorde', 'hokulea'), ('christ', 'empire', 'smallpox'), ('tenoch', 'hastings', 'oxford')]
DROP=set(frozenset(t) for t in DROP)

# Phrases for hooks. XPH: the subject ("... is closer in time to M than to A."). OBJ: how M and A are named.
XPH=dict(angkor="Angkor Wat is",lalibela="The rock churches of Lalibela are",genji="The Tale of Genji is",canon="Avicenna's Canon of Medicine is",literature="Hanoi's Temple of Literature is",genghis="Genghis Khan's rise to power is",hangul="Korea's Hangul alphabet is",jikji="Korea's Jikji, the metal-type book, is",zhenghe="Zheng He's first treasure fleet is",forbidden="The Forbidden City is",mansa="Mansa Musa's pilgrimage is",tenoch="The founding of Tenochtitlan is",machu="Machu Picchu is",inca="The Inca Empire's expansion is",taj="The Taj Mahal is",sekigahara="The Battle of Sekigahara is",tokugawa="The start of Japan's Edo period is",hagia="Hagia Sophia is",baghdad="The Mongol sack of Baghdad is",qaraw="The University of al-Qarawiyyin is",borobudur="Borobudur is",tang="China's Tang dynasty is",hijra="The Hijra is",khwarizmi="The book that gave us \"algebra\" is",ott_start="The Ottoman Empire's founding is",moai="The Easter Island statues are",nz="The Polynesian settlement of New Zealand is",elephantbird="The death of Madagascar's elephant birds is",panipat="The Mughal Empire's founding is",mactan="Magellan's death in the Philippines is",constantinople="The fall of Constantinople is",blackdeath="The Black Death is",joan="The burning of Joan of Arc is",monalisa="The start of the Mona Lisa is",kamehameha="Kamehameha's unification of Hawaii is",oxford="The start of teaching at Oxford is",kongo="The founding of Kongō Gumi is",pantheon="The Pantheon's rebuilding is",olymp776="The first ancient Olympics are",alexander="Alexander the Great's death is")
OBJ=dict(moon="the Moon landing",iphone="the first iPhone",willie="Steamboat Willie",starry="The Starry Night",titanic="the Titanic",civilwar="the end of the US Civil War",napoleon="Napoleon's death",bastille="the storming of the Bastille",hamlet="Hamlet",harvard="Harvard's founding",galileo="Galileo's trial",gutenberg="Gutenberg's Bible",principia="Newton's Principia",eniac="ENIAC",tv="the first TV broadcast",wright="the Wright brothers' flight",gettysburg="the Battle of Gettysburg",declaration="the Declaration of Independence",oreo="the first Oreo",panama="the Panama Canal",empire="the Empire State Building",sliced="sliced bread",mayflower="the Mayflower landing",columbus="Columbus's voyage",armada="the Spanish Armada",cook="Cook's arrival in Australia",caesar="Julius Caesar's murder",pompeii="the burial of Pompeii",colosseum="the Colosseum",cleo="Cleopatra's birth",parthenon="the start of the Parthenon",republic="Rome becoming a republic",hannibal="Hannibal's march on Italy",rome="the founding of Rome",romefall="the fall of Rome",charl="Charlemagne's coronation",hastings="the Battle of Hastings",notredame="Notre-Dame's first stone",domesday="the Domesday Book",magna="Magna Carta",olymp776="the first Olympics",alexander="Alexander the Great's death",hammurabi="Hammurabi's law code",qin="China's unification",ashoka="Ashoka's edicts",terracotta="the Terracotta Army",confucius="Confucius's birth",cyrus="Cyrus taking Babylon",persepolis="the start of Persepolis",rosetta="the Rosetta Stone",cailun="Cai Lun's paper",hero="Hero's vending machine",abusimbel="Abu Simbel",oracle="the oracle bones",kush="Kush ruling Egypt",tang="the Tang dynasty",hijra="the Hijra",hagia="Hagia Sophia",khwarizmi="al-Khwarizmi's algebra book",qaraw="al-Qarawiyyin's opening",genji="The Tale of Genji",canon="the Canon of Medicine",pantheon="the Pantheon's rebuilding",mansa="Mansa Musa's pilgrimage",tenoch="the founding of Tenochtitlan",tenochfall="the fall of Tenochtitlan",inca="the Inca expansion",forbidden="the Forbidden City",zhenghe="Zheng He's fleet",joan="Joan of Arc's burning",blackdeath="the Black Death",monalisa="the Mona Lisa",hangul="Hangul")


NEW=[
('angkor','starry','colosseum','Angkor Wat is closer in time to The Starry Night than to the Colosseum.'),
('lalibela','iphone','pompeii','The rock churches of Lalibela are closer in time to the first iPhone than to the burial of Pompeii.'),
('genji','bastille','pompeii','The Tale of Genji is closer in time to the storming of the Bastille than to the burial of Pompeii.'),
('canon','napoleon','caesar',"Avicenna's Canon of Medicine is closer in time to Napoleon's death than to Julius Caesar's murder."),
('oxford','tenoch','charl',"The start of teaching at Oxford is closer in time to the founding of Tenochtitlan than to Charlemagne's coronation."),
('constantinople','wright','romefall',"The fall of Constantinople is closer in time to the Wright brothers' flight than to the fall of Rome."),
('hangul','titanic','tang',"Korea's Hangul alphabet is closer in time to the Titanic than to the Tang dynasty."),
('literature','mario','alexander',"Hanoi's Temple of Literature is closer in time to Super Mario Bros. than to Alexander the Great's death."),
('genghis','pacman','pantheon',"Genghis Khan's rise to power is closer in time to Pac-Man than to the Pantheon's rebuilding."),
('jikji','panama','hijra',"Korea's Jikji, the metal-type book, is closer in time to the Panama Canal than to the Hijra."),
('zhenghe','greatwave','khwarizmi',"Zheng He's first treasure fleet is closer in time to The Great Wave than to al-Khwarizmi's algebra book."),
('forbidden','sputnik','hijra','The Forbidden City is closer in time to Sputnik than to the Hijra.'),
('mansa','dna','hero',"Mansa Musa's pilgrimage is closer in time to the DNA double helix than to Hero's vending machine."),
('machu','oreo','khwarizmi',"Machu Picchu is closer in time to the first Oreo than to al-Khwarizmi's algebra book."),
('inca','sliced','qaraw',"The Inca Empire's expansion is closer in time to sliced bread than to al-Qarawiyyin's opening."),
('taj','mario','vikings','The Taj Mahal is closer in time to Super Mario Bros. than to the Vikings in Newfoundland.'),
('hagia','tenochfall','olymp776','Hagia Sophia is closer in time to the fall of Tenochtitlan than to the first Olympics.'),
('baghdad','suez','pantheon',"The Mongol sack of Baghdad is closer in time to the Suez Canal's opening than to the Pantheon's rebuilding."),
('tang','cook','olymp776',"China's Tang dynasty is closer in time to Cook's arrival in Australia than to the first Olympics."),
('moai','pacman','rosetta','The Easter Island statues are closer in time to Pac-Man than to the Rosetta Stone.'),
('nz','iphone','terracotta','The Polynesian settlement of New Zealand is closer in time to the first iPhone than to the Terracotta Army.'),
('blackdeath','sputnik','pantheon',"The Black Death is closer in time to Sputnik than to the Pantheon's rebuilding."),
]
T.extend(NEW)
