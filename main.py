from ritter import *
from gegenstände import *
from monster import *
from händler import *
import os
from sys import platform as sp
try:
    from playsound import playsound as play
except:
    print('.. no playsound lib found ..')


if sp == 'linux' or sp == 'darwin':
    clear = 'clear'
else:
    clear = 'cls'

def Kopfzeile(Spieler_):
    if Spieler_.Waffe == None:
        Schaden_ = '0'
    else:
        Schaden_ =str(Spieler_.Waffe.Schaden)
    if Spieler_.Helm == None:
        Helm_ = '0'
    else:
        Helm_ =str(Spieler_.Helm.Schutz)
    if Spieler_.Rüstung == None:
        Rüstung_ = '0'
    else:
        Rüstung_ =str(Spieler_.Rüstung.Schutz)
    if Spieler_.Schild == None:
        Schild_ = '0'
    else:
        Schild_ =str(Spieler_.Schild.Schutz)


    print(Spieler_.Name,' Leben:',str(int(Spieler_.Leben))+'/'+str(Spieler_.Leben_max),
          ' Stärke: '+str(Spieler_.Stärke_komplett)+' ('+str(Spieler_.Stärke)+'+'+Schaden_+')',
          ' Verteidigung: '+str(Spieler_.Verteidigung_komplett)+' ('+str(Spieler_.Verteidigung)+'+'+Helm_+'+'+Rüstung_+'+'+Schild_+')',
          '\nMünzen: '+str(Spieler_.Geld),' Level: '+str(Spieler_.Level),'\n\n')

def Kampf(Spieler_, Gegner):
    print(Spieler_.Name,'kämpft mit',Gegner.Name)
    Flucht = 0
    while Spieler_.Leben>0 and Gegner.Leben>0 and Flucht==0:
        Spieler_.kämpfen(Gegner=Gegner)
        Gegner.kämpfen(Gegner=Spieler_)
        print(Gegner.Name,':',round(Gegner.Leben,1))
        print(Spieler_.Name,':',round(Spieler_.Leben,1))
        if Spieler_.Leben <= 0:
            print('Du wurdest besiegt und fällst in Ohnmacht..\n')
            print('Du erwachst in Burg.\n')
            Rückgabe = 'z'
            break
        elif Gegner.Leben <= 0:
            print('Du hast',Gegner.Name,'besiegt!!')
            Loot = Gegner.Loot(Spieler_.Stufe)
            Spieler_.Geld += Loot[0]
            Spieler_.Inventar.update(Loot[1])
            print('Du hast',Loot[0],'Münzen erhalten.\n')
            print('Du besitzt jetzt',Spieler_.Geld,'Münzen\n')
            if Loot[1]:
                print('HEEY! Du hast noch einen besonderen Gegenstand gefunden! Schau in dein Inventar.\n')
            Spieler_.XP += 5
            Spieler_.level_up()
            Rückgabe = 'gewonnen'
            if type(Gegner) == Feind:
                #Rückgabe = input('Möchtest du gegen den nächsten Gegner kämpfen?\nja (j)\nnein (n)\n')
                Rückgabe = 'weiter'
                input('Drücke (k)\n')
                os.system(clear)
                Kopfzeile(Spieler_)
                #if Rückgabe == 'z':
                #    Rückgabe = 'n'
            elif type(Gegner) == Monster:
                Gegner.flag = True
            break
        Eingabe = input('Möchtest du weiter kämpfen? \nja (j) \nnein (n)\n')
        os.system(clear)
        if Eingabe == 'n':
            Flucht = np.random.randint(0,3) # 2/3 Flucht gelingt
            if Flucht:
                print('Du fliehst aus dem Kampf..\n')
                Rückgabe = 'n'
            else:
                print('Du siehst keinen Ausweg..\n') 
    Gegner.Leben = Gegner.Leben_max
    if Spieler_.Leben <= 0:
        Spieler_.Leben += Spieler_.Leben_max
    return Rückgabe

