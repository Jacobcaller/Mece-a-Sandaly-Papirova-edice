import random
#Akce: Vytvoření Class Gladiatori pro možnost hromadnných úprav, a lepší odkazování proměnných. 
#Class pro určení a následnou možnost hromadnných úprav atributů bojovníků.
#hrac1 = [Název bojovníka,Zdraví bojovníka, Rozsah útoku bojovníka [OD/DO] v kategoriích min/str/max, Energie bojovníka, Štěstí bojovníka]
class Gladiatori:
    def __init__(self, jmeno,zivot,min_utok,str_utok,max_utok,energie,stesti):
        self.jmeno = jmeno
        self.zivot = zivot
        self.min_utok = min_utok 
        self.str_utok = str_utok
        self.max_utok = max_utok
        self.energie = energie
        self.stesti = stesti

#Akce: PŘIŘAZENÍ ATRIBUTŮ K POSTAVĚ HRÁČE 1
#Tato proměnná slouží k zadání množství bodů pro rozdělení do atributů zápasníka.
atributy_body_hrac1 = 10
#Defaultní atributy bojovníka
hrac1 = [input("Zadejte název vašeho válečníka: "),100,[5,10],[10,20],[25,35],60,0]
#Pomocí smyčky while si hráč1 přidává body k atributům které si určí. Smyčka skončí po rozřazení všech bodů.
#Pokud hráč zadá víc bodů než má, upozorní ho na to hláška, body se nepřiřadí, a hráč si musí vybrat znovu.
while atributy_body_hrac1 != 0:
    print("""Atributy:
    Zdraví = zdr 
    Útok = utk
    Energie = ener
    Štěstí = stest    
    """)
    #Atribut Zdraví
    volba = input("Zvolte atribut kterému chcete přiřadit body: ")
    if volba == "zdr":
        print("Počet bodů k dispozici: ",atributy_body_hrac1)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac1:
            atributy_body_hrac1 -= pocet
            hrac1[1] += pocet * 10
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
    #Atribut Útok
    if volba == "utk":
        print("Počet bodů k dispozici: ",atributy_body_hrac1)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac1:
            atributy_body_hrac1 -= pocet
            hrac1[2][0] += pocet * 3
            hrac1[2][1] += pocet * 3
            hrac1[3][0] += pocet * 3
            hrac1[3][1] += pocet * 3
            hrac1[4][0] += pocet * 3
            hrac1[4][1] += pocet * 3
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
    #Atribut Energie
    if volba == "ener":
        print("Počet bodů k dispozici: ",atributy_body_hrac1)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac1:
            atributy_body_hrac1 -= pocet
            hrac1[5] += pocet * 5
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
    #Atribut Štěstí
    if volba == "stest":
        print("Počet bodů k dispozici: ",atributy_body_hrac1)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac1:
            atributy_body_hrac1 -= pocet
            hrac1[6] += pocet * 4
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
#Zde se zadané atributy přiřadí do classy Gladiatori. Přes class Gladiatori lze poté dělat hromadné upravy atributů. např. Zvýšit všem bojovníkům útok, atp.
hrac1_zapasnik = Gladiatori(hrac1[0], hrac1[1], hrac1[2], hrac1[3], (hrac1[4]), hrac1[5], hrac1[6])

#Akce: PŘIŘAZENÍ ATRIBUTŮ K POSTAVĚ HRÁČE 2 - stejné jako u Hráče1
atributy_body_hrac2 = 10
hrac2 = [input("Zadejte název vašeho válečníka: "),100,[10,15],[15,20],[25,30],60,0]
while atributy_body_hrac2 != 0:
    print("""Atributy:
    Zdraví = zdr 
    Útok = utk
    Energie = ener
    Štěstí = stest    
    """)
    volba = input("Zvolte atribut kterému chcete přiřadit body: ")
    if volba == "zdr":
        print("Počet bodů k dispozici: ",atributy_body_hrac2)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac2:
            atributy_body_hrac2 -= pocet
            hrac2[1] += pocet * 10
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
    if volba == "utk":
        print("Počet bodů k dispozici: ",atributy_body_hrac2)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac2:
            atributy_body_hrac2 -= pocet
            hrac2[2][0] += pocet * 3
            hrac2[2][1] += pocet * 3
            hrac2[3][0] += pocet * 3
            hrac2[3][1] += pocet * 3
            hrac2[4][0] += pocet * 3
            hrac2[4][1] += pocet * 3
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
    if volba == "ener":
        print("Počet bodů k dispozici: ",atributy_body_hrac2)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac2:
            atributy_body_hrac2 -= pocet
            hrac2[5] += pocet * 5
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")
    if volba == "stest":
        print("Počet bodů k dispozici: ",atributy_body_hrac2)
        pocet = int(input("Zadejte počet bodů které chcete přiřadit: "))
        if pocet <= atributy_body_hrac2:
            atributy_body_hrac2 -= pocet
            hrac2[6] += pocet * 4
        else:
            print("Zadal jste větší počet bodů než máte k dispozici.")

