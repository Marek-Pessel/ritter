import numpy as np
from gegenstände import *

class Ritter():

    def __init__(self, Name:str, Leben=25, Stärke=2, Verteidigung=2):
        self.Name = Name
        self.Level = 0
        self.XP = 0
        self.Stufe = 0
        self.Leben = Leben
        self.Leben_max = Leben
        self.Stärke = Stärke
        self.Stärke_komplett = Stärke
        self.Verteidigung = Verteidigung
        self.Verteidigung_komplett = Verteidigung
        self.Helm = None
        self.Rüstung = None
        self.Schild = None
        self.Waffe = None
        self.Geld = 0
        self.Inventar = {}

    def training_stärke(self):
        Kosten = self.Stärke * 10
        print('Deine Stärke zu verbessern würde dich',Kosten,'Münzen kosten.')
        print('Du besitzt derzeit',self.Geld,'Münzen.')
        if self.Geld < Kosten:
            print('Dein Geld reicht leider nicht aus..')
            return
        else:
            Eingabe = input('Möchtest du deine Stärke verbessern?\nja (j)\nnein (n)\n')
            if Eingabe == 'j':
                self.Stärke += 1
                self.Stärke_komplett = self.Stärke
                if self.Waffe:
                    self.Stärke_komplett += self.Waffe.Schaden
                self.Geld -= Kosten
                self.Leben_max += 1
                self.Leben = self.Leben_max
                print('Deine Basisstärke ist jetzt:',self.Stärke,'\n')
            else:
                return

    def training_verteidigung(self):
        Kosten = self.Verteidigung * 10
        print('Deine Verteidigung zu verbessern würde dich',Kosten,'Münzen kosten.')
        print('Du besitzt derzeit',self.Geld,'Münzen.')
        if self.Geld < Kosten:
            print('Dein Geld reicht leider nicht aus..')
            return
        else:
            Eingabe = input('Möchtest du deine Verteidigung verbessern?\nja (j)\nnein (n)\n')
            if Eingabe == 'j':
                self.Verteidigung += 1
                self.Verteidigung_komplett = self.Verteidigung
                if self.Rüstung:
                    self.Verteidigung_komplett += self.Rüstung.Schutz
                if self.Helm:
                    self.Verteidigung_komplett += self.Helm.Schutz
                if self.Schild:
                    self.Verteidigung_komplett += self.Schild.Schutz
                self.Leben_max += 1
                self.Leben = self.Leben_max
                self.Geld -= Kosten
                print('Deine Basisverteidigung ist jetzt:',self.Verteidigung,'\n')
            else:
                return
    
    def kämpfen(self, Gegner):

        Schaden_dev = 0.15 * self.Stärke_komplett
        Schaden_ = round(np.random.normal(self.Stärke_komplett, Schaden_dev),1)
        kritt = 1.1*self.Stärke_komplett
        
        Block_dev = 0.15 * Gegner.Verteidigung_komplett
        Block_ = round(np.random.normal(Gegner.Verteidigung_komplett, Block_dev),1)
        Schaden = Schaden_ - Block_
        if Schaden <= 0:
            Gegner.Leben -= round(np.random.uniform(0.0, 0.3),1)
        else:
            if Schaden_ >= kritt and type(self)==Held:
                Schaden += kritt*2
            Gegner.Leben -= Schaden

    def ausrüsten(self, Gegenstand):
        if Gegenstand.Level > self.Level:
            print('Diesen Gegenstand kannst du erst ab Level',Gegenstand.Level,'tragen.')
            print('Du bist aktuell Level', self.Level,'\n')
            input('Drücke (k)')
            return
        else:
            print(Gegenstand.Beschreibung)
            Eingabe = input('Möchtest du diesen Gegenstand ausrüsten?\nja (j)\nnein (n)\n')
            if Eingabe == 'j':
                if Gegenstand.Art == 'Rüstung':
                    if self.Rüstung:
                        self.ablegen(self.Rüstung)
                    self.Rüstung = Gegenstand
                    self.Verteidigung_komplett += Gegenstand.Schutz
                    print('Du hast',Gegenstand.Name,'jetzt ausgerüstet. Dein Verteidigungswert ist jetzt:',self.Verteidigung_komplett)
                    del self.Inventar[Gegenstand.Name]
                elif Gegenstand.Art == 'Helm':
                    if self.Helm:
                        self.ablegen(self.Helm)
                    self.Helm = Gegenstand
                    self.Verteidigung_komplett += Gegenstand.Schutz
                    print('Du hast',Gegenstand.Name,'jetzt ausgerüstet. Dein Verteidigungswert ist jetzt:',self.Verteidigung_komplett)
                    del self.Inventar[Gegenstand.Name]        
                elif Gegenstand.Art == 'Schild':
                    if self.Schild:
                        self.ablegen(self.Schild)
                    self.Schild = Gegenstand
                    self.Verteidigung_komplett += Gegenstand.Schutz
                    print('Du hast',Gegenstand.Name,'jetzt ausgerüstet. Dein Verteidigungswert ist jetzt:',self.Verteidigung_komplett)
                    del self.Inventar[Gegenstand.Name]
                elif Gegenstand.Art == 'Waffe':
                    if self.Waffe:
                        self.ablegen(self.Waffe)
                    self.Waffe = Gegenstand
                    self.Stärke_komplett += Gegenstand.Schaden
                    print('Du hast',Gegenstand.Name,'jetzt ausgerüstet. Deine Stärke ist jetzt:',self.Stärke_komplett)
                    del self.Inventar[Gegenstand.Name]        
                else:
                    print('Du kannst diesen Gegenstand nicht ausrüsten')

    def ablegen(self, Gegenstand):
        if Gegenstand.Art == 'Rüstung':
            self.Inventar.update({Gegenstand.Name : Gegenstand})
            self.Rüstung = False
            self.Verteidigung_komplett -= Gegenstand.Schutz
            print(Gegenstand.Name,'abgelegt')
        elif Gegenstand.Art == 'Helm':
            self.Inventar.update({Gegenstand.Name : Gegenstand})
            self.Helm = False
            self.Verteidigung_komplett -= Gegenstand.Schutz
            print(Gegenstand.Name,'abgelegt')
        elif Gegenstand.Art == 'Schild':
            self.Inventar.update({Gegenstand.Name : Gegenstand})
            self.Schild = False
            self.Verteidigung_komplett -= Gegenstand.Schutz
            print(Gegenstand.Name,'abgelegt')
        elif Gegenstand.Art == 'Waffe':
            self.Inventar.update({Gegenstand.Name : Gegenstand})
            self.Waffe = False
            self.Stärke_komplett -= Gegenstand.Schaden
            print(Gegenstand.Name,'abgelegt')
        else:
            print('Du trägst diesen Gegenstand nicht.')

    def level_up(self):
        Levelgrenze = int((self.Level+1)**1.4 * 100)
        if self.XP >= Levelgrenze and self.Level<5:
            self.Level += 1
            self.Leben_max += 5 * self.Level
            self.Leben = self.Leben_max
            print('!! Du bist ein Level aufgestiegen !!\n')

##################

class Feind(Ritter):
    def __init__(self, Name:str, Leben, Stärke, Verteidigung):
        
        if Stärke == 0:
            Stärke = 1
        if Verteidigung == 0:
            Verteidigung = 1

        super().__init__(Name=Name, Leben=Leben, Stärke=Stärke, Verteidigung=Verteidigung)
        self.Geld = np.random.randint(5,16)

    def Loot(self, Stufe) -> list:
        Loot= []
        Loot.append(self.Geld*(Stufe+1))
        Loot.append({})
        return Loot

##########################

class Held(Ritter):
    def __init__(self, Name:str, Leben, Stärke, Verteidigung):
        

        super().__init__(Name=Name, Leben=Leben, Stärke=Stärke, Verteidigung=Verteidigung)


### Namensliste für Gegner ####
