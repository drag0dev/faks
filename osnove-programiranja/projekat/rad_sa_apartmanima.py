import datetime
import os
from unittest.util import sorted_list_difference
from tabulate import tabulate
from funckije_postojanje import domacin_postoji, sifra_apartmana_postoji
from lifecycle import sortiranje_opsega
from pregled_ispis import ispis_dodatne_opreme, pregled_aktivnih_apartmana
from globalne_promenljive import *
from rad_sa_rezervacijama import brisanje_rezervacija
from rad_sa_sistemom_i_korisnicima import odjava_sa_sistema
from validacija import praznicni_dan, validacija_adresa, validacija_email, vikend

def unos_parametara(str):
    print('\nKod parametara koji uzimaju broj napisite v za vece od ili m za manje od pre broja praceno razmakom\nili za egzaktno pretragu e')
    parameti = ['prefiksno ili puno ime mesta:', 'vreme dostupnosti u obliku dan/mesec/godina:',
                '']
    # unos mesta
    mesto = ''
    if '1' in str:
        while True:
            mesto = input('\nUnesite prefiskno ili puno ime mesta: ')
            if not mesto.replace(' ', '').isalpha():
                print('Unesite pravilno ime mesta!')
            else: break
    
    vreme_dostupnosti = ''
    if '2' in str:
        while True:
            vreme_dostupnosti = input('\nUnesite vreme dostupnosti: ').upper()
            temp = vreme_dostupnosti.split(' ')
            if len(temp)!=2:
                print('Neispravan unos, pokusajte ponovo!')
            elif temp[0].upper()!='M' and temp[0].upper() != 'V' and temp[0].upper() !='E':
                print('Neispravan unos, pokusajte ponovo!')
            elif not temp[1].isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
            else: break
   
    broj_soba = ''
    if '3' in str:
        while True:
            broj_soba = input('\nUnesite broj soba: ').upper()
            temp = broj_soba.split(' ')
            if len(temp)!=2:
                print('Neispravan unos, pokusajte ponovo!')
            elif temp[0].upper()!='M' and temp[0].upper() != 'V' and temp[0].upper() !='E':
                print('Neispravan unos, pokusajte ponovo!')
            elif not temp[1].isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
            else: break
   
    broj_osoba = ''
    if '4' in str:
        while True:
            broj_osoba = input('\nUnesite broj osoba: ').upper()
            temp = broj_osoba.split(' ')
            if len(temp)!=2:
                print('Neispravan unos, pokusajte ponovo!')
            elif temp[0].upper()!='M' and temp[0].upper() != 'V' and temp[0].upper() !='E':
                print('Neispravan unos, pokusajte ponovo!')
            elif not temp[1].isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
            else: break

    cena = ''
    if '5' in str:
        while True:
            cena = input('\nUnesite cenu: ').upper()
            temp = cena.split(' ')
            if len(temp)!=2:
                print('Neispravan unos, pokusajte ponovo!')
            elif temp[0].upper()!='M' and temp[0].upper() != 'V' and temp[0].upper() !='E':
                print('Neispravan unos, pokusajte ponovo!')
            elif not temp[1].isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
            else: break
    return mesto, vreme_dostupnosti, broj_soba, broj_osoba, cena

