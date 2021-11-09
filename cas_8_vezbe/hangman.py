import random

broj_reci = 267751 #ukupak broj reci u fajlu
dictionary = open("dictionary.txt", "r")
random.seed() #postavlja se seed za radnom
dicitonary_reci = dictionary.readlines()
dictionary.close()

niz_pogodjenih_slova = ''
broj_pogresenih = 0
broj_pogodjenih = 0
rec = ''

def nova_rec():
    redni_broj_linije = random.randint(0, broj_reci)
    rec =  dicitonary_reci[redni_broj_linije-1]
    rec = rec[:-1] #jer se svaka rec zavrsava \n a ne treba nam
    print(rec) #ako se proverava da li program radi kad je pogodjena rec
    return rec

def ispis_hangamana():
    print("-------------------------------------")
    print(" ____")
    print(" |  |")

    if broj_pogresenih>=1: print(" |  O") #jedna greska
    else: print(" |")
    
    if broj_pogresenih>1: print(" | ", end='') 
    else: print(" |")

    if broj_pogresenih>=4 : print("/|\\") #cetiri
    elif broj_pogresenih == 3 :print("/|") #tri
    elif broj_pogresenih == 2 : print(" |") #dve

    if(broj_pogresenih==5): print(" | /") #pet
    elif(broj_pogresenih==6): print(" | / \\") #sest
    else: print(" |")

    print(" |")
    print("_|_")

def ispis_pogodjenih(): #ispisuje pogodjena slova i _ tamo gde nisu pogodjena
    print("\nBroj pogresenih:", broj_pogresenih)
    print("Broj pogodjenih:", broj_pogodjenih)
    print("Rec: ", end='')
    for chr in rec: #za svako slovo iz reci cemo proveravati da li se nalazi u nizu pogodjenih slova
        if chr in niz_pogodjenih_slova:
            print(chr + " ", end='')
        else: print("_ ", end='')
    print()
    print()
        
def provera_pogodjenih(slovo): #funkcija koja nakon unosa proverava da li je pogodak ili ne
    global broj_pogodjenih
    global broj_pogresenih
    global niz_pogodjenih_slova

    nadjeno = 0 #promenljiva koja ako je 0 znaci da uneto slovo nije u reci, a 1 ako jeste
    for chr in rec:
        if(slovo==chr):
            nadjeno = 1 #cim nadjemo slovo u zadatoj reci podesavamo nadjeno na 1
            broj_pogodjenih +=1
            if niz_pogodjenih_slova.find(slovo)==-1: niz_pogodjenih_slova += slovo #ako to slovo nije duplikat ili nije nadjeno do sad pise se u niz

    if nadjeno==0: broj_pogresenih += 1

def nova_igra(): #pocinje se nova igra
    global niz_pogodjenih_slova
    niz_pogodjenih_slova = ""
    
    global broj_pogresenih
    broj_pogresenih = 0

    global broj_pogodjenih
    broj_pogodjenih = 0

    global rec
    rec = nova_rec()

def zastita_unosa(): #zastita unosa
    temp = ''
    while len(temp)!=1 or not temp.isalpha(): #sve dok se ne unese jedno slovo ili -1 za kraj
        temp = input("\n(-1 za kraj) Unesite sledece slovo: ")
        if temp=='-1': break # ako korisnik zeli kraj
        if niz_pogodjenih_slova.find(temp.upper())!=-1:  #proveravamo da li je uneto slovo vec pokusano
            print("Ovo slovo je vec pogodjeno!")
            temp = ''

    if temp.isalpha():
        temp = temp.upper() #postavljamo da uneto slovo bude veliko jer su sve reci u dictionary.txt napisana velikim slovima
    return temp

def provera_kraj():
    if broj_pogresenih == 6:
        print("Niste pogodili rec!")
        print("Zamisljena rec je: " + rec + "\n")
        input("Pritisnite enter da nastavite. ")
        return True #ako je kraj
    elif broj_pogodjenih == len(rec):
        print("Pogodili ste!")
        print("Zamisljena rec je: " + rec + "\n")
        input("Pritisnite enter da nastavite. ")
        return True #ako je kraj
    return False #ako nije kraj


#glavni deo programa
unos=''
nova_igra()

while True:
    ispis_hangamana()
    ispis_pogodjenih()
    if provera_kraj():
        nova_igra()
        continue
    unos = zastita_unosa()
    if unos=='-1': break
    provera_pogodjenih(unos)