hrac2_zapasnik = Gladiatori(hrac2[0], hrac2[1], hrac2[2], hrac2[3], (hrac2[4]), hrac2[5], hrac2[6])

#Akce: TATO FUNKCE PROVÁDÍ SOUBOJ
def Souboj(hrac1_jmeno,hrac1_zivot,hrac1_min_utok,hrac1_str_utok,hrac1_max_utok,hrac1_energie,hrac1_stesti,hrac2_jmeno,hrac2_zivot,hrac2_min_utok,hrac2_str_utok,hrac2_max_utok,hrac2_energie,hrac2_stesti):
    print("Hráč 1 -",hrac1_jmeno,"VS","Hráč 2 -",hrac2_jmeno,"\n")

    #Proměnná útok náhodně rozhodne kdo zaútočí první. Poté se hráči střídají. 
    utok = random.choices([0,1], weights = (50,50), k = 1)[0]
    while hrac1_zivot > 0 and hrac2_zivot > 0 :
        #Tyto proměnné oboum hráčům po každém útoku obnoví 10 bodů energie, a 1 bod života.
        hrac1_energie += 10
        hrac2_energie += 10
        hrac1_zivot += 1
        hrac2_zivot += 1

        #Akce: HRÁČ 1 ÚTOČÍ NA HRÁČE 2
        if utok == 0:
            #Akce: VOLBA ÚTOKU HRÁČE 1
            #K proměnné útok se přičte 1, aby příští kolo začínal Hráč2. V útoku Hráče2 na Hráče1 se od proměnné utok odečte 1, aby proměnná útok byla 0, a další kolo začínal Hráč1. Tímto se hráči po každém kole střídají.
            utok += 1
            #Následující IF/ELIF a else zajišťují, aby hráč nemohl použít útok na který nemá dostatek energie. 
            if hrac1_energie >= 40:
                print("Útočí zápasník hráče1 -",hrac1_jmeno)
                print(hrac1_jmeno,"má",hrac1_energie,"bodů energie, a ",hrac1_zivot,"bodů života.")
                zvol_utok = input("""Zvol druh útoku:
                Nejsilnější - max(40% šance) - cena 40 energie
                Střední - str(60% šance) - cena 30 energie
                Nejmenší - min(80% šance) - cena 20 energie
                Pro přeskočení kola zmačkněte Enter.
: """)
            elif hrac1_energie >= 30:
                print("Útočí zápasník hráče1 -",hrac1_jmeno)
                print(hrac1_jmeno,"má",hrac1_energie,"bodů energie, a ",hrac1_zivot,"bodů života.")
                while True:
                    zvol_utok = input("""Zvol druh útoku:
                Střední - str(60% šance) - cena 30 energie
                Nejmenší - min(80% šance) - cena 20 energie
                Pro přeskočení kola zmačkněte Enter.
: """)
                    if zvol_utok == "max" or zvol_utok == "max":
                            print("Na tento útok nemáte energii.")
                    else:
                        break
            elif hrac1_energie >= 20:
                print("Útočí zápasník hráče1 -",hrac1_jmeno)
                print(hrac1_jmeno,"má",hrac1_energie,"bodů energie, a ",hrac1_zivot,"bodů života.")
                while True:
                    zvol_utok = input("""Zvol druh útoku:
                Nejmenší - min(80% šance) - cena 20 energie
                Pro přeskočení kola zmačkněte Enter.
: """)
                    if zvol_utok == "max" or zvol_utok == "max":
                        print("Na tento útok nemáte energii.")
                    elif zvol_utok == "max" or zvol_utok == "str":
                        print("Na tento útok nemáte energii.")
                    else:
                        break
            else:
                print(hrac1_jmeno,"má",hrac1_energie,"bodů energie, a ",hrac1_zivot,"bodů života.")
                print("Hráč1 nemá dostatek energie na žádný útok.")
                zvol_utok = "pauza"
                

            #Akce: PROVEDENÍ ZVOLENÉHO ÚTOKU HRÁČE1
            #V následujících IF/ELSE se zjistí jaký útok hráč zvolil, zda-li byl útok úspěšný nebo ne, a případně kolik poškození útok způsobil. 
            #Každý útok stojí jiné množství energie. Pokud hráč využil nějaké body do atributu štěstí, navýši se o ně procentuelní šance na zásah, a sníží se šance na to, že hráč mine.
            #Poškození Hráče1 se odečte od životů Hráče2. Pokud se Hráč1 netrefí, vypíše se pouze hláška že hráč minul. Pokud Hráč2 po útoku Hráče1 zemřel, vypíše se hláška, a souboj se ukončí.
            #Hráč si také může zvolit přeskočení kola, pokud chce nasbírat energii.
            if zvol_utok.lower()  == "max":
                poskozeni = (random.choices((0,(random.randint(hrac1_max_utok[0],hrac1_max_utok[1]))), weights = (60 - hrac1_stesti, 40 + hrac1_stesti), k = 1))[0]
                hrac1_energie -= 40
                if poskozeni > 0:
                    hrac2_zivot -= poskozeni
                    print("Zápasník",hrac1_jmeno, "způsobil zápasníkovi",hrac2_jmeno,poskozeni,"bodů poškození.")
                    if hrac2_zivot <= 0:
                        print("Zápasník",hrac2_jmeno,"je mrtev.\n")
                    else:
                        print("Zápasníkovi",hrac2_jmeno,"zbývá",hrac2_zivot,"zdraví.\n")  
                else: 
                    print("Zápasník",hrac1_jmeno, "zaútočil na zápasníka",hrac2_jmeno,"svým nejsilnějším útokem, a minul.\n")

            if zvol_utok.lower()  == "str":
                hrac1_energie -= 30
                poskozeni = (random.choices((0,(random.randint(hrac1_str_utok[0],hrac1_str_utok[1]))), weights = (40 - hrac1_stesti, 60 + hrac1_stesti), k = 1))[0]
                if poskozeni > 0:
                    hrac2_zivot -= poskozeni
                    print("Zápasník",hrac1_jmeno, "způsobil zápasníkovi",hrac2_jmeno,poskozeni,"bodů poškození.")
                    if hrac2_zivot <= 0:
                        print("Zápasník",hrac2_jmeno,"je mrtev.\n")
                    else:
                        print("Zápasníkovi",hrac2_jmeno,"zbývá",hrac2_zivot,"zdraví.\n")
                else:
                    print("Zápasník",hrac1_jmeno, "zaútočil na zápasníka",hrac2_jmeno,"středně silným útokem, a minul.\n")

            if zvol_utok.lower() == "min":
                hrac1_energie -= 20
                poskozeni = (random.choices((0,(random.randint(hrac1_min_utok[0],hrac1_min_utok[1]))), weights = (20 - hrac1_stesti, 80 + hrac1_stesti), k = 1))[0]
                if poskozeni > 0:
                    hrac2_zivot -= poskozeni
                    print("Zápasník",hrac1_jmeno, "způsobil zápasníkovi",hrac2_jmeno,poskozeni,"bodů poškození.")
                    if hrac2_zivot <= 0:
                        print("Zápasník",hrac2_jmeno,"je mrtev.\n")
                    else:
                        print("Zápasníkovi druhého hráče",hrac2_jmeno,"zbývá",hrac2_zivot,"zdraví.\n")
                else:
                    print("Zápasník",hrac1_jmeno, "zaútočil na zápasníka",hrac2_jmeno,"svým nejslabším útokem, a minul.\n")
            if zvol_utok == "pauza":
                pass

        
        #Akce: HRÁČ 2 ÚTOČÍ NA HRÁČE 1 - vše je stejné jako u hráče 1
        elif utok == 1:
            #Akce: VOLBA ÚTOKU HRÁČE 2 - vše stejné jako u hráče 1
            utok -= 1
            if hrac2_energie >= 40:
                print("Útočí zápasník hráče2 -",hrac2_jmeno)
                print(hrac2_jmeno,"má",hrac2_energie,"bodů energie, a ",hrac2_zivot,"bodů života.")
                zvol_utok = input("""Zvol druh útoku:
                Nejsilnější - max(40% šance) - cena 40 energie
                Střední - str(60% šance) - cena 30 energie
                Nejmenší - min(80% šance) - cena 20 energie
                Pro přeskočení kola zmačkněte Enter.
: """)
            elif hrac2_energie >= 30:
                print("Útočí zápasník hráče2 -",hrac2_jmeno)
                print(hrac2_jmeno,"má",hrac2_energie,"bodů energie, a ",hrac2_zivot,"bodů života.")
                while True:
                    zvol_utok = input("""Zvol druh útoku:
                Střední - str(60% šance) - cena 30 energie
                Nejmenší - min(80% šance) - cena 20 energie
                Pro přeskočení kola zmačkněte Enter.
: """)
                    if zvol_utok == "max" or zvol_utok == "max":
                            print("Na tento útok nemáte energii.")
                    else:
                        break
            elif hrac2_energie >= 20:
                print("Útočí zápasník hráče2 -",hrac2_jmeno)
                print(hrac2_jmeno,"má",hrac2_energie,"bodů energie, a ",hrac2_zivot,"bodů života.")
                while True:
                    zvol_utok = input("""Zvol druh útoku:
                Nejmenší - min(80% šance) - cena 20 energie
                Pro přeskočení kola zmačkněte Enter.
: """)
                    if zvol_utok == "max" or zvol_utok == "max":
                        print("Na tento útok nemáte energii.")
                    elif zvol_utok == "max" or zvol_utok == "str":
                        print("Na tento útok nemáte energii.")
                    else:
                        break
            else:
                print("Hráč2 nemá dostatek energie na žádný útok.")
                zvol_utok = "pauza"
                
            #Akce: PROVEDENÍ ÚTOKU HRÁČE 2 - vše stejné jako u hráče 1
            if zvol_utok.lower()== "max":
                hrac2_energie -= 40
                poskozeni = (random.choices((0,(random.randint(hrac2_max_utok[0],hrac2_max_utok[1]))), weights = (60 - hrac2_stesti, 40 + hrac2_stesti), k = 1))[0]
                if poskozeni > 0:
                    hrac1_zivot -= poskozeni
                    print("Zápasník",hrac2_jmeno, "způsobil zápasníkovi",hrac1_jmeno,poskozeni,"bodů poškození.")
                    if hrac1_zivot <= 0:
                        print("Zápasník",hrac1_jmeno,"je mrtev.")
                    else:
                        print("Zápasníkovi prvního hráče",hrac1_jmeno,"zbývá",hrac1_zivot,"zdraví.\n")
                else:
                    print("Zápasník",hrac2_jmeno, "zaútočil na zápasníka",hrac1_jmeno,"svým nejsilnějším útokem, a minul.\n")

            if zvol_utok.lower()  == "str":
                hrac2_energie -= 30
                poskozeni = (random.choices((0,(random.randint(hrac2_str_utok[0],hrac2_str_utok[1]))), weights = (40 - hrac2_stesti, 60 + hrac2_stesti), k = 1))[0]
                if poskozeni >= 0:
                    hrac1_zivot -= poskozeni
                    print("Zápasník",hrac2_jmeno, "způsobil zápasníkovi",hrac1_jmeno,poskozeni,"bodů poškození.")
                    if hrac1_zivot <= 0:
                        print("Zápasník",hrac1_jmeno,"je mrtev.")
                    else:
                        print("Zápasníkovi prvního hráče",hrac1_jmeno,"zbývá",hrac1_zivot,"zdraví.\n")  
                else: 
                    print("Zápasník",hrac2_jmeno, "zaútočil na zápasníka",hrac1_jmeno,"středně silným útokem, a minul.\n")

            if zvol_utok.lower()  == "min":
                hrac2_energie -= 20
                poskozeni = (random.choices((0,(random.randint(hrac2_min_utok[0],hrac2_min_utok[1]))), weights = (20 - hrac2_stesti, 80 + hrac2_stesti), k = 1))[0]
                if poskozeni >= 0:
                    hrac1_zivot -= poskozeni
                    print("Zápasník",hrac2_jmeno, "způsobil zápasníkovi",hrac1_jmeno,poskozeni,"bodů poškození.")
                    if hrac1_zivot <= 0:
                        print("Zápasník",hrac1_jmeno,"je mrtev.")
                    else:
                        print("Zápasníkovi prvního hráče",hrac1_jmeno,"zbývá",hrac1_zivot,"zdraví.\n")  
                else:   
                    print("Zápasník",hrac2_jmeno, "zaútočil na zápasníka",hrac1_jmeno,"svým nejslabším útokem, a minul.\n")
            if zvol_utok == "pauza":
                pass

    #Když životy jednoho zápasníka klesnou na nebo pod 0 bodů, ukončí se smyčka while, a pomocí funkce if porovnáme životy, a zjistíme který ze zápasníků vyhrál.
    if hrac1_zivot > hrac2_zivot:
        print(hrac1_jmeno,"z týmu prvního hráče porazil válečníka",hrac2_jmeno,"z týmu druhého hráče.\n")
        
    elif hrac2_zivot > hrac1_zivot:
        print(hrac2_jmeno,"z týmu druhého hráče porazil válečníka",hrac1_jmeno,"z týmu prvního hráče.\n")
    else:
        print("Souboj",hrac1_jmeno,"s",hrac2_jmeno,"skončil remízou. Žádný z týmu nevyhrál.\n")

#Tato proměnná volá funkci Souboj, a určuje potřebné parametry
Souboj1 = Souboj(hrac1_zapasnik.jmeno, hrac1_zapasnik.zivot, hrac1_zapasnik.min_utok, hrac1_zapasnik.str_utok, hrac1_zapasnik.max_utok, hrac1_zapasnik.energie, hrac1_zapasnik.stesti, hrac2_zapasnik.jmeno, hrac2_zapasnik.zivot, hrac2_zapasnik.min_utok, hrac2_zapasnik.str_utok, hrac2_zapasnik.max_utok, hrac2_zapasnik.energie, hrac2_zapasnik.stesti)