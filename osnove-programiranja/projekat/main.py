import os
import datetime
from tabulate import tabulate

from rad_sa_rezervacijama import ponistavanje_rezervacije, potvrda_odbijanje_rezervacija
from ucitavanja import *
from rad_sa_apartmanima import *
from pregled_ispis import *
from rad_sa_sistemom_i_korisnicima import *
from admin_funckije import *
from lifecycle import *
from globalne_promenljive import *

neulogovan_opcije = ['1', '2', '3', '4', '5', '6', '7']
gost_opcije = ['2', '3', '4', '5', '6', '8', '9', '10', '11']
domacin_opcije = ['2', '3', '4', '5', '6', '8', '12', '13', '14', '15', '16']
admin_opcije = ['2', '3', '4', '5', '6', '8', '17', '18', '19', '20', '21', '22']

dict_opcija = {
    '1': 'Prijava na stistem',
    '2': 'Izlazak iz aplikacije',
    '3': 'Pregled aktivnih apartmana',
    '4': 'Pretraga apartmana',
    '5': 'Visekriterijumska pretraga apartmana',
    '6': 'Prikaz 10 najpopularnijih gradova',
    '7': 'Registracija',
    '8': 'Odjava sa sistema',
    '9': 'Rezervisanje apartmana',
    '10': 'Pregled licnih rezervacija',
    '11': 'Ponistavanja rezervacija',
    '12': 'Dodavanje apartmana',
    '13': 'Izmena podataka o apartmanu',
    '14': 'Brisanje apartmana',
    '15': 'Pregled rezervacija',
    '16': 'Potvrda ili odbijanje rezervacija',
    '17': 'Pretraga rezervacija',
    '18': 'Registracija novih domacina',
    '19': 'Kreiranje dodatne opreme',
    '20': 'Brisanje dodatne opreme',
    '21': 'Blokiranje korisnika',
    '22': 'Izvestavanje'
}

def menu():
    opcija = ''
    while opcija != '2':
        os.system('cls' if os.name=='nt' else 'clear')
        radne_opcije = [] # opcije koje ce se ispisivati u zavinosti od trenutnog korisnika
        if len(ulogovanKorisnik) == 0:
            radne_opcije = neulogovan_opcije
        elif ulogovanKorisnik['uloga'] == 'GOST':
            radne_opcije = gost_opcije
        elif ulogovanKorisnik['uloga'] == 'DOMACIN':
            radne_opcije = domacin_opcije
        else:
            radne_opcije = admin_opcije 
        
        if len(ulogovanKorisnik) > 0:
            print('Ulogovan korisnik:', ulogovanKorisnik['username'])
        else:
            print('Korisnik nije ulogovan!')
        print('-'*30)
        print('Dostupne opcije:')
        for key in radne_opcije:
            print(key + ')', dict_opcija[key])
        print('-'*30)
        print()
        
        while True: # unos opcije
            opcija = input('Unesite jednu od navedenih opcija: ')
            if not opcija in radne_opcije:
                print('Neispravan unos, pokusajte ponovo!\n')
            else:
                break
        
        if opcija == '1':
            prijava_na_sistem()
        elif opcija == '2':
            izlaz()
        elif opcija == '3':
            pregled_aktivnih_apartmana()
        elif opcija == '4':
            pretraga(0)
        elif opcija == '5':
            pretraga(1, neaktivni=True) 
        elif opcija == '6':
            najpopularniji_gradovi()
        elif opcija == '7':
            registracija()
        elif opcija == '8':
            odjava_sa_sistema()
        elif opcija == '9':
            rezervisanje_apartmana()
        elif opcija == '10':
            pregled_rezervacija_korisnika()
        elif opcija == '11':
            ponistavanje_rezervacije()
        elif opcija == '12':
            dodavanje_aprtamana()
        elif opcija == '13':
            izmena_podataka_apartmana()
        elif opcija == '14':
            brisanje_apartmana()
        elif opcija == '15':
            pregled_rezervacija()
        elif opcija == '16':
            potvrda_odbijanje_rezervacija()
        elif opcija == '17':
            pretraga_rezervacija()
        elif opcija == '18':
            registracija_novih_domacina()
        elif opcija == '19':
            kreiranje_dodatne_opreme()
        elif opcija == '20':
            brisanje_dodatne_opreme()
        elif opcija == '21':
            blokiranje_korisnika()
        else: # opcija == '22'
            admin_izvestavanje()
        input('\nPritisnite enter da nastavite')

if __name__ == '__main__':
    ucitavanje_korisnika()
    ucitavanje_dodatne_opereme()
    ucitavanje_apartmana()
    ucitavanje_rezervacija()
    ucitavanje_neradnih_dana()
    auto_odbijanje_rezervacija()
    auto_update_dostupnost()
    sortiranje_opsega()
    menu()