def pretraga(vrsta, neaktivni=False): # 0 jedan parametar pretrage, 1 vise parametara pretrage
    if vrsta==1:
        while True:
            opcije = ['1', '2', '3', '4', '5']
            print('\n1 - Ime Mesta, 2 - Vreme dostupnosti, 3 - Broj soba, 4 - Broj osoba, 5 - Cena')
            str = input('Unesite broj parametara koje zelite da koristie za pretragu: ').replace(' ', '')
            validan = True
            for karakter in str:
                if not karakter in opcije:
                    print('Neispravan unos, pokusajte ponovo!')
                    validan = False
                    break
            if validan:
                break 

    elif vrsta==0:
        while True:
            opcije = ['1', '2', '3', '4', '5']
            print('1 - Ime Mesta, 2 - Vreme dostupnosti, 3 - Broj soba, 4 - Broj osoba, 5 - Cena')
            str = input('Unesite broj parametara koje zelite da koristie za pretragu: ').replace(' ', '')
            if str in opcije:
                break
            else:
                print('Neispravan unos, pokusajte ponovo!')
    


    mesto, vreme_dostupnosti, broj_soba, broj_osoba, cena = unos_parametara(str) 
    temp = list(apartmani.keys())
    if '1' in str: # mesto
        for key in temp.copy():
            apart_mesto = apartmani[key]['adresa'].split(', ')[1] # pristup imenu mesta
            if not apart_mesto.upper().startswith(mesto.upper()):
                temp.remove(key)

    if '2' in str: # vreme dostupnosti
        trazeniBroj = int(vreme_dostupnosti.split(' ')[1]) # broj koji je korisnik uneo
        for key in temp.copy():
            nadjen = False
            opsezi = apartmani[key]['dostupnost'].split(' ')
            for opseg in opsezi:
                if len(opseg) == 0 :
                    break
                opseg = opseg.split('-')
                delta =  datetime.datetime.strptime(opseg[1],'%d/%m/%Y') - datetime.datetime.strptime(opseg[0],'%d/%m/%Y')
                delta = delta.days
                if ('E' in vreme_dostupnosti) and (delta==trazeniBroj):
                    nadjen = True
                    break
                elif ('V' in vreme_dostupnosti) and (delta>trazeniBroj):
                    nadjen = True
                    break
                elif ('M' in vreme_dostupnosti) and (delta<trazeniBroj):
                    nadjen = True 
                    break
            if not nadjen:
                temp.remove(key)

    if '3' in str: # broj_soba
        trazeniBroj = int(broj_soba.split(' ')[1]) # broj koji je korisnik uneo
        for key in temp.copy():
            broj_soba_apartman = int(apartmani[key]['broj_soba'])
            if ('E' in broj_soba) and (broj_soba_apartman!=trazeniBroj):
                    temp.remove(key)
            elif ('V' in broj_soba) and (broj_soba_apartman<=trazeniBroj):
                    temp.remove(key)
            elif ('M' in broj_soba) and (broj_soba_apartman>=trazeniBroj):
                    temp.remove(key)

    if '4' in str: # broj osoba
        trazeniBroj = int(broj_osoba.split(' ')[1]) # broj koji je korisnik uneo
        for key in temp.copy():
            broj_osoba_apartman = int(apartmani[key]['broj_gostiju'])
            if ('E' in broj_osoba) and (broj_osoba_apartman!=trazeniBroj):
                    temp.remove(key)
            elif ('V' in broj_osoba) and (broj_osoba_apartman<=trazeniBroj):
                    temp.remove(key)
            elif ('M' in broj_osoba) and (broj_osoba_apartman>=trazeniBroj):
                    temp.remove(key)

    if '5' in str: # cena
        trazeniBroj = int(cena.split(' ')[1]) # broj koji je korisnik uneo
        for key in temp.copy():
            cena_apartman = int(apartmani[key]['cena'])
            if ('E' in cena) and (cena_apartman!=trazeniBroj):
                    temp.remove(key)
            elif ('V' in cena) and (cena_apartman<=trazeniBroj):
                    temp.remove(key)
            elif ('M' in cena) and (cena_apartman>=trazeniBroj):
                    temp.remove(key)
    print('Prikaz apartmana prema unetim parametrima:')
    
    novi_apartmani = {}
    for key in temp:
        novi_apartmani[key] = apartmani[key]

    pregled_aktivnih_apartmana(novi_apartmani, neaktivni)

