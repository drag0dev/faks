from random import random, seed
from random import randint

seed(1)
unos = -1
#1-kamen, 2-papir, 3-makaze
broj_racunar_pobedjenih = 0
broj_korisnik_pobedjenih = 0
broj_neresenih = 0
while 1:
    print("------------------------------------")
    print("Korisnik je pobedio: %d" % broj_korisnik_pobedjenih)
    print("Racunar je pobedio: %d" % broj_racunar_pobedjenih)
    print("Broj neresenih: %d"%broj_neresenih)
    print("------------------------------------")
    while unos < 1 or unos > 4:
        unos = eval(input("Unesite broj 1-kamen, 2-papir, 3-makaze, 4-izlaz: "))
    if(unos==4):
        break
    pokusaj_racunar = randint(1,3)
    print("Pokusaj racunara je: ", pokusaj_racunar)
    if(unos == pokusaj_racunar):
        print("Racunar i korisnik su izabrali isto.")
        broj_neresenih = broj_neresenih +1
    elif(unos == 1 and pokusaj_racunar == 2):
        print("Korisnik gubi.")
        broj_racunar_pobedjenih = broj_racunar_pobedjenih +1
    elif(unos == 1 and pokusaj_racunar == 3):
        print("Korisnik je pobedio.")
        broj_korisnik_pobedjenih = broj_korisnik_pobedjenih + 1
    elif(unos == 2 and pokusaj_racunar == 1):
        print("Korisnik je pobedio.")
        broj_korisnik_pobedjenih = broj_korisnik_pobedjenih + 1
    elif(unos == 2 and pokusaj_racunar == 3):
        print("Korisnik gubi.")
        broj_racunar_pobedjenih = broj_racunar_pobedjenih +1
    elif(unos == 3 and pokusaj_racunar == 1):
        print("Korisnik gubi.")
        broj_racunar_pobedjenih = broj_racunar_pobedjenih +1
    elif(unos == 3 and pokusaj_racunar == 2):
        print("Korisinik je pobedio.")
        broj_korisnik_pobedjenih = broj_korisnik_pobedjenih + 1
    unos = -1