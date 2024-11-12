from gegenstände import *

class Händler():

    def __init__(self, Name:str, Geld=30):
        self.Name = Name
        self.Inventar = {}
        self.Geld = Geld

    def kaufen(self, Gegenstand):
        self.Inventar.update({Gegenstand.Name:Gegenstand})
        self.Geld -= int(Gegenstand.Preis*0.75)  # Händler kann zZ unbegrenzt kaufen

    def verkaufen(self, Gegenstand):
        self.Geld += Gegenstand.Preis
        del self.Inventar[Gegenstand.Name]


# Dagobert = Händler('Dagobert', Geld=100000) # Jokehändler ??
Victorius = Händler('Victorius')
for item in Rüstung_Level0_Händler:
    Victorius.Inventar.update(item)
for item in Waffen_Level0_Händler:
    Victorius.Inventar.update(item)

Avenius = Händler('Avenius')
for item in Rüstung_Level1_Händler:
    Avenius.Inventar.update(item)
for item in Waffen_Level1_Händler:
    Avenius.Inventar.update(item)

Ora = Händler('Ora')
for item in Rüstung_Level2_Händler:
    Ora.Inventar.update(item)
for item in Waffen_Level2_Händler:
    Ora.Inventar.update(item)

Linius = Händler('Linius')
for item in Rüstung_Level3_Händler:
    Linius.Inventar.update(item)
for item in Waffen_Level3_Händler:
    Linius.Inventar.update(item)

Händler_Liste=[Victorius, Avenius, Ora, Linius]