def rezervisanje_apartmana():
    os.system('cls' if os.name=='nt' else 'clear')
    prethodna_rezervacija = False
    while True:
        nova_rezervacija = {}
        # odabir apartmana
        while True:
            sifra = ''
            sifra = input('\nUnesite sifru apartmana koji zelite da rezervisete ili ostavite prazno da bi pretrazili apartmane ili -1 za prekid: ')
            if sifra == '-1':
                return
            elif sifra == '':
                pretraga(1, True) # vise parametarska pretraga
                continue
            if not sifra.isnumeric():
                print('Neispravna sifra, pokusajte ponovo!')
            elif not sifra_apartmana_postoji(sifra):
                print('Aprtman sa sifrom:', sifra, 'nepostoji!')
            else: break
        
        if apartmani[sifra]['status'] == 'NEAKTIVNO':
            print('Apartman nije aktivan!')
            return
        
        nova_rezervacija['apartman'] = sifra
        print()
        
        # ispis termina
        if not apartmani[sifra]['dostupnost']:
            print('Apartman nema dostupnih termina!')
            return
        
        termini = []

        today = datetime.datetime.today()
        for termin in apartmani[sifra]['dostupnost'].split(' '):
            pocetni_datum = datetime.datetime.strptime(termin.split('-')[0],'%d/%m/%Y')
            if pocetni_datum > today:
                termini.append(termin)

        if len(termini)==0:
            print('Nema dostupnih termina za dati apratman!')
            return

        i = 0
        today = datetime.datetime.today()
        print('Dostupni termini:')
        for termin in termini:
                termin_pocetak = datetime.datetime.strptime(termin.split('-')[0], '%d/%m/%Y')
                if (termin_pocetak - today) > datetime.timedelta(days=0) and (termin_pocetak - today) <= datetime.timedelta(days=31):
                    print(str(i+1) + '.', termin)
                    i += 1

        # odabir termina
        termin = ''
        while True:
            termin = input('\nUnesite redni broj termina: ')
            if not termin.isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
                continue
            elif int(termin)<1 or int(termin)>i:
                print('Neispravan unos, pokusajte ponovo!')
                continue
            else:
                break

        pocetni_datum = ''
        broj_dana = 0
        odabrani_termin = termini[int(termin)-1]

        # unos pocetnog datuma i broja nocenja
        while True:
            unos = ''
            unos = input('\nUnesite pocetni datum u obliku \'dd/mm/yyyy\' i broj nocenja razdvojeno razmakom: ')
            unos = unos.split(' ')
            if len(unos)!=2:
                print('Neispravan unos, pokusajte ponovo!')
                continue

            try:
                pocetni_datum = datetime.datetime.strptime(unos[0], '%d/%m/%Y')    
            except:
                print('Neispravan datum, pokusajte ponovo!')
                continue

            if not unos[1].isnumeric():
                print('Neispravan broj nocenja, pokusajte ponovo!')
                continue
            
            broj_nocenja = int(unos[1])
            pocetni_datum_dostupnosti = datetime.datetime.strptime(odabrani_termin.split('-')[0], '%d/%m/%Y')
            krajnji_datum_dostupnosti = datetime.datetime.strptime(odabrani_termin.split('-')[1], '%d/%m/%Y')
        
            if pocetni_datum < pocetni_datum_dostupnosti:
                print('Neispravan unos, pokusajte ponovo!')
            elif (pocetni_datum + datetime.timedelta(days=broj_nocenja)) > krajnji_datum_dostupnosti:
                print('Neispravan unos, pokusajte ponovo!')
            else:
                nova_rezervacija['pocetni_datum'] = datetime.datetime.strftime(pocetni_datum, '%d/%m/%Y')
                nova_rezervacija['broj_nocenja'] = str(broj_nocenja)
                break    



        # unos broja osoba
        broj_osoba = 0
        while True:
            broj_osoba = input('\nUkoliko dovodite jos osoba unesti broj u suprotnom ostavite prazno: ')
            if broj_osoba=='':
                broj_osoba = 0
                break
            elif not broj_osoba.isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
            elif int(broj_osoba) == 0:
                print('Neispravan unos, pokusajte ponovo!')
            else:
                broj_osoba_apartman = int(apartmani[sifra]['broj_gostiju'])
                broj_osoba = int(broj_osoba)
                if broj_osoba+1 > broj_osoba_apartman:
                    print('Apartman moze maksimalno da primi', broj_osoba_apartman, 'osoba!')
                    print('Pokusajte ponovo!')
                else:
                    break

        # unos dodatnih gostiju ako ih ima
        dodatni_gosti = ''
        if broj_osoba>0:
            for i in range(broj_osoba):
                while True:
                    ime_prezime = input('Unesite ime i prezime ' + str(i+1)+ '.' + ' gosta odvojeno razmakom: ')
                    ime_prezime = ime_prezime.split(' ')
                    if len(ime_prezime)!=2:
                        print('Neispravana unos, pokusajte ponovo!')
                    elif not ime_prezime[0].isalpha() and not ime_prezime[1].isalpha():
                        print('Neispravana unos, pokusajte ponovo!')
                    else:
                        dodatni_gosti += ime_prezime[0] + ' ' + ime_prezime[1] + ', '
                        break

        dodatni_gosti = dodatni_gosti[:-2] # skida se zadnji zarez
        nova_rezervacija['dodatni_gosti'] = dodatni_gosti
        broj_osoba += 1


        vikend_cena = 1
        neradni_dan = 1
        ukupna_cena = 0
        cena_po_noci = float(apartmani[sifra]['cena'])
        for broj in range(int(broj_nocenja)):
            neradni_dan = 1
            if praznicni_dan(pocetni_datum+datetime.timedelta(days=int(broj))):
                neradni_dan = 1.05
            if vikend_cena == 1  and vikend(pocetni_datum+datetime.timedelta(days=int(broj))):
                vikend_cena = 0.9
            
            ukupna_cena += cena_po_noci * neradni_dan

        ukupna_cena = ukupna_cena * vikend_cena
        if prethodna_rezervacija:
            ukupna_cena = ukupna_cena * 0.95

        nova_rezervacija['ukupna_cena'] = str(ukupna_cena)     
        
        nova_rezervacija['gost'] = ulogovanKorisnik['username']

        print()
        print('-'*30)
        print('Username gosta:', nova_rezervacija['gost'])
        print('Sifra apartmana:', nova_rezervacija['apartman'])
        print('Pocetni datum:', nova_rezervacija['pocetni_datum'])
        print('Broj nocenja:', nova_rezervacija['broj_nocenja'])
        print('Broj osoba:', broj_osoba)
        print('Ukupna cena:', nova_rezervacija['ukupna_cena'])
        if broj_osoba>1:
            print('Dodatni gosti:', nova_rezervacija['dodatni_gosti'])
        print('-'*30)

        opcija = ''
        while True:
            opcija = input('\nUnesite \'da\' da bi potvrdili ili \'ne\' da bi otkazali rezervaciju: ')
            if opcija.upper()=='DA':
                break
            elif opcija.upper()=='NE':
                return
            else:
                print('Neispravan unos, pokusajte ponovo!\n')

        nova_sifra = 0

        for sifra in rezervacije.keys():
            if int(sifra) > nova_sifra:
                nova_sifra = int(sifra)
        if nova_sifra != 1:
            nova_sifra +=1
        
        nova_rezervacija['sifra'] = str(nova_sifra)
        nova_rezervacija['status'] = 'KREIRANA'
        rezervacije[str(nova_sifra)] = nova_rezervacija
        primena_rezervacije_na_dostupnost(termini[int(termin)-1], nova_rezervacija['pocetni_datum'], nova_rezervacija['broj_nocenja'], nova_rezervacija['apartman'])

        prethodna_rezervacija = True

        nasatavak = True
        while True:
            unos = input('\nUnesite \'da\' ako zelite da nastavite da rezervisete, u suprotnom \'ne\': ').upper()
            if unos == 'DA':
                break
            elif unos == 'NE':
                nasatavak = False
                break
            else:
                print('Neispravan unos, pokusajte ponovo!')
        if not nasatavak:
            break