def Turnierplatz(Spieler_):
    Kopfzeile(Spieler_)
    print('Du begibst dich zur Arena vor der Burg.\nHier messen sich die Besten der Besten, du solltest eine gute Waffe mitbringen.\nVielleicht gewinnst du etwas Preisgeld!\n')
    Eingabe = 'Turnierplatz'        
    while Eingabe != 'z': # z für zurück zur Burg
        Turniergegner = Turniergruppe(Spieler_)
        
        #print(Spieler_.Name,':\nStärke',Spieler_.Stärke_komplett,'\nLeben',int(Spieler_.Leben),'\nVerteidigung',Spieler_.Verteidigung_komplett,'\n')
        print('TURNIERGRUPPE:') # class def zeige Werte schreiben
        print(Turniergegner[0].Name,':  Stärke',Turniergegner[0].Stärke,', Leben',Turniergegner[0].Leben,', Verteidigung',Turniergegner[0].Verteidigung)
        print(Turniergegner[1].Name,':  Stärke',Turniergegner[1].Stärke,', Leben',Turniergegner[1].Leben,', Verteidigung',Turniergegner[1].Verteidigung)
        print(Turniergegner[2].Name,':  Stärke',Turniergegner[2].Stärke,', Leben',Turniergegner[2].Leben,', Verteidigung',Turniergegner[2].Verteidigung,'\n')
        
        Eingabe = input('Die Teilnahme kostet '+str((Spieler_.Stufe+1)*10)+' Münzen.\nWillst du am Turnier teilnehmen? \nja (j) \nnein (n) \nzurück zur Burg (z)\n\n')
        os.system(clear)
        if Eingabe == 'j':
            Runde = 0
            if Spieler_.Geld < (Spieler_.Stufe+1)*10:
                Kopfzeile(Spieler_)
                Eingabe = input('Dein Geld reicht leider nicht aus..\nDrücke (k)\n')
                os.system(clear)
                Kopfzeile(Spieler_)
                Eingabe = 'z'
                break
            for Ritter in Turniergegner:
                Eingabe = Kampf(Spieler_,Ritter)
                
                if Eingabe == 'z':
                    print('Dein Geldbeutel fühlt sich leichter an...')
                    Spieler_.Geld -= np.random.randint(5,21)
                    if Spieler_.Geld < 0:
                        Spieler_.Geld = 0
                    print('Du hast noch',Spieler_.Geld,'Münzen..\n')
                    break
                elif Eingabe == 'n':
                    input('Höhnisches Gelächter verfolgt dich..\n')
                    Eingabe = 'z'
                    os.system(clear)
                    print('Du bist zurück in Burg.\n\n')
                    break
                
                Runde += 1
            if Runde == 3:    
                Spieler_.Geld += (Spieler_.Stufe+1)*30
                Eingabe = input('Du hast das Preisgeld gewonnen!\nAuf dem Turnierplatz bleiben (k)\nZurück zur Burg (z)\n')
                os.system(clear)
                Kopfzeile(Spieler_)
        elif Eingabe == 'n':
            Kopfzeile(Spieler_)
            print('Du suchst nach einer anderen Turniergruppe.\n')
            Eingabe = 'weiter auf Turnierplatz'

        else:
            print('Du verlässt den Turnierplatz und gehst zur Burg zurück.')
            break

def Turniergruppe(Spieler_) -> list:
    Gruppe = []
    for i in range(3):
        k = i+1     # Faktor für Gegner-Init
        Name_ = 'Gegner'+str(k) # Wenn Namensliste vorhanden, dann Name random auswählen
        Leben_ = np.random.randint(int(Spieler_.Leben_max*(0.4*k)),int(Spieler_.Leben_max*(0.8*k)))
        Stärke_ = np.random.randint(int((Spieler_.Stärke)*(0.4*k)),int((Spieler_.Stärke+1)*(0.8*k)))
        Verteidigung_ = np.random.randint(int((Spieler_.Verteidigung)*(0.4*k)),int((Spieler_.Verteidigung+1)*(0.8*k)))
        Gegner = Feind(Name=Name_, Leben=Leben_, Stärke=Stärke_, Verteidigung=Verteidigung_)
        Gruppe.append(Gegner)
    
    return Gruppe

