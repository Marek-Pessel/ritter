#test comment

class Rüstung(): 

    def __init__(self, Name:str, Schutz, Art:str, Preis, Level):
        self.Name = Name
        self.Schutz = Schutz
        self.Art = Art
        self.Preis = Preis
        self.Level = Level
        self.Beschreibung = ''

class Waffe():

    def __init__(self, Name:str, Schaden, Art:str, Preis, Level):
        self.Name = Name
        self.Schaden = Schaden
        self.Art = Art
        self.Preis = Preis
        self.Level = Level
        self.Beschreibung = ''

############# GEGENSTÄNDE #############

# Stufe 0 -------------
# loot
Lederkappe = Rüstung(Name='Lederkappe',Schutz=1, Art='Helm',Preis=10, Level=0)
Lederkappe.Beschreibung = 'Eine schmutzige Kappe aus einfachem Leder. Schutz: 1\n'
Lederrüstung = Rüstung(Name='Lederrüstung',Schutz=1, Art='Rüstung',Preis=10, Level=0)
Lederrüstung.Beschreibung = 'Eine abgenutzte, eng anliegende Lederrüstung. Schutz: 1\n'
Rundschild = Rüstung(Name='Rundschild', Schutz=1, Art='Schild', Preis=10, Level=0)
Rundschild.Beschreibung = 'Ein einfacher Rundschild aus Holz. Die Halteriemen sind ausgeleihert. Schutz: 1\n'
Keule = Waffe(Name='Keule',Schaden=1, Art='Waffe', Preis=5, Level=0)
Keule.Beschreibung = 'Eine grobe Keule, nicht mehr als ein grob bearbeiteter Ast. Schaden: 1\n'
# Händler
Kettenhaube = Rüstung(Name='Kettenhaube',Schutz=2, Art='Helm',Preis=20, Level=0)
Kettenhaube.Beschreibung = 'Eine Stoffhaube versehen mit feinen Kettengliedern. Schutz: 2\n'
Kettenhemd = Rüstung(Name='Kettenhemd',Schutz=2, Art='Rüstung',Preis=20, Level=0)
Kettenhemd.Beschreibung = 'An einigen Kettengliedern hat der Rost genagt, doch sonst ist der Zustand gut. Schutz: 2\n'
VerstärkerterSchild = Rüstung(Name='Verstärkter Schild',Schutz=2, Art='Schild',Preis=20, Level=0)
VerstärkerterSchild.Beschreibung = 'Ein Rundschild aus Holz, die Kante ist mit Eisen beschlagen. Schutz: 2\n'
Kurzschwert = Waffe(Name='Kurzschwert',Schaden=3, Art='Waffe',Preis=20, Level=0)
Kurzschwert.Beschreibung = 'Ein schlichtes Schwert. Es könnte mal wieder poliert werden, doch scharf ist es. Schaden: 3\n'
Breitschwert = Waffe(Name='Breitschwert', Schaden=5, Art='Waffe', Preis=35, Level=1)
Breitschwert.Beschreibung = 'Ein Schwert von einfacher Schmiedekunst mit breiter Klinge. Schaden: 5 (benötigt Level 1)\n'
Dolch = Waffe(Name='Dolch',Schaden=2, Art='Waffe', Preis=8, Level=0)
Dolch.Beschreibung = 'Ein schmuckloser Dolch, doch ist er scharf und spitz. Schaden: 2\n'
# Bossloot
SchwarzerHelm = Rüstung(Name='Schwarzer Helm', Schutz=5, Art='Helm',Preis=100,Level=1)
SchwarzerHelm.Beschreibung = 'Ein Helm so schwarz wie die Nacht. Schutz: 5 (benötigt Level 1)\n'
SchwarzeRüstung = Rüstung(Name='Schwarze Rüstung', Schutz=5, Art='Rüstung',Preis=100,Level=1)
SchwarzeRüstung.Beschreibung = 'Eine Rüstung so schwarz wie die Nacht. Schutz: 5 (benötigt Level 1)\n'
SchwarzerSchild = Rüstung(Name='Schwarzer Schild',Schutz=5, Art='Schild',Preis=100, Level=1)
SchwarzerSchild.Beschreibung = 'Ein Schild so schwarz wie die Nacht. Schutz: 5 (benötigt Level 1)\n'
Blauschimmeraxt = Waffe(Name='Blauschimmeraxt', Schaden=7, Art='Waffe', Preis=100, Level=1)
Blauschimmeraxt.Beschreibung = 'Eine Axt mit breiten Bart. Ein mystischer Schimmer umgibt sie. Schaden: 7 (benötigt Level 1)\n'

 
# Stufe 1 -------------
# loot
Eisenhelm = Rüstung(Name='Eisenhelm', Schutz=3, Art='Helm', Preis=30,Level=1)
Eisenhelm.Beschreibung = 'Ein schlichter Helm aus Eisen. Schutz: 3 (benötigt Level 1)\n'
Eisenrüstung = Rüstung(Name='Eisenrüstung', Schutz=3, Art='Rüstung', Preis=30,Level=1)
Eisenrüstung.Beschreibung = 'Eine schlichte Rüstung aus Eisen. Schutz: 3 (benötigt Level 1)\n'
Eisenschild = Rüstung(Name='Eisenschild', Schutz=3, Art='Schild', Preis=30,Level=1)
Eisenschild.Beschreibung = 'Ein rundes Schild aus Eisen. Schutz: 3 (benötigt Level 1)\n'
Degen = Waffe(Name='Degen',Schaden=4, Art='Waffe', Preis=40, Level=1)
Degen.Beschreibung = 'Eine schlanke und scharfe Waffe. Schaden: 4 (benötigt Level 1)\n'
# Händler
Stahlhelm = Rüstung(Name='Stahlhelm', Schutz=4, Art='Helm', Preis=40,Level=2)
Stahlhelm.Beschreibung = 'Ein Helm aus genieteten Stahlplatten. Schutz: 4 (benötigt Level 2)\n'
Stahlrüstung = Rüstung(Name='Stahlrüstung',Schutz=4, Art='Rüstung',Preis=40, Level=2)
Stahlrüstung.Beschreibung = 'Eine Rüstung aus genieteten Eisenplatten. Schutz: 4 (benötigt Level 2)\n'
StahlSchild = Rüstung(Name='Stahlschild', Schutz=4, Art='Schild', Preis=40,Level=2)
StahlSchild.Beschreibung = 'Ein rechteckiger Schild, wie ihn die Kaiserlichen Truppen tragen. Schutz: 4 (benötigt Level 2)\n'
Streitaxt = Waffe(Name='Streitaxt',Schaden=7, Art='Waffe',Preis=70, Level=2)
Streitaxt.Beschreibung = 'Ein Axt mit doppeltem Bart. Schaden: 7 (benötigt Level 2)\n'
# Bossloot
Knochenhelm = Rüstung(Name='Knochehelm', Schutz=7, Art='Helm', Preis=150,Level=2)
Knochenhelm.Beschreibung = 'Ein Helm geschnitz aus den Knochen eines Riesen. Schutz: 7 (benötigt Level 2)\n'
Knochenpanzer = Rüstung(Name='Knochenpanzer', Schutz=7, Art='Rüstung', Preis=150,Level=2)
Knochenpanzer.Beschreibung = 'Ein Lederpanzer verstärkt und verziert mit den Knochen eines Riesen. Schutz: 7 (benötigt Level 2)\n'
Knochenschild = Rüstung(Name='Knochenschild', Schutz=7, Art='Schild', Preis=150,Level=2)
Knochenschild.Beschreibung = 'Ein Schild gefertigt au dem Schulterblatt eines Riesen. Schutz: 7 (benötigt Level 2)\n'
BlutroterRiesenhammer = Waffe(Name='Blutroter Riesenhammer', Schaden=12, Art='Waffe', Preis=150, Level=2)
BlutroterRiesenhammer.Beschreibung = 'Ein mächtiger Hammer, aus einer fremdartigen Legierung. Schaden: 12 (benötigt Level 2)\n'