def primena_rezervacije_na_dostupnost(opseg, pocetni_datum, broj_dana, sifra_apartmana):
    broj_dana = datetime.timedelta(days=int(broj_dana))
    opseg = opseg.split('-')
    pocetni_datum = datetime.datetime.strptime(pocetni_datum, '%d/%m/%Y')
    pocetni_datum_dostupnosti = datetime.datetime.strptime(opseg[0], '%d/%m/%Y')
    krajnji_datum_dostupnosti = datetime.datetime.strptime(opseg[1], '%d/%m/%Y')

    delta = krajnji_datum_dostupnosti - pocetni_datum_dostupnosti
    novi_opseg = ''
    if delta == broj_dana: # pokriva ceo opseg
        novi_opseg = ''
    
    elif pocetni_datum == pocetni_datum_dostupnosti: # pocinje od pocetka opsega, zavrsava pre kraja opsega
        # print('|{}  |')
        novi_opseg = datetime.datetime.strftime((pocetni_datum + broj_dana).date(), '%d/%m/%Y') + '-' + datetime.datetime.strftime(krajnji_datum_dostupnosti.date(), '%d/%m/%Y')
    
    elif (pocetni_datum+broj_dana) == krajnji_datum_dostupnosti: # pocinje posle pocetka a zavrsava na kraj opega
        # print('|  {}|')
        novi_opseg = datetime.datetime.strftime(pocetni_datum_dostupnosti.date(), '%d/%m/%Y') + '-' + datetime.datetime.strftime(pocetni_datum.date(), '%d/%m/%Y')
    
    elif (pocetni_datum > pocetni_datum_dostupnosti) and ((pocetni_datum+broj_dana) < krajnji_datum_dostupnosti):
        # print('| {} |')
        # izmedju pocetka i kraj opsega
        opseg_jedan = datetime.datetime.strftime(pocetni_datum_dostupnosti.date(), '%d/%m/%Y') + '-' + datetime.datetime.strftime(pocetni_datum.date(), '%d/%m/%Y')
        opseg_dva = datetime.datetime.strftime((pocetni_datum+broj_dana).date(), '%d/%m/%Y') + '-' + datetime.datetime.strftime(krajnji_datum_dostupnosti.date(), '%d/%m/%Y')
        novi_opseg = opseg_jedan + ' ' + opseg_dva
    
    if not novi_opseg:
        apartmani[sifra_apartmana]['dostupnost'] = apartmani[sifra_apartmana]['dostupnost'].replace(opseg[0] + '-' + opseg[1], '')
    apartmani[sifra_apartmana]['dostupnost'] = apartmani[sifra_apartmana]['dostupnost'].replace(opseg[0]+'-'+opseg[1], novi_opseg)
    apartmani[sifra_apartmana]['dostupnost'] = ' '.join(apartmani[sifra_apartmana]['dostupnost'].split()) # brisanje visak razmaka