def Wald(Spieler_):
    print('Du gehst durchs Burgtor hinaus in den Wald.\n')

    Eingabe = 'Wald'
    while Eingabe != 'z': # z für zurück zur Burg
            print('Im Dämerlicht des Waldes siehst du einen Schatten auf dich zu kommen.\n')
            Eingabe = input('Drücke (k) um fortzufahren.\nInventar (i)\n')
            if Eingabe == 'i':
                Inventar(Spieler_)
            os.system(clear)
            Kopfzeile(Spieler_)
            Kreatur = Auswahl_Kreatur(Spieler_)

            while Eingabe != 'n':
                print('Es ist ein(e)', Kreatur.Name,'!\n')
                if Kreatur.Name == 'Phönix':
                    Phönix(Spieler_)
                    break
                
                print(Kreatur.Name,':\nStärke',Kreatur.Stärke_komplett,'\nLeben',Kreatur.Leben,'\nVerteidigung',Kreatur.Verteidigung_komplett,'\n')
                #print(Spieler_.Name,':\nStärke',Spieler_.Stärke_komplett,'\nLeben',int(Spieler_.Leben),'\nVerteidigung',Spieler_.Verteidigung_komplett,'\n')
                Eingabe=input('Möchteste du den Kampf wagen? \nja (j) \nnein (n) \nzurück zur Burg (z)\n\n')
                os.system(clear)
                if Eingabe == 'j':
                    if Kreatur.Art:
                        print('BOSSFIGHT')
                        Eingabe = Bossfight(Spieler_, Kreatur)
                        break
                    else:
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'n':
                    Flucht = np.random.randint(0,6) # 20% das Flucht nicht gelingt
                    if Flucht:
                        print('Du schleichst davon.\n')
                        Eingabe = 'weiter im wald'
                        break
                    else:
                        print('Die Kreatur hat dich bereits entdeckt!')
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'i':
                    Inventar(Spieler_)
                elif Eingabe == 'z':
                    print('Du verlässt den Wald und gehst zur Burg zurück.')
                    break

def Berge(Spieler_):
    print('Du gehst durchs Burgtor hinaus und wanderst in die Berge.\n')

    Eingabe = 'Berge'
    while Eingabe != 'z': # z für zurück zur Burg
            print('Zwischen den Felsen siehst du ein plötzliche Bewegung!\n')
            Eingabe = input('Drücke (k) um fortzufahren.\nInventar (i)\n')
            if Eingabe == 'i':
                Inventar(Spieler_)
            os.system(clear)
            Kopfzeile(Spieler_)
            Kreatur = Auswahl_Kreatur(Spieler_)

            while Eingabe != 'n':
                print('Es ist ein(e)', Kreatur.Name,'!\n')
                if Kreatur.Name == 'Phönix':
                    Phönix(Spieler_)
                    break
                
                print(Kreatur.Name,':\nStärke',Kreatur.Stärke_komplett,'\nLeben',Kreatur.Leben,'\nVerteidigung',Kreatur.Verteidigung_komplett,'\n')
                #print(Spieler_.Name,':\nStärke',Spieler_.Stärke_komplett,'\nLeben',int(Spieler_.Leben),'\nVerteidigung',Spieler_.Verteidigung_komplett,'\n')
                Eingabe=input('Möchteste du den Kampf wagen? \nja (j) \nnein (n) \nzurück zur Burg (z)\n\n')
                os.system(clear)
                if Eingabe == 'j':
                    if Kreatur.Art:
                        print('BOSSFIGHT')
                        Eingabe = Bossfight(Spieler_, Kreatur)
                        break
                    else:
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'n':
                    Flucht = np.random.randint(0,6) # 20% das Flucht nicht gelingt
                    if Flucht:
                        print('Du entkommst zwischen den Felsen.\n')
                        Eingabe = 'weiter im wald'
                        break
                    else:
                        print('Die Kreatur hat dich bereits entdeckt!')
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'i':
                    Inventar(Spieler_)
                elif Eingabe == 'z':
                    print('Du steigst die Berge hinab und gehst zur Burg zurück.')
                    break

