from readline import append_history_file
from admin_funckije import blokiranje_korisnika
from globalne_promenljive import *
from rad_sa_sistemom_i_korisnicima import izlaz
import datetime

def ucitavanje_korisnika(): # funkcija koja ucitava sve korisnike
    try:
        fajl = open('assets/korisnici.txt', 'r', encoding='utf-8')
    except IOError:
        print('Problem sa otvaranjem fajla korisnici.txt')
        return

    for linija in fajl.readlines():
        korisnik = {}
        linija = linija.split('|')

        if len(linija) !=8:
            print('Nepotpun korisnik')
            return

        korisnik['username'] = linija[0]
        korisnik['password'] = linija[1]
        korisnik['ime'] = linija[2]
        korisnik['prezime'] = linija[3]
        korisnik['pol'] = linija[4].upper()
        korisnik['telefon'] = linija[5].replace('/', '').replace('-', '').replace(' ', '')
        korisnik['email'] = linija[6]
        korisnik['uloga'] = linija[7].upper().replace('\n', '')
        korisnici[korisnik['username']] = korisnik

    fajl.close()

def ucitavanje_dodatne_opereme():
    try:
        fajl = open('assets/dodatna_oprema.txt', encoding='utf-8')
    except IOError:
        print('Fajl dodatna_oprema.txt ne moze da se otvori!')
        return

    global dodatna_oprema

    for linija in fajl.readlines():
        linija = linija.split('|')
        dodatna_oprema[linija[0]] = linija[1].replace('\n', '')

    fajl.close()

def ucitavanje_apartmana(): # funkcija koja ucitava apartmane
    try:
        fajl = open('assets/apartmani.txt', 'r', encoding='utf-8')
    except IOError:
        print('Problem sa otvaranjem fajla!')
        return
    
    for linija in fajl.readlines():
        apartman = {}
        linija = linija.split('|')

        if len(linija) !=10:
            print('Nepotpun apartman')
            return

        apartman['sifra'] = linija[0]
        apartman['tip'] = linija[1].upper()
        apartman['broj_soba'] = linija[2]
        apartman['broj_gostiju'] = linija[3]
        apartman['adresa'] = linija[4]
        apartman['dostupnost'] = linija[5]
        apartman['domacin'] = linija[6]
        apartman['cena'] = linija[7]
        apartman['status'] = linija[8].upper()
        apartman['sadrzaj'] = linija[9].replace('\n', '')
        apartmani[apartman['sifra']] = apartman

    fajl.close()

def ucitavanje_rezervacija():
    try:
        fajl = open('assets/rezervacije.txt', 'r')
    except IOError:
        print('Problem sa otvaranjem fajla rezervacije.txt!')
        return
    
    for linija in fajl.readlines():
        linija = linija.split('|')
        rezervacija = {}


        rezervacija['sifra'] = linija[0]
        rezervacija['apartman'] = linija[1]
        rezervacija['pocetni_datum'] = linija[2]
        rezervacija['broj_nocenja'] = linija[3]
        rezervacija['ukupna_cena'] = linija[4]
        rezervacija['gost'] = linija[5]
        rezervacija['dodatni_gosti'] = linija[6]
        rezervacija['status'] = linija[7].upper().replace('\n', '')
        rezervacije[rezervacija['sifra']] = rezervacija

    fajl.close()

def ucitavanje_neradnih_dana():
    try:
        fajl = open('assets/neradni_dani.txt', 'r')
    except IOError:
        print('Problem sa otvaranjem fajla \'neradni_dani.txt\'!')
        izlaz()

    global neradni_dani

    temp = fajl.readlines()
    for datum in temp:
        datum = datum.replace('placeholder', str(datetime.datetime.now().year)).replace('\n', '')
        neradni_dani.append(datum)