def dodavanje_aprtamana():
    print('Unos podataka za novi apartman:')

    novi_apartman = {}

    while True: # unos tipa apartmana
        unos = ''
        unos = input('\nApartman je ceo/soba?: ', ).upper()
        if unos=='CEO' or unos=='SOBA':
            novi_apartman['tip'] = unos
            break
        else:
            print('Neisparavan unos, pokusajte ponovo!')
            unos = ''

    while True: # unos broja soba
        unos = ''
        unos = input('\nUnesite broj soba: ', )
        if unos.isdigit():
            novi_apartman['broj_soba'] = unos
            break
        else:
            unos = ''
            print('Neispravan unos, pokusajte ponovo!')
            
    while True: # unos broja gostiju
        unos = ''
        unos = input('\nUnesite broj gostiju: ', )
        if unos.isdigit():
            novi_apartman['broj_gostiju'] = unos
            break
        else:
            print('Neisparavan unos, pokusajte ponovo!')
            unos = ''
    
    while True: # unos adrese
        unos = ''
        unos = input('\nUnesite adresu apartmana u formatu ulica broj, grad, postanski broj: ')
        if not validacija_adresa(unos):
            print('Neispravan unos, pokusajte ponovo!')
        else:
            novi_apartman['adresa'] = unos
            break

    opsezi = ''
    while True: # unos datuma dostupnosti
        unos = ''
        print('\nUnesite -1 ako zelite da prekinete unos datuma!')
        print('Dosada uneseni opsezi:', opsezi)
        unos = input('Unesite pocetni i krajnji datum razdvojeni razmakom izmedju (day/month/year) : ' )
        temp = unos.split(' ')

        if unos == '-1':
            if opsezi:
                opsezi = opsezi[:-1]
            novi_apartman['dostupnost'] = opsezi 
            break

        if len(temp) !=2:
            print('Neispravan unos, pokusajte ponovo!')
            continue
        pocetni_datum, kranji_datum = '', ''
        try: # provera pocetnog datuma
            pocetni_datum = datetime.datetime.strptime(temp[0], '%d/%m/%Y') 
        except:
            print('Uneti pocetni datum nije validan, pokusajte ponovo!')
            continue
            
        try: # provera krajnjeg datuma
            kranji_datum = datetime.datetime.strptime(temp[1], '%d/%m/%Y')
        except:
            print('Uneti krajnji datum nije validan, pokusajte ponovo!')
            continue

        zadatati_opsezi = opsezi.split(' ')
        nadjen = False
        for opseg in zadatati_opsezi: # provera da li se preklapa sa prethodno unesenim
            if len(opseg) == 0:
                continue
            pomocna = opseg.split('-')
            zadati_pocetni = datetime.datetime.strptime(pomocna[0], '%d/%m/%Y')
            zadati_krajnji = datetime.datetime.strptime(pomocna[1], '%d/%m/%Y')

            if kranji_datum > zadati_pocetni and kranji_datum <= zadati_krajnji: # {|}|
                nadjen = True
                break
            elif pocetni_datum >= zadati_pocetni and pocetni_datum < zadati_krajnji: # |{|}
                nadjen = True
                break

        if nadjen:
            print('Datumi se poklapaju sa prethodndim, pokusajte ponovo!')
            continue

        if pocetni_datum > kranji_datum:
            print('Kranji datum mora biti posle ili isti dan kao pocetni datum!')
            continue
        if pocetni_datum == kranji_datum:
            print('Razlika izmedju datuma mora biti najmanje jedan dan!')
            continue
        today = datetime.datetime.today()
        if pocetni_datum <= today:
            print('Pocetni datum mora biti od sutrasnjeg datuma nadalje!')
            continue

        if unos != '':
            opsezi += datetime.datetime.strftime(pocetni_datum, '%d/%m/%Y') + '-'
            opsezi += datetime.datetime.strftime(kranji_datum, '%d/%m/%Y') + ' '
    
    novi_apartman['domacin'] = ulogovanKorisnik['username']
    
    while True: # unos cene po noci
        unos = ''
        unos = input('\nUnesite cenu po noci sa tackom u slucaju decimalnog dela: ', )
        if unos.count('.')>1:
            print('Neispravan unos, pokusajte ponovo!')
            continue
        elif not unos.replace('.', '').isdigit():
            print('Neispravan unos, pokusajte ponovo!')
            continue
        else:
            novi_apartman['cena'] = unos
            break
    
    sadrzaj = ''
    while True: # unos sadrzaja aprtmana
        unos = ''
        print('\nOprema aprtmana se unosi jedan po jedan, za prekid unesite -1, za pregled opreme ostavite unos prazan!')
        unos = input('Unesite sifru opreme apartmana: ')

        if unos == '-1':
            novi_apartman['sadrzaj'] = sadrzaj[:-2] # izbacimo space i zarez na kraju
            break 

        if unos == '': # ispis opreme
            print('Pregled opreme:')
            ispis_dodatne_opreme()
            continue
        elif unos.isdigit() and (unos in dodatna_oprema.keys()):
                sadrzaj += unos + ', '
        else:
            print('Neispravan unos, pokusajte ponovo!')

    novi_apartman['status'] = 'NEAKTIVNO'
    nova_sifra = 0
    for key in apartmani.keys():
        if int(key) > nova_sifra:
            nova_sifra = int(key)
    if len(apartmani)==0:
        nova_sifra = 0
    elif len(apartmani)>0:
        nova_sifra +=1
    novi_apartman['sifra'] = str(nova_sifra)
    apartmani[str(nova_sifra)] = novi_apartman
    sortiranje_opsega()