# Stufe 2 ------------
# loot (3 Rüstungen, 1 Waffe) BESCHREIBUNGEN
Plattenhelm = Rüstung(Name='Plattenhelm', Schutz=5, Art='Helm', Preis=50,Level=3)
Plattenpanzer = Rüstung(Name='Plattenpanzer', Schutz=5, Art='Rüstung', Preis=50,Level=3)
Plattenschild = Rüstung(Name='Plattenschild', Schutz=5, Art='Schild', Preis=50,Level=3)
RostSchwert = Waffe(Name='rostiges Schwert', Schaden=8, Art='Waffe',Preis=80,Level=3)
# Händler (3 Rüstungen, 3 Waffen) BESCHREIBUNGEN
Gardistenhelm = Rüstung(Name='Gardistenhelm', Schutz=6, Art='Helm', Preis=60,Level=4)
Gardistenrüstung = Rüstung(Name='Gardistenrüstung', Schutz=6, Art='Rüstung', Preis=60,Level=4)
Gardistenschild = Rüstung(Name='Gardistenschild', Schutz=6, Art='Schild', Preis=60,Level=4)
Langschwert = Waffe(Name='Zweihänder', Schaden=10, Art='Waffe',Preis=100,Level=4)
Hellebarde = Waffe(Name='Hellebarde', Schaden=8, Art='Waffe',Preis=90,Level=4)
Kriegsaxt = Waffe(Name='Kriegsaxt', Schaden=11, Art='Waffe',Preis=110,Level=4)
# Bossloot (3 Rüstungen) BESCHREIBUNGEN
Kristallhelm = Rüstung(Name='Kristallhelm', Schutz=9, Art='Helm', Preis=160,Level=4)
Kristallrüstung = Rüstung(Name='Kristallrüstung', Schutz=9, Art='Rüstung', Preis=160,Level=4)
Kristallschild = Rüstung(Name='Kristallschild', Schutz=9, Art='Schild', Preis=160,Level=4)
Morgenschwert = Waffe(Name='Morgenschwert',Schaden=15, Art='Waffe', Preis=200, Level=3)
Morgenschwert.Beschreibung = 'Die Klinge ist aus einem eigenartigen Kristall, der von innen zu leuchten scheint. Schaden: 15 (benötigt Level 3)\n'


