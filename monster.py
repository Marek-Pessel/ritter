import numpy as np
from gegenstände import *

class Monster():
    def __init__(self, Name:str, Leben=10, Stärke=1, Verteidigung=1, Level=1, Art =''):
        self.Name = Name
        self.Leben = Leben
        self.Leben_max = Leben
        self.Stärke_komplett = Stärke
        self.Verteidigung_komplett = Verteidigung
        self.Level = Level
        self.flag = False
        self.Art = Art
        self.Beschreibung = ''

    def kämpfen(self, Gegner):

        Schaden_dev = 0.15 * self.Stärke_komplett
        Schaden_ = round(np.random.normal(self.Stärke_komplett, Schaden_dev),1)
        kritt = 1.15*self.Stärke_komplett
        Block_dev = 0.15 * Gegner.Verteidigung_komplett
        Block_ = round(np.random.normal(Gegner.Verteidigung_komplett, Block_dev),1)
        Schaden = Schaden_ - Block_
        
        if Schaden <= 0:
            Gegner.Leben -= round(np.random.uniform(0.0, 0.3),1)
        else:
            if self.Art and Schaden_ >= kritt:
                Schaden += kritt*2
            Gegner.Leben -= Schaden

    def Loot(self, Stufe) -> list:
        Loot = []
        Loot.append( np.random.randint(1,3*self.Level + 1))
        if np.random.randint(0,101) > 10 or len(Loot_liste[Stufe])==0:
            Loot.append({})
        else:
            loot = np.random.randint(0,len(Loot_liste[Stufe]))
            Loot.append(Loot_liste[Stufe][loot])
            Loot_liste[Stufe].pop(loot)

        return Loot
    


### Kreaturen für Stufe 0

Wildhund = Monster('Wildhund', Leben=5, Stärke=2, Verteidigung=0.5, Level=1)
Regenwurm = Monster('Regenwurm', Leben=2, Stärke=1, Verteidigung=0, Level=1)
Wildkatze = Monster('Wildkatze', Leben=9, Stärke=2, Verteidigung=0, Level=1)
Phönix = Monster('Phönix', Leben=30, Stärke=0, Verteidigung=40, Level=1)

Riesenspinne = Monster('Riesenspinne', Leben=15, Stärke=3, Verteidigung=2, Level=2)
Einaugenstein = Monster('Einaugenstein', Leben=25, Stärke=2, Verteidigung=2, Level=2)

Wolf = Monster('Wolf', Leben=20, Stärke=4, Verteidigung=2, Level=3)
Riesenschlange = Monster('Riesenschlange', Leben=30, Stärke=5, Verteidigung=3, Level=3)

Walddrache = Monster('Walddrache', Leben=50 ,Stärke=6, Verteidigung=6, Level=4)

Wurzelschlinge = Monster('Wurzelschlinge',Leben=70,Stärke=9,Verteidigung=7,Level=10, Art='Boss')
Wurzelschlinge.Beschreibung = 'In einem wütenden Wirbel aus Blättern, Zweigen und Erde, kommt ein Ungetüm auf dich zu!\nMit langen Ranken peitscht es nach dir,\nwährend es ein hölzernes Knarren von sich gibt, gleich dem Knurren eines zornigen Hundes!\n'

monsterliste0 = [Wildhund, Regenwurm, Wildkatze, Phönix, Riesenspinne, Einaugenstein, Wolf,
                Riesenschlange,Walddrache, Wurzelschlinge]

## Kreaturen für Stufe 1

Geier = Monster(Name='Geier',Leben=40, Stärke=7,Verteidigung=4,Level=1)
Puma = Monster(Name='Puma',Leben=40, Stärke=7, Verteidigung=5, Level=1)
WutZiege = Monster(Name='wütende Ziege', Leben=30, Stärke=8, Verteidigung=5, Level=1)
Phönix2 = Monster('Phönix', Leben=30, Stärke=0, Verteidigung=40, Level=1)

