from sqlite3 import Connection

class PopulateDb:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def populateServant(self):
        cursor = self.__conn.cursor()

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

        self.__conn.commit()
        self.__conn.close()

    def populateCE(self):
        cursor = self.__conn.cursor()

        ce_and_rarity = [
            ("Formal craft",5), ("Imaginary around",5), ("Limited/zero over",5), ("Kaleidoscope",5), ("Heaven's fell",5), ("Prisma cosmos",5), ("The black grail",5), 
            ("Victor of the moon",5), ("Another ending",5), ("A fragment of 2030",5), ("500-years obsession",5), ("Vessel of the saint",5), ("Ideal holyking",5),
            ("Volumen hydrargyrum",5), ("Before awakening",5), ("Origin bullet",5), ("Devilish bodhisattva",5), ("Under the sun",5), ("Child of the atlas",5), 
            ("Duke of flames",5), ("Holy king of twilight",5), ("One who wish for salvation",5), ("Witchcraft",5), ("Love's curse",5), ("The one who withstood pain",5),
            ("Great marshal of magic",5), ("Holy maiden of winter",5), ("Phantasmal princess",5), ("Averge one",5), ("Iron-willed trainning",4), ("Gen magecraft: Antumbra",4), 
            ("With one strike",4),("Code cast",4), ("Knight's dignity",4), ("Necromancy",4), ("Awakened will",4), ("Golden millennium tree",4), ("Record holder",4), 
            ("Art of poisonous snake",4), ("Art of beater",4),("Gentle affection",4), ("Innocent maiden",4), ("Covering fire",4), ("Room guard",4), ("The final narrator",4), 
            ("Cleaner",4), ("What lies beyond the horizon",4), ("La folia",4), ("The beginning of ambition",4), ("Rhythmed birth",4), ("Royal presence",4), ("Gemstone shots",4), 
            ("Imaginary number attribute",4), ("The vessel of desire",4), ("Winter crystal",4), ("Guardians of the garden",4), ("Flowery paradise",4), ("The illusory confessional",4),
            ("Trigger off",4), ("Inheritance of a long-cherished dream",4), ("Transmutation magecraft",4), ("Ryudoji temple",3), ("Elixir of love",3), ("Bronze-link manipulator",3), 
            ("Ath ngabla",3), ("Hydra dagger",3),("Extremely spicy mapo tofu",3), ("Jeweled sword zelretch",3), ("Battle of caimlamm",3), ("Fragarach",3), ("Inverted moon of the heavens",3), 
            ("Reality marble",3),("Potion of youth",3), ("Collection of mysterious masks",3), ("Ruined church",3), ("Marugoshi shinji",3), ("Atlas institute",3), ("Phantasmal species",3), 
            ("Divine construct",3), ("Soul eater",3),("Sakura's special bento",3), ("The have-not",3), ("Homurahara academy student concil president",3), ("Unwithering flower",3)
        ]

        cursor.executemany("""
            INSERT INTO ce(name, rarity)
            VALUES (?, ?)
            """,ce_and_rarity)
    
        self.__conn.commit()
        self.__conn.close()