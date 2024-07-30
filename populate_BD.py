import sqlite3

conn = sqlite3.connect('storage.db')
cursor = conn.cursor()

servants_and_rarity = [
    ("Altria Pendragon", 5), ("Mordred", 5), ("Altera", 5), ("Orion",5), ("Arjuna",5), ("Napoleon",5), ("Minamoto-no-Tametomo",5), ("Karna",5), ("Enkidu",5), ("Bradamante",5),
    ("Vritra",5), ("Francis Drake",5), ("Ozymandias",5), ("Achilles",5), ("Nemo",5), ("Odysseus",5), ("Europa",5), ("Taizang Wang",5), ("Xuanzang Sanzang",5), ("Caster of nightless city",5),
    ("Anastasia",5), ("Jack the ripper",5), ("Osakabehime",5), ("Vlad III",5), ("Florence Nightingale",5), ("Xiang yu",5), ("Galatea",5),("Great statue of god",5), 
    ("Jeanne d'arc",5), ("Siegfried",4), ("Rama",4), ("Lancelot",4), ("Chevalier d'eon",4), ("Suzuka gozen",4), ("Diarmiund ua duibhne",4), ("Prince of lang ling",4), ("Lakshmi bai",4),
    ("Roland",4), ("Watanabe-no-tsuna",4), ("Emiya",4), ("Atalante",4), ("Archer of inferno",4), ("Chiron",4), ("Zenobia",4), ("Vlad III(Extra)",4), ("Elizabeth báthory",4),
    ("Fionn mac cumhail",4), ("Medusa",4), ("Pãrvati",4), ("Nezha",4), ("Valkyrie",4), ("Qin Liangyu",4), ("Percival",4), ("Anne bonny & Mary read",4), ("Marie antoinette",4),
    ("Martha",4), ("Dobrynya Nikitich",4), ("Nursery rhyme",4), ("Nitocris",4), ("Gilgamesh",4), ("Helena blavatsky",4), ("Caster of okeanos",4), ("Stheno",4),
    ("Emiya(Assassin)",4), ("Carmilla",4), ("Assassin of shinjuku",4), ("Assassin of nightless city",4), ("Assassin of paraiso",4), ("Heracles",4), ("Lancelot",4),
    ("Frankstein",4), ("Beowulf",4), ("Tamamo Cat",4), ("Ibaraki douji",4), ("Berserk of el dorado",4), ("Atalante(Alter)",4), ("Astria",4), ("Avenger of shinjuku",4), ("Hephastion",4),
    ("Julius caesar",3), ("Fergus mac raich",3), ("Gilles de rais",3), ("Robin hood",3), ("David",3), ("Billy the kid",3), ("Euryale",3), ("Tawara touta",3), 
    ("Gilgamesh(Child)",3), ("Willian tell",3), ("Cú chulainn(Prototype)",3), ("Romulus",3), ("Houzouin inshun",3), ("Hektor",3), ("Medusa",3), ("Boudica",3),
    ("Ushiwakamaru",3), ("Alexander",3), ("Mandricardo",3), ("Medea",3), ("Paracelsus von hohenheim",3), ("Charles babbage",3), ("Mephistopheles",3), ("Geronimo",3), ("Avicebron",3),
    ("Zhang jue",3), ("Hassan of the hundred personas",3), ("Henry jekyll & Hyde",3), ("Hassan of the serenity",3), ("Jing ke",3), ("Fumma 'Evil wind' Kotarou",3), ("Lu bu fengxian",3),
    ("Darius III",3), ("Kiyohime",3)
]

cursor.executemany("""
INSERT INTO servants(name, rarity)
VALUES(?, ?)
""", servants_and_rarity)

conn.commit()

conn.close()