def Eisland(Spieler_):
    print('Du gehst durchs Burgtor hinaus und begibst dich in die verschneiten Lande nördlich der Burg.\n')

    Eingabe = 'Eisland'
    while Eingabe != 'z': # z für zurück zur Burg
            print('Im Schneegestöber siehst du einen Schatten auf dich zu kommen.\n')
            Eingabe = input('Drücke (k) um fortzufahren.\nInventar (i)\n')
            if Eingabe == 'i':
                Inventar(Spieler_)
            os.system(clear)
            Kopfzeile(Spieler_)
            Kreatur = Auswahl_Kreatur(Spieler_)

            while Eingabe != 'n':
                print('Es ist ein(e)', Kreatur.Name,'!\n')
                if Kreatur.Name == 'Phönix':
                    Phönix(Spieler_)
                    break
                
                print(Kreatur.Name,':\nStärke',Kreatur.Stärke_komplett,'\nLeben',Kreatur.Leben,'\nVerteidigung',Kreatur.Verteidigung_komplett,'\n')
                #print(Spieler_.Name,':\nStärke',Spieler_.Stärke_komplett,'\nLeben',int(Spieler_.Leben),'\nVerteidigung',Spieler_.Verteidigung_komplett,'\n')
                Eingabe=input('Möchteste du den Kampf wagen? \nja (j) \nnein (n) \nzurück zur Burg (z)\n\n')
                os.system(clear)
                if Eingabe == 'j':
                    if Kreatur.Art:
                        print('BOSSFIGHT')
                        Eingabe = Bossfight(Spieler_, Kreatur)
                        break
                    else:
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'n':
                    Flucht = np.random.randint(0,6) # 20% das Flucht nicht gelingt
                    if Flucht:
                        print('Zwischen zwei Schneewehen kannst entkommen.\n')
                        Eingabe = 'weiter im wald'
                        break
                    else:
                        print('Die Kreatur hat dich bereits entdeckt!')
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'i':
                    Inventar(Spieler_)
                elif Eingabe == 'z':
                    print('Durchgefroren wanderst du zur Burg zurück.')
                    break

def Sumpf(Spieler_):
    print('Du gehst durchs Burgtor hinaus wagst dich in den trügerischen Sumpf.\n')

    Eingabe = 'Wald'
    while Eingabe != 'z': # z für zurück zur Burg
            print('Zwischen moosbewachsenen, halb toten Bäumen siehst du etwas auf dich zukommen.\n')
            Eingabe = input('Drücke (k) um fortzufahren.\nInventar (i)\n')
            if Eingabe == 'i':
                Inventar(Spieler_)
            os.system(clear)
            Kopfzeile(Spieler_)
            Kreatur = Auswahl_Kreatur(Spieler_)

            while Eingabe != 'n':
                print('Es ist ein(e)', Kreatur.Name,'!\n')
                if Kreatur.Name == 'Phönix':
                    Phönix(Spieler_)
                    break
                
                print(Kreatur.Name,':\nStärke',Kreatur.Stärke_komplett,'\nLeben',Kreatur.Leben,'\nVerteidigung',Kreatur.Verteidigung_komplett,'\n')
                #print(Spieler_.Name,':\nStärke',Spieler_.Stärke_komplett,'\nLeben',int(Spieler_.Leben),'\nVerteidigung',Spieler_.Verteidigung_komplett,'\n')
                Eingabe=input('Möchteste du den Kampf wagen? \nja (j) \nnein (n) \nzurück zur Burg (z)\n\n')
                os.system(clear)
                if Eingabe == 'j':
                    if Kreatur.Art:
                        print('BOSSFIGHT')
                        Eingabe = Bossfight(Spieler_, Kreatur)
                        break
                    else:
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'n':
                    Flucht = np.random.randint(0,6) # 20% das Flucht nicht gelingt
                    if Flucht:
                        print('Du schleichst davon.\n')
                        Eingabe = 'weiter im Sumpf'
                        break
                    else:
                        print('Die Kreatur hat dich bereits entdeckt!')
                        Eingabe = Kampf(Spieler_, Kreatur)
                        break
                elif Eingabe == 'i':
                    Inventar(Spieler_)
                elif Eingabe == 'z':
                    print('Du verlässt den Sumpf und gehst zur Burg zurück. Den Modergeruch wirst du sicher nicht vermissen.')
                    break

