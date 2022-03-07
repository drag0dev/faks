from email import header
import os
from tabulate import tabulate
from funckije_postojanje import username_postoji
from globalne_promenljive import *

def pregled_aktivnih_apartmana(apart=apartmani, neaktivni=False, domacin=''):
    os.system('cls' if os.name=='nt' else 'clear')
    temp = []
    headers=['Sifra', 'Tip', 'Broj soba', 'Broj osoba', 'Adresa', 'Cena po noci', 'Dostupnost', 'Status']
    for key in apart:
        if apart[key]['status'] == 'NEAKTIVNO' and not neaktivni:
            continue
        if domacin!='' and apart[key]['domacin'] != domacin:
            continue
        new_apart = []
        new_apart.append(apart[key]['sifra'])
        new_apart.append(apart[key]['tip'])
        new_apart.append(apart[key]['broj_soba'])
        new_apart.append(apart[key]['broj_gostiju'])
        new_apart.append(apart[key]['adresa'])
        new_apart.append(apart[key]['cena'])

        novi_str = ''
        dostupnost = apart[key]['dostupnost'].split(' ')
        if len(dostupnost) <= 2:
            novi_str = apart[key]['dostupnost']
        else:
            novi_str += dostupnost[0]
            novi_str += ' '
            novi_str += dostupnost[1]
        new_apart.append(novi_str)
        new_apart.append(apart[key]['status'])
        temp.append(new_apart)

    print(tabulate(temp, headers))


def najpopularniji_gradovi():
    lista = {}
    for key in rezervacije.keys(): # brojanje rezervacija za svaki grad
        if rezervacije[key]['status']== 'ODBIJENA' or  rezervacije[key]['status']== 'ODUSTANAK':
            continue
        grad = apartmani[rezervacije[key]['apartman']]['adresa'].split(', ')[1] # ime grada
        if grad in lista.keys():
            lista[grad] +=1
        else:
            lista[grad] = 1
    
    # sortiranje liste najpopularnijih gradova
    niz_keyeva = list(lista.keys())
    for i in range(len(niz_keyeva)):
        for j in range(len(niz_keyeva)-1):
            if lista[niz_keyeva[j]] < lista[niz_keyeva[j+1]]:
                temp = niz_keyeva[j]
                niz_keyeva[j] = niz_keyeva[j+1]
                niz_keyeva[j+1] = temp

    print('\n10 Najpopularnijih gradova:')
    for i in range(10):
        if i==len(niz_keyeva): break
        print(str(i+1) + '.', niz_keyeva[i] + ':', lista[niz_keyeva[i]])


def pregled_rezervacija_korisnika():
    username = ulogovanKorisnik['username']
    os.system('cls' if os.name=='nt' else 'clear')
    print('Rezervacije korisnika \''+ username +'\':')

    headers = ['Sifra', 'Apartman', 'Pocetni datum', 'Broj nocenja', 'Ukupna cena', 'Status']
    temp = []

    for key in rezervacije.keys():
        if rezervacije[key]['gost'] == username:
            rezervacija_za_ispis = []
            rezervacija_za_ispis.append(rezervacije[key]['sifra'])
            rezervacija_za_ispis.append(rezervacije[key]['apartman'])
            rezervacija_za_ispis.append(rezervacije[key]['pocetni_datum'])
            rezervacija_za_ispis.append(rezervacije[key]['broj_nocenja'])
            rezervacija_za_ispis.append(rezervacije[key]['ukupna_cena'])
            rezervacija_za_ispis.append(rezervacije[key]['status'])
            temp.append(rezervacija_za_ispis)
    
    print(tabulate(temp, headers))

def pregled_rezervacija():
    temp = [] # sve rezervacije za apartmane ulogovanog domacina
    os.system('cls' if os.name=='nt' else 'clear')
    for key in rezervacije.keys():
        if apartmani[rezervacije[key]['apartman']]['domacin'] == ulogovanKorisnik['username'] and rezervacije[key]['status'] == 'KREIRANA':
            modified_rez = []
            modified_rez.append(key)
            modified_rez.append(rezervacije[key]['apartman'])
            modified_rez.append(rezervacije[key]['pocetni_datum'])
            modified_rez.append(rezervacije[key]['broj_nocenja'])
            modified_rez.append(rezervacije[key]['ukupna_cena'])
            modified_rez.append(rezervacije[key]['gost'])
            temp.append(modified_rez)

    headers = ['sifra', 'Apartman', 'Pocetni datum', 'Broj nocenja', 'Ukupna cena', 'Gost']
    print(tabulate(temp, headers))

def ispis_dodatne_opreme():
    print()
    headers = ['Kljuc', 'Opis']
    za_ispis = []
    for key in dodatna_oprema.keys():
        temp = []
        temp.append(key)
        temp.append(dodatna_oprema[key])
        za_ispis.append(temp)

    print(tabulate(za_ispis, headers))
    print()
