import os
from funckije_postojanje import email_postoji, username_postoji
from globalne_promenljive import *
from validacija import *

def izlaz():
    zapis_u_fajl()
    quit()


def prijava_na_sistem():
    os.system('cls' if os.name=='nt' else 'clear')
    username = ''
    password = ''
    korisnikNadjen = 0 # 0 - nije nadjen, 1 - pogresna sifra, 2- prijavljen
    temp = {}

    print('Prijava')
    print('Unesite -1 za prekid!')
    while True:
        korisnikNadjen = 0
        print('-'*30)
        while not username:
            username = input('Unesite korisnicko ime: ')
        if username == '-1':
            return

        while not password:
            password = input('Unesite lozniku: ')
        if password == '-1':
            return
        
        for key in korisnici:
            if korisnici[key]['username']==username:
                if korisnici[key]['password'] == password:
                    korisnikNadjen = 2
                    temp = korisnici[key]
                    break
                else:
                    korisnikNadjen = 1
                    break

        if korisnikNadjen == 0: # ako nije nadjen username
            print('Korisnik sa usernameom \''+ username+ '\' nije nadjen!')
            print('Pokusajte ponovo!')
        if korisnikNadjen == 1: # ako je pogresna sifra
            print('Pogresna sifra!')
            print('Pokusajte ponovo!')
        if korisnikNadjen == 2: # ako je username password tacno
            print('Uspesno prijavljeni!')
            break

        username = ''
        password = ''
        korisnikNadjen = 0
    ulogovanKorisnik.update(temp)


def registracija():
    novi_korisnik = {}

    username = ''
    while True:
        username = input('\nUnesite korisnicko ime: ')
        if not validacija_slova(username):
            print('Nevalidan usernanem, pokusajte ponovo!')
        elif username_postoji(username):
            print('Username vec postoji, pokusajte ponovo!')
        else: break
    novi_korisnik['username'] = username

    password = ''
    while True:
        password = input('\nUnesite lozinku: ')
        if not validacija_slova(password):
            print('Nevalidna sifra, pokusajte ponovo!')
        else: break
    novi_korisnik['password'] = password

    ime = ''
    while True:
        ime = input('\nUnesite vase ime: ')
        if not ime or not ime.isalpha():
            print('Nevalidno ime, pokusajte ponovo!')
        else: break
    novi_korisnik['ime'] = ime

    prezime = ''
    while True:
        prezime = input('\nUnesite vase prezime: ')
        if not prezime or not prezime.isalpha():
            print('Nevalidno ime, pokusajte ponovo!')
        else: break
    novi_korisnik['prezime'] = prezime

    pol = ''
    while True:
        pol = input('\nUnesite vas pol m-musko, z-zensko, d-drugo: ')
        if not pol or (pol.upper()!='M' and pol.upper()!='Z' and pol.upper()!='D'):
            print('Nevalidan pol, pokusajte ponovo!')
        else: break
    novi_korisnik['pol'] = pol

    telefon = ''
    while True:
        telefon = input('\nUnesite vas broj telefon: ').replace('-', '').replace(' ', '').replace('/', '')
        if not telefon or not telefon.isnumeric():
            print('Nevalidan broj telefon, pokusajte ponovo!')
        else: break
    novi_korisnik['telefon'] = telefon

    email = ''
    while True:
        email = input('\nUnesite vasu email adresu: ')
        if not validacija_email(email):
            print('Neispravan unos, pokusajte ponovo!')
        else: break
    novi_korisnik['email'] = email

    novi_korisnik['uloga'] = 'GOST'
    
    korisnici[novi_korisnik['username']] = novi_korisnik
    ulogovanKorisnik.update(novi_korisnik)

def odjava_sa_sistema():
    ulogovanKorisnik.clear()

def zapis_u_fajl():
    # zapis korisnika
    try:
        fajl = open('assets/korisnici.txt', 'w')
    except IOError:
        print('Problem sa otvaranjem fajla \'korisnici.txt\'!')
        return
    
    for key in korisnici:
        temp = ''
        temp += korisnici[key]['username'] + '|'
        temp += korisnici[key]['password'] + '|'
        temp += korisnici[key]['ime'] + '|'
        temp += korisnici[key]['prezime'] + '|'
        temp += korisnici[key]['pol'] + '|'
        temp += korisnici[key]['telefon'] + '|'
        temp += korisnici[key]['email'] + '|'
        temp += korisnici[key]['uloga'] + '\n'
        fajl.writelines(temp)
    fajl.close()

    # zapis dodatne opreme
    try:
        fajl = open('assets/dodatna_oprema.txt', 'w')
    except IOError:
        print('Problem sa otvaranjem fajl \'dodatna_operma.txt!\'')
        return
    for key in dodatna_oprema:
        temp = ''
        temp += key + '|'
        temp += dodatna_oprema[key] + '\n'
        fajl.writelines(temp)
    fajl.close()

    # zapis apartmana
    try:
        fajl = open('assets/apartmani.txt', 'w')
    except IOError:
        print('Problem sa otvaranjem fajla \'apartmani.txt\'')
        return
    for key in apartmani:
        temp = ''
        temp += apartmani[key]['sifra'] + '|'
        temp += apartmani[key]['tip'] + '|'
        temp += apartmani[key]['broj_soba'] + '|'
        temp += apartmani[key]['broj_gostiju'] + '|'
        temp += apartmani[key]['adresa'] + '|'
        temp += apartmani[key]['dostupnost'] + '|'
        temp += apartmani[key]['domacin'] + '|'
        temp += apartmani[key]['cena'] + '|'
        temp += apartmani[key]['status'] + '|'
        temp += apartmani[key]['sadrzaj'] + '\n'
        fajl.writelines(temp)
    fajl.close()

    # zapis rezervacija
    try: 
        fajl = open('assets/rezervacije.txt', 'w')
    except IOError:
        print('Problem sa otvaravnjem fajla \'rezervacije.txt\'')
        return
    for key in rezervacije:
        temp = ''
        temp += rezervacije[key]['sifra'] + '|'
        temp += rezervacije[key]['apartman'] + '|'
        temp += rezervacije[key]['pocetni_datum'] + '|'
        temp += rezervacije[key]['broj_nocenja'] + '|'
        temp += rezervacije[key]['ukupna_cena'] + '|'
        temp += rezervacije[key]['gost'] + '|'
        temp += rezervacije[key]['dodatni_gosti'] + '|'
        temp += rezervacije[key]['status'] + '\n'
        fajl.writelines(temp)
    fajl.close()