def izmena_podataka_apartmana():
    sifra_apartmana = ''
    global ulogovanKorisnik
    while True:
        unos = ''
        unos = input('\nUnesite sifru apartmana, ostavite prazno za pretragu ili -1 za prekid: ')
        if unos == '-1':
            return
        elif unos == '':
            pregled_aktivnih_apartmana(domacin=ulogovanKorisnik['username'], neaktivni=True)
            continue
        
        elif not sifra_apartmana_postoji(unos):
            print('Unesena sifra ne postoji, pokusajte ponovo!')
            continue
        elif apartmani[unos]['domacin'] == ulogovanKorisnik['username']:
            sifra_apartmana = unos
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')
    
    temp_apartman = apartmani[sifra_apartmana]

    print('Ukoliko ne zelite da promenite neke od narednih podataka ostavite unos prazan!')

    while True: # unos tipa apartmana
        unos = ''
        unos = input('\nApartman je ceo/soba?: ', ).upper()
        if unos=='CEO' or unos=='SOBA':
            temp_apartman['tip'] = unos
            break
        elif unos == '':
            break
        else:
            print('Neisparavan unos, pokusajte ponovo!')
            unos = ''

    while True: # unos broja soba
        unos = ''
        unos = input('\nUnesite broj soba: ', )
        if unos.isdigit():
            temp_apartman['broj_soba'] = unos
            break
        elif unos == '':
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')
            
    while True: # unos broja gostiju
        unos = ''
        unos = input('\nUnesite broj gostiju: ', )
        if unos.isdigit():
            temp_apartman['broj_gostiju'] = unos
            break
        elif unos == '':
            break
        else:
            print('Neisparavan unos, pokusajte ponovo!')

    while True: # unos adrese
        unos = ''
        unos = input('\nUnesite adresu apartmana u formatu ulica broj, grad, postanski broj: ')
        if unos == '':
            break
        elif not validacija_adresa(unos):
            print('Neispravan unos, pokusajte ponovo!')
        else:
            temp_apartman['adresa'] = unos
            break

    opsezi = ''

    while True:
        unos = ''
        unos = input('\nAko zelite da obrisete trenutne datume dostupnoti unesite \'da\', u suprotnom \'ne\': ').upper()
        if unos == 'DA':
            break
        elif unos == 'NE':
            opsezi = temp_apartman['dostupnost']
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')

    while True: # unos datuma dostupnosti
        unos = ''
        print('\nUnesite -1 ako zelite da prekinete unos datuma!')
        print('Dosada uneseni opsezi:', opsezi)
        unos = input('Unesite pocetni i krajnji datum razdvojeni razmakom izmedju (day/month/year) : ' )
        temp = unos.split(' ')

        if unos == '':
            break

        if unos == '-1':
            temp_apartman['dostupnost'] = opsezi 
            break

        if len(temp) !=2:
            print('Neispravan unos, pokusajte ponovo!')
            continue
        pocetni_datum, kranji_datum = '', ''
        try: # provera pocetnog datuma
            pocetni_datum = datetime.datetime.strptime(temp[0], '%d/%m/%Y') 
        except:
            print('Uneti pocetni datum nije validan, pokusajte ponovo!')
            continue
            
        try: # provera krajnjeg datuma
            kranji_datum = datetime.datetime.strptime(temp[1], '%d/%m/%Y')
        except:
            print('Uneti krajnji datum nije validan, pokusajte ponovo!')
            continue

        zadatati_opsezi = opsezi.split(' ')
        nadjen = False
        for opseg in zadatati_opsezi: # provera da li se preklapa sa prethodno unesenim
            if len(opseg) == 0:
                continue
            pomocna = opseg.split('-')
            zadati_pocetni = datetime.datetime.strptime(pomocna[0], '%d/%m/%Y')
            zadati_krajnji = datetime.datetime.strptime(pomocna[1], '%d/%m/%Y')

            if kranji_datum > zadati_pocetni and kranji_datum <= zadati_krajnji: # {|}|
                nadjen = True
                break
            elif pocetni_datum >= zadati_pocetni and pocetni_datum < zadati_krajnji: # |{|}
                nadjen = True
                break

        if nadjen:
            print('Datumi se poklapaju sa prethodndim, pokusajte ponovo!')
            continue

        if pocetni_datum > kranji_datum:
            print('Kranji datum mora biti posle ili isti dan kao pocetni datum!')
            continue
        if pocetni_datum == kranji_datum:
            print('Razlika izmedju datuma mora biti najmanje jedan dan!')
            continue
        today = datetime.datetime.today()
        if pocetni_datum <= today:
            print('Pocetni datum mora biti od sutrasnjeg datuma nadalje!')
            continue

        if unos != '':
            if opsezi:
                opsezi += ' '
            opsezi += datetime.datetime.strftime(pocetni_datum, '%d/%m/%Y') + '-'
            opsezi += datetime.datetime.strftime(kranji_datum, '%d/%m/%Y')
    
    while True: # unos cene po noci
        unos = ''
        unos = input('\nUnesite cenu po noci sa tackom u slucaju decimalnog dela: ', )
        if unos == '':
            break
        if unos.count('.')>1:
            print('Neispravan unos, pokusajte ponovo!')
            continue
        elif not unos.replace('.', '').isdigit():
            print('Neispravan unos, pokusajte ponovo!')
            continue
        else:
            temp_apartman['cena'] = unos
            break
    
    sadrzaj = ''
    
    while True:
        unos = ''
        unos = input('\nUnesite \'da\' ako zelite da obrisete trenutnu opreamu apartmana, u suprotnom \'ne\': ').upper()
        if unos == 'DA':
            sadrzaj = ''
            break
        elif unos == 'NE':
            sadrzaj = temp_apartman['sadrzaj']
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')

    while True: # unos sadrzaja aprtmana
        unos = ''
        print('\nDosada unesena operma:', sadrzaj)
        print('Oprema aprtmana se unosi jedan po jedan, za prekid unesite -1, za pregled opreme unesite \'p\' prazan!')
        unos = input('Unesite sifru opreme apartmana: ')
        if unos == '-1':
            sadrzaj = ' '.join(sadrzaj.split())
            temp_apartman['sadrzaj'] = sadrzaj
            break 

        if unos == 'p' or unos == 'P': # ispis opreme
            print('Pregled opreme:')
            ispis_dodatne_opreme()
            continue
        if unos.isdigit():
            if not (unos in dodatna_oprema.keys()):
                print('Nepostojeca oprema, pokusajte ponovo!')
            elif unos in sadrzaj:
                print('Vec dodata dodatna oprema!')
            else:
                sadrzaj += ' ' + unos + ' '
                sadrzaj = ' '.join(sadrzaj.split())

    while True:
        print('\nTrenutno stanje apartmana je:', temp_apartman['status'])
        unos = ''
        unos = input('Ako zelite da obrnete stanje apartmana unesite \'da\' u suprotnom \'ne\': ').upper()
        if unos == 'NE':
            break
        if unos == 'DA':
            if temp_apartman['status'] == 'NEAKTIVNO': temp_apartman['status'] = 'AKTIVNO'
            else: temp_apartman['status'] = 'NEAKTIVNO'
            break

    apartmani[sifra_apartmana] = temp_apartman
    sortiranje_opsega()
    
def brisanje_apartmana():
    unos = ''
    while True: # unos sifre
        unos = ''
        unos = input('\nUnesite sifru apartman za brisanje, -1 za odustanak ili ostavite unos prazan za pretragu: ')
        if unos == '':
            pregled_aktivnih_apartmana(domacin=ulogovanKorisnik['username'])
            continue
        elif unos == '-1':
            return
        elif sifra_apartmana_postoji(unos) and apartmani[unos]['domacin'] == ulogovanKorisnik['username']:
            del apartmani[unos]
            break
    
    brisanje_rezervacija(unos)
    
    print('Apartman sa sifrom:', unos, 'obrisan!')