# Stufe 3 ------------
# loot (3 Rüstungen, 1 Waffe) BESCHREIBUNGEN
Helm4_loot = Rüstung(Name='Helm4_loot', Schutz=7, Art='Helm', Preis=70,Level=4)
Rüstung4_loot = Rüstung(Name='Rüstung4_loot', Schutz=7, Art='Rüstung', Preis=70,Level=4)
Schild4_loot = Rüstung(Name='Schild4_loot', Schutz=7, Art='Schild', Preis=70,Level=4)
Waffe4_loot = Waffe(Name='Waffe4_loot', Schaden=11, Art='Waffe',Preis=80,Level=4)
# Händler (3 Rüstungen, 3 Waffen) BESCHREIBUNGEN
Helm4_händler = Rüstung(Name='Helm4_händler', Schutz=9, Art='Helm', Preis=60,Level=5)
Rüstung4_händler = Rüstung(Name='Rüstung4_händler', Schutz=9, Art='Rüstung', Preis=60,Level=5)
Schild4_händler = Rüstung(Name='Schild4_händler', Schutz=9, Art='Schild', Preis=60,Level=5)
Waffe4_händler = Waffe(Name='Waffe4_händler', Schaden=13, Art='Waffe',Preis=100,Level=5)
# Bossloot (3 Rüstungen, 1 Waffe) BESCHREIBUNGEN
Helm4_boss = Rüstung(Name='Helm4_boss', Schutz=12, Art='Helm', Preis=160,Level=5)
Rüstung4_boss = Rüstung(Name='Rüstung4_boss', Schutz=12, Art='Rüstung', Preis=150,Level=5)
Schild4_boss = Rüstung(Name='Schild4_boss', Schutz=12, Art='Schild', Preis=160,Level=5)
Waffe4_boss = Waffe(Name='Waff4_boss', Schaden=18,Art='Waffe',Preis=200,Level=5)