Steinzwerg = Monster(Name='Steinzwerg',Leben=60,Stärke=11,Verteidigung=9,Level=2)
Greif = Monster(Name='Greif',Leben=50, Stärke=9, Verteidigung=11,Level=2)

Bergdrache = Monster(Name='Bergdrache',Leben=60, Stärke=13, Verteidigung=12, Level=3)
Steingolem = Monster(Name='Steingolem',Leben=80, Stärke=12, Verteidigung=14, Level=3)

Bergtroll = Monster(Name='Bergtroll',Leben=80, Stärke=16,Verteidigung=14,Level=4)

Bergriese = Monster(Name='Bergriese',Leben=200,Stärke=21,Verteidigung=17,Level=20,Art='Boss')

monsterliste1 = [Geier, Puma, WutZiege, Phönix2, Steinzwerg, Greif, Bergdrache,
                Steingolem,Bergtroll,Bergriese]

## Kreaturen für Stufe 2

WutPinguin = Monster('tollwütiger Pinguin',Leben=60, Stärke=9, Verteidigung=7,Level=1)
Schneeleopad = Monster('Schneeleopad',Leben=60, Stärke=9, Verteidigung=9,Level=1)
mutierterHase = Monster('mutierter Schneehase',Leben=40, Stärke=6, Verteidigung=6,Level=1)
Phönix3 = Monster('Phönix', Leben=30, Stärke=0, Verteidigung=40, Level=1)

Eisbär = Monster(Name='Eisbär',Leben=80, Stärke=14, Verteidigung=13,Level=2)
Säbelzahntiger = Monster(Name='Säbelzahntiger',Leben=70, Stärke=14, Verteidigung=12, Level=2)

Eisgolem = Monster(Name='Eisgolem',Leben=100, Stärke=16, Verteidigung=16, Level=3)
Eisdrache = Monster(Name='Eisdrache',Leben=90, Stärke=15, Verteidigung=13,Level=3)

Yeti = Monster(Name='Yeti',Leben=120, Stärke=15, Verteidigung=17, Level=4)

ZombieMammut = Monster('Zombie Mammut',Leben=350, Stärke=25, Verteidigung=19,Level=30, Art='Boss')

monsterliste2 = [WutPinguin, Schneeleopad, mutierterHase, Phönix3, Eisbär, Säbelzahntiger, Eisgolem,
                Eisdrache,Yeti,ZombieMammut]

## Kreaturen für Stufe 3 (8 Gegner, 1 Boss)

Moorfliege = Monster('Moorfliege',Leben=60, Stärke=9, Verteidigung=7,Level=1)
Sumpfnatter = Monster('Sumpfnatter',Leben=60, Stärke=9, Verteidigung=7,Level=1)
Modergnom = Monster('Modergnom',Leben=60, Stärke=9, Verteidigung=7,Level=1)
Phönix4 = Monster('Phönix', Leben=30, Stärke=0, Verteidigung=40, Level=1)

Moorleiche = Monster(Name='Moorleiche',Leben=60, Stärke=9, Verteidigung=7,Level=2)
Grottenkeiler = Monster(Name='Grottenkeiler',Leben=60, Stärke=9, Verteidigung=7, Level=2)

Schlammgolem = Monster(Name='Schlammgolem',Leben=60, Stärke=9, Verteidigung=7, Level=3)
Sumpfdrache = Monster(Name='Sumpfdrache',Leben=60, Stärke=9, Verteidigung=7,Level=3)

Oger = Monster(Name='Oger',Leben=60, Stärke=9, Verteidigung=7, Level=4)

Tümpeltroll = Monster('Tümpeltroll',Leben=60, Stärke=9, Verteidigung=7,Level=30, Art='Boss')

monsterliste3 = [Moorfliege, Sumpfnatter, Modergnom, Phönix4, Moorleiche, Grottenkeiler, Schlammgolem,
                Sumpfdrache,Oger,Tümpeltroll]



monsterlisten = [monsterliste0,monsterliste1,monsterliste2,monsterliste3]