def Auswahl_Kreatur(Spieler_)-> Monster:
    alle_besiegt = 0
    for monster in monsterlisten[Spieler_.Stufe]:
        alle_besiegt += monster.flag
    if alle_besiegt < 8:

        balance = np.random.randint(1,5)
        Kreatur = monsterlisten[Spieler_.Stufe][np.random.randint(0,len(monsterlisten[Spieler_.Stufe])-1)]

        if Kreatur.Level > balance:
            Auswahl_Kreatur(Spieler_)
    else:
        Kreatur = monsterlisten[Spieler_.Stufe][9] # Wähle Endboss der Region
        os.system(clear)
        Kopfzeile(Spieler_)
        print('    BOSSFIGHT     \n')
        print(Kreatur.Beschreibung)
        Eingabe = input('Viel Glück, tapferer Held!\nDürcke (k)\n')
        if Eingabe == 'k':
            os.system(clear)
            Kopfzeile(Spieler_)
            return Kreatur
        else:
            Auswahl_Kreatur(Spieler_)

        
    return Kreatur

def Phönix(Spieler_):
    Spieler_.Leben = Spieler_.Leben_max
    print('Der Phönix singt sein wundervolles Lied.\nEin warmes Gefühl durchströmt dich und gibt dir neue Energie!')
    print('Du besitzt wieder volle Lebenskraft!\n\n')

def Bossfight(Spieler_, Boss):
    print(Spieler_.Name,'kämpft mit',Boss.Name)
    Flucht = 0
    while Spieler_.Leben>0 and Boss.Leben>0 and Flucht==0:
        Spieler_.kämpfen(Gegner=Boss)
        Boss.kämpfen(Gegner=Spieler_)
        print(Boss.Name,':',round(Boss.Leben,1))
        print(Spieler_.Name,':',round(Spieler_.Leben,1))
        if Spieler_.Leben <= 0:
            print('Du wurdest besiegt und fällst in Ohnmacht..\n')
            print('Du erwachst in Burg.\n')
            Rückgabe = 'z'
            break
        elif Boss.Leben <= 0:
            print('Du hast',Boss.Name,'besiegt!!')
            Spieler_.Geld += Boss.Level * 10
            Gegenstand = np.random.randint(0,4)
            Spieler_.Inventar.update(Bossloot_liste[Spieler_.Stufe][Gegenstand])
            print('Du hast',Boss.Level*10,'Münzen erhalten.\n')
            print('Du besitzt jetzt',Spieler_.Geld,'Münzen\n')
            print('!! Du hast einen mächtigen Gegenstand erhalten !!')
            Spieler_.XP += 5*Boss.Level
            Spieler_.level_up()
            Spieler_.Stufe += 1
            Rückgabe = 'z'
            break
        Eingabe = input('Möchtest du weiter kämpfen? \nja (j) \nnein (n)\n')
        os.system(clear)
        if Eingabe == 'n':
            Flucht = np.random.randint(0,2)
            if Flucht:
                print('Du fliehst aus dem Kampf, bist aber weiter vor Ort.\n')
                Rückgabe = 'n'
            else:
                print('Du siehst keinen Ausweg..\n')
    # Ende while 
    Boss.Leben = Boss.Leben_max
    if Spieler_.Leben <= 0:
        Spieler_.Leben += Spieler_.Leben_max
    return Rückgabe

def Trainigsplatz(Spieler_):
    Kopfzeile(Spieler_)
    print('Du läufst zum Trainingsplatz.')
    print('Hier kannst du deine Stärke und deine Verteidigung verbessern.')

    Eingabe = 'Trainingsplatz'
    while Eingabe != 'z': # z für zurück zur Burg
        Kopfzeile(Spieler_)
        Eingabe = input('Was möchtest du trainieren?\nStärke (s)\nVerteidigung (v)\nzurück zur Burg (z)\n\n')
        os.system(clear)

        if Eingabe == 's':
            Kopfzeile(Spieler_)
            Spieler_.training_stärke()
            Eingabe = input('Drücke (k), um fortzufahren.')
            os.system(clear)
                    
        elif Eingabe == 'v':
            Kopfzeile(Spieler_)
            Spieler_.training_verteidigung()
            Eingabe = input('Drücke (k), um fortzufahren.')
            os.system(clear)
            
        elif Eingabe == 'z':
            Kopfzeile(Spieler_)
            print('Du verlässt den Trainingsplatz und gehst zur Burg zurück.\n')
            break