#------------




### LISTEN für Anwendung ###

Rüstung_Level0_Händler = [{Kettenhaube.Name:Kettenhaube},{Kettenhemd.Name:Kettenhemd},
                          {VerstärkerterSchild.Name:VerstärkerterSchild}]
Rüstung_Level1_Händler = [{Stahlhelm.Name:Stahlhelm},{Stahlrüstung.Name:Stahlrüstung},
                          {StahlSchild.Name:StahlSchild}]
Rüstung_Level2_Händler = [{Gardistenhelm.Name:Gardistenhelm},{Gardistenrüstung.Name:Gardistenrüstung},
                          {Gardistenschild.Name:Gardistenschild}]
Rüstung_Level3_Händler = [{Helm4_händler.Name:Helm4_händler},{Rüstung4_händler.Name:Rüstung4_händler},
                          {Schild4_händler.Name:Schild4_händler}]
#------------
Waffen_Level0_Händler = [{Breitschwert.Name:Breitschwert}, {Kurzschwert.Name:Kurzschwert}, {Dolch.Name:Dolch}]
Waffen_Level1_Händler = [{Streitaxt.Name:Streitaxt}, {Kurzschwert.Name:Kurzschwert}, {Dolch.Name:Dolch}]
Waffen_Level2_Händler = [{Langschwert.Name:Langschwert}, {Hellebarde.Name:Hellebarde}, {Kriegsaxt.Name:Kriegsaxt}]
Waffen_Level3_Händler = [{Waffe4_händler.Name:Waffe4_händler}, {Kurzschwert.Name:Kurzschwert}, {Dolch.Name:Dolch}]
#------------
Loot_0 = [{Lederkappe.Name:Lederkappe}, {Lederrüstung.Name:Lederrüstung},
          {Rundschild.Name:Rundschild},{Keule.Name:Keule}]
Loot_1 = [{Eisenhelm.Name:Eisenhelm}, {Eisenrüstung.Name:Eisenrüstung},
          {Eisenschild.Name:Eisenschild},{Degen.Name:Degen}]
Loot_2 = [{Plattenhelm.Name:Plattenhelm}, {Plattenpanzer.Name:Plattenpanzer},
          {Plattenschild.Name:Plattenschild},{RostSchwert.Name:RostSchwert}]
Loot_3 = [{Helm4_loot.Name:Helm4_loot}, {Rüstung4_loot.Name:Rüstung4_loot},
          {Schild4_loot.Name:Schild4_loot},{Waffe4_loot.Name:Waffe4_loot}]

Loot_liste = [Loot_0,Loot_1,Loot_2,Loot_3]
#-------------
Bossloot_0 = [{SchwarzerSchild.Name:SchwarzerSchild}, {Blauschimmeraxt.Name:Blauschimmeraxt},
              {SchwarzerHelm.Name:SchwarzerHelm},{SchwarzeRüstung.Name:SchwarzeRüstung}]
Bossloot_1 = [{BlutroterRiesenhammer.Name:BlutroterRiesenhammer}, {Knochenhelm.Name:Knochenhelm},
              {Knochenpanzer.Name:Knochenpanzer},{Knochenschild.Name:Knochenschild}]
Bossloot_2 = [{Kristallhelm.Name:Kristallhelm}, {Kristallrüstung.Name:Kristallrüstung},
              {Morgenschwert.Name:Morgenschwert},{Kristallschild.Name:Kristallschild}]
Bossloot_3 = [{Helm4_boss.Name:Helm4_boss}, {Rüstung4_boss.Name:Rüstung4_boss},
              {Schild4_boss.Name:Schild4_boss},{Waffe4_boss.Name:Waffe4_boss}]

Bossloot_liste = [Bossloot_0, Bossloot_1, Bossloot_2, Bossloot_3]
#-------------