def Inventar(Spieler_):
    Eingabe = 'Inventar'
    while Eingabe != 'z':
        os.system(clear)
        Kopfzeile(Spieler_)
        print('INVENTAR von',Spieler_.Name,'\n')
        for key in Spieler_.Inventar:
            value = Spieler_.Inventar[key]
            if type(value) == list:
                print(key, len(value))
            else:
                print(key)
        Eingabe = input('Welchen Gegenstand möchtest du benutzen?\n')
        os.system(clear)
        if Eingabe == 'z':
            os.system(clear)
            break
        try:
            Gegenstand = Spieler_.Inventar[Eingabe]
            Spieler_.ausrüsten(Gegenstand)
        except:
            print('Diesen Gegenstand hast du nicht.\n')
            pass
              
def Marktplatz(Händler_, Spieler_):
    Eingabe = 'Marktplatz'
    while Eingabe != 'z':
        Kopfzeile(Spieler_)
        print(Händler_.Name+': Seid gegrüßt! Wie kann ich helfen?')
        Eingabe = input('kaufen (k)\nverkaufen (v)\nInventar (i)\n')
        os.system(clear)
        
        if Eingabe == 'k':
            Kopfzeile(Spieler_)
            print('INVENTAR von',Händler_.Name,'\n')
            for key in Händler_.Inventar:
                value = Händler_.Inventar[key]
                #if type(value) == list:
                #    print(key, len(value),': Stk.')
                #else:
                print(key,' : Preis', value.Preis)

            Eingabe = input('\nWelche Ware weckt dein Interesse?\n')
            os.system(clear)
            if Eingabe == 'z':
                break
            try:
                Gegenstand = Händler_.Inventar[Eingabe]
            except:
                input('Diesen Gegenstand habe ich nicht. Komm wieder, wenn du etwas anderes brauchst. (k)\n')
                os.system(clear)
                break
                    
            Kopfzeile(Spieler_)
            print('Du schaust dir den Gegenstand genauer an:\n',Gegenstand.Beschreibung)
            Eingabe = input('Möchtest du diesen Gegenstand kaufen?\nja (j)\nnein (n)\n')
            os.system(clear)
            if Eingabe == 'j':
                if Gegenstand.Preis > Spieler_.Geld:
                    Kopfzeile(Spieler_)
                    print('Dein Geld reicht nicht aus..')
                    Eingabe = input('Drücke (k) um fortzufahren.\n')
                    os.system(clear)
                else:
                    Händler_.verkaufen(Gegenstand)
                    Spieler_.Inventar.update({Gegenstand.Name:Gegenstand})
                    Spieler_.Geld -= Gegenstand.Preis
                    Kopfzeile(Spieler_)
                    print('Du hast', Gegenstand.Name, 'gekauft!')
                    Eingabe = input('Drücke (k) um fortzufahren.\n')
                    os.system(clear)

        elif Eingabe == 'v':
            Kopfzeile(Spieler_)
            print('INVENTAR von',Spieler_.Name,'\n')
            for key in Spieler_.Inventar:
                value = Spieler_.Inventar[key]
                if type(value) == list:
                    print(key, len(value))
                else:
                    print(key)
            Eingabe = input('Welchen Gegenstand möchtest du verkaufen?\n')
            os.system(clear)
            if Eingabe == 'z':
                break
            try:
                Gegenstand = Spieler_.Inventar[Eingabe]
            except:
                input('Diesen Gegenstand hast ich nicht. Komm wieder. (k)\n')
                os.system(clear)
                break
            if Gegenstand.Preis > Händler_.Geld:
                print('Für diesen Kauf reichen meine Münzen leider nicht.')
            else:
                Händler_.kaufen(Gegenstand)
                Spieler_.Geld += int(Gegenstand.Preis * 0.75)
                del Spieler_.Inventar[Gegenstand.Name]
                print('Du hast', Gegenstand.Name, 'verkauft!')
        elif Eingabe == 'i':
            Inventar(Spieler_)



def main():

    # Intro
    print('So so, du willst also Computer spielen. Schön, schön. In diesem Spiel bist du ein Held.')
    print('Ein Held, der mit Schild und Schwert, Axt und Speer die Monster und wilden Tiere in Schach halten muss.')
    print('Wenn du Kämpfe gewinnst, erhählst du Belohnungen. Diese Belohnungen werden dir helfen, stärker zu werden.')
    print('Dann zeig mal, was du drauf hast!')
    
    # Spieler Init
    Name = input('Wie ist dein Name, du Held?\n')
    Spieler = Held(Name=Name,Leben=25,Stärke=1,Verteidigung=1)
    
    os.system(clear)
    Kopfzeile(Spieler)
    
    # Spiel Loop
    Eingabe = input('Es geht los! Drücke (k) um zu starten oder (q) um das Spiel zu beenden.\n\n')
    os.system(clear)

    ####### special INITs for debugging
    #Spieler.Geld = 10
    #Spieler.Stufe = 4
    #for monster in monsterlisten[Spieler.Stufe]:
    #    monster.flag = True
    # another test for commiting


# Hauptschleife ###########
    while Eingabe != 'q':

        if Spieler.Stufe == 0:
            Eingabe = input('Wohin möchtest du gehen?\nWald (w)\nArena (a)\nTrainingsplatz (t)\nHändler (h)\nInventar (i)\n\n')
        elif Spieler.Stufe == 1:
            Eingabe = input('Wohin möchtest du gehen?\nBerge (b)\nArena (a)\nTrainingsplatz (t)\nHändler (h)\nInventar (i)\n\n')
        elif Spieler.Stufe == 2:
            Eingabe = input('Wohin möchtest du gehen?\nEisland (e)\nArena (a)\nTrainingsplatz (t)\nHändler (h)\nInventar (i)\n\n')
        elif Spieler.Stufe == 3:
            Eingabe = input('Wohin möchtest du gehen?\nSumpf (s)\nArena (a)\nTrainingsplatz (t)\nHändler (h)\nInventar (i)\n\n')
        else:
            os.system(clear)
            print('\n\n\nOh du tapferer Held! Dank dir sind die Länderein um die Burg wieder sicher!')
            print('Ewiger Ruhm und ein glückliches Leben seien dir beschieden! Mögest du leben, bis du alt und bucklig bist!')
            dir_path = os.path.dirname(__file__)
            sound_path = os.path.normpath(os.path.join(dir_path, 'winner.mp3')).replace('\\', '/')
            try:
                play(sound_path)
            except:
                print('Leider fehlt die Playsound Library. Da musst du dir die Musik leider vorstellen.')
                print('Dölölöööö düdü dölödüüü... und so weiter.')
            input('Drücke eine Taste\n')
            break

        os.system(clear)
        ## Regionen
        if Eingabe == 'w' and Spieler.Stufe == 0:
            Wald(Spieler)
        elif Eingabe == 'b' and Spieler.Stufe == 1:
            Berge(Spieler)
        elif Eingabe == 'e' and Spieler.Stufe == 2: 
            Eisland(Spieler)
        elif Eingabe == 's' and Spieler.Stufe == 3: # Kreaturenliste
            Sumpf(Spieler)

        # Arena        
        elif Eingabe == 'a':
            Turnierplatz(Spieler) # Gegner müssen auch Rüstung bekommen oder mit Komplett-Werten steigen

        # Trainingsplatz
        elif Eingabe == 't':
            Trainigsplatz(Spieler)

        # Händler
        elif Eingabe == 'h':
            Händler = Händler_Liste[Spieler.Stufe] # Händler und Gegenstände Stufe 2 un 3 schreiben
            Marktplatz(Händler, Spieler) # Bei Wahl eines Gegenstands kurze Beschreibung geben

        # Inventar
        elif Eingabe == 'i':
            Inventar(Spieler)

        elif Eingabe == 'q':
            print('Du hast das Spiel beendet.')
        else:
            print('Das war keine gültige Eingabe..')
            

    # Ende Spiel Loop




if __name__ == '__main__':
    main() 