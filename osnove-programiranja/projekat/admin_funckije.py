from tabulate import tabulate
from funckije_postojanje import dodatna_oprema_postoji, domacin_postoji, nova_sifra
from globalne_promenljive import *
from rad_sa_rezervacijama import primena_odustanka_rezervacije_na_dostupnost 
from validacija import *
import os
import datetime 

def pretraga_rezervacija():        
    os.system('cls' if os.name=='nt' else 'clear')
    print('Pretraga rezervacija')
    print('-'*30)

    opcija = ''
    keyword = ''

    while True: # odabir opcije pretrage
        moguci_statusi = ['ODBIJENA', 'PRIHVACENA']
        print('\nPretraga rezervacija korisnika po:')
        print('0-statusu')
        print('1-adresi')
        print('2-korisnickom imenu domacina')
        unos = ''
        unos = input('Unesite redni broj opcije i vrednost po kojoj ce se traziti odvojenu razmakom: ')
        opcija = unos.split(' ')

        if len(opcija)!=2:
            print('Neispravan unos, pokusajte ponovo!')
            continue

        keyword = unos[len(opcija[0])+1:]
        if(len(keyword)==0):
            print('Neispravan unos, pokusajte ponovo!')

        elif opcija[0] == '0' and (keyword.upper() in moguci_statusi): 
            break
        elif opcija[0] == '1' or opcija[0] == '2':
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')
            
    # pretraga
    headers = ['Sifra', 'Pocetni datum', 'Broj nocenja', 'Ukupna cena', 'Gost']
    temp = []
    for key in rezervacije:
        modified_entry = []
        pomocna = {}

        if opcija[0] == '0':
            if rezervacije[key]['status'] == keyword.upper():
                pomocna.update(rezervacije[key])

        elif opcija[0] == '1':
            if keyword.upper() in apartmani[rezervacije[key]['apartman']]['adresa'].upper(): 
                pomocna.update(rezervacije[key])

        elif apartmani[rezervacije[key]['apartman']]['domacin'] == keyword:
                pomocna.update(rezervacije[key])
        
        if pomocna:
            modified_entry.append(key)
            modified_entry.append(pomocna['pocetni_datum'])
            modified_entry.append(pomocna['broj_nocenja'])
            modified_entry.append(pomocna['ukupna_cena'])
            modified_entry.append(pomocna['gost'])
            temp.append(modified_entry)
    print('\nKeywoard je: \'' + keyword + '\'')
    print(tabulate(temp, headers))

def registracija_novih_domacina():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Registracija novih dodmacina')
    print('-'*30)

    while True: # unos podatka domacina
        novi_domacin = {}
        while True: # unos korisnickog imena
            unos = ''
            unos = input('\nUnesite korisnicko ime domacina: ')
            if not unos.isalnum():
                print('Neispravan unos, pokusajte ponovo!') 
            elif domacin_postoji(unos):
                print('Domacin sa korisnickim imenom:', unos, 'vec postoji!')
            else:
                novi_domacin['username'] = unos
                break

        while True: # unos domacinove lozinke
            unos = ''
            unos = input('\nUnesite lozinku domacina: ')
            if unos:
                novi_domacin['password'] = unos
                break
            else:
                print('Neispravn unos, pokusajte ponovo!')
        
        while True: # unos imena
            unos = ''
            unos = input('\nUnesite ime domacin: ')
            if not unos.isalpha():
                print('Neispravan unos, pokusajte ponovo!')
            else:
                novi_domacin['ime'] = unos
                break

        while True: # unos prezimena
            unos = ''
            unos = input('\nUnesite prezime domacina: ')
            if not unos.isalpha():
                print('Neispravan unos, pokusajte ponovo!')
            else:
                novi_domacin['prezime'] = unos
                break

        while True: # unos pola
            unos = ''
            unos = input('\nUnesite pol domacina (m/z/d): ').upper()
            if unos == 'M' or unos == 'Z' or unos == 'D':
                novi_domacin['pol'] = unos
                break
            else:
                print('Neispravan unos, pokusajte ponovo!')
        
        while True: # unos broja telefona
            unos = ''
            unos = input('\nUnesite broj telefona domacina: ').replace('/', '').replace('-', '').replace(' ', '')
            if not unos.isnumeric():
                print('Neispravan unos, pokusajte ponovo!')
            else:
                novi_domacin['telefon'] = unos
                break

        while True: # unos emaila
            unos = ''
            unos = input('\nUnesite email adresu domacina: ')
            if not validacija_email(unos):
                print('Neispravan unos, pokusajte ponovo!')
            else:
                novi_domacin['email'] = unos
                break
        
        novi_domacin['uloga'] = 'DOMACIN'

        korisnici[novi_domacin['username']] = novi_domacin

        nastavak = True

        while True: # dalji unos domacina
            unos = ''
            unos = input('\nUnesite \'da\' ako zelite da unsete jos domacina, u suprotnom \'ne\': ').upper()
            if unos == 'NE':
                nastavak = False
                break
            elif unos == 'DA':
                nastavak = True 
                break
            else:
                print('Neispravan unos, pokusajte ponovo!')
            
        if not nastavak:
            break

def kreiranje_dodatne_opreme():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Kreiranje dodatne opreme')
    print('-'*30)
    
    while True: # unos nove opreme
        unos = ''
        unos = input('\nUnesite opis opreme: ')
        if not unos:
            print('Neisparavan unos, pokusajte ponovo!')
        else:
            if dodatna_oprema_postoji(unos):
                print('Dodatna oprema vec postoji!')
                continue
            sifra = nova_sifra(dodatna_oprema)
            dodatna_oprema[sifra] = unos
            
            nastavak = True
            while True: # jos operme
                unos = input('\nUnesite \'da\' ako zelite jos opreme da dodate, u suprotnom \'ne\': ').upper()
                if unos=='DA':
                    break
                elif unos=='NE':
                    nastavak = False
                    break
                else:
                    print('Neispravan unos, pokusajte ponovo!')
            
            if not nastavak:
                break

def brisanje_dodatne_opreme():
        os.system('cls' if os.name=='nt' else 'clear')
        print('Brisanje dodatne opreme')
        print('-'*30)
        headers = ['Sifra', 'Opis']

        # nalazenje opreme koja ne pripada ni jednom apartmanu
        modified_oprema = []
        kljucevi_opreme = list(dodatna_oprema.keys())

        for key in dodatna_oprema:
            for key_apartman in apartmani.keys():
                if key in apartmani[key_apartman]['sadrzaj']:
                    if key in kljucevi_opreme:
                        kljucevi_opreme.remove(key)

        for key in kljucevi_opreme:
            temp_oprema = []
            temp_oprema.append(key)
            temp_oprema.append(dodatna_oprema[key])
            modified_oprema.append(temp_oprema)
        
        if len(modified_oprema) == 0:
            print('Nepostoji oprema koja se ne koristi!')
            return
        
        print(tabulate(modified_oprema, headers))
        print('-'*30)
        
        while True: # unos sifre opreme     
            unos = ''
            unos = input('\nUnesite sifru opreme koju zelite da obrisete: ')

            if not unos:
                print('Neispravan unos, pokusajte ponovo!')
                continue

            nadjen = False
            index = 0

            for oprema in modified_oprema:
                if unos in oprema[0]:
                    nadjen = True
                    break
                index +=1 
            
            if nadjen:
                del dodatna_oprema[unos] 
                del modified_oprema[index]
            else:
                print('Neispravan unos, pokusajte ponovo!')
                continue

            nastavak = True

            while True: # da li se nastavlja
                unos = ''
                unos = input('\nUnesite \'da\' ako zelite da brisete jos opreme, u suprotnom \'ne\': ').upper()
                if unos=='DA':
                    break
                elif unos=='NE':
                    nastavak = False
                    break
                else:
                    print('Neispravan unos, pokusajte ponovo!')
            if not nastavak:
                break
            os.system('cls' if os.name=='nt' else 'clear')
            print(tabulate(modified_oprema, headers))
            print('-'*30)

def blokiranje_korisnika():
    os.system('cls' if os.name=='nt' else 'clear')
    print('Blokiranje korisnika')
    print('-'*30)

    headers = ['Korisnicko ime', 'Ime', 'Prezime']
    modified_korisnici = []
    for key in korisnici.keys():
        temp = []
        temp.append(korisnici[key]['username'])
        temp.append(korisnici[key]['ime'])
        temp.append(korisnici[key]['prezime'])
        modified_korisnici.append(temp)

    while True: # unos korisnickog imena korisnika   
        os.system('cls' if os.name=='nt' else 'clear')
        print(tabulate(modified_korisnici, headers))
        print('-'*30)

        unos = ''
        unos = input('\nUnesite korisnicko ime korisnika kojeg zelite da blokirate: ')

        if unos == ulogovanKorisnik['username']:
            print('Admin ne moze samog sebe da blokirati!')
        
        elif unos in korisnici.keys() and (korisnici[unos]['uloga'] == 'ADMIN'):
            print('Admini se ne mogu blokirati!')

        elif unos in korisnici.keys():
            brisanje_korisnika(unos)
            print('Korisnik:', unos, 'blokiran!')
            index = 0
            for korisnik in modified_korisnici:
                if korisnik[0] == unos:
                    break
                index += 1 
            modified_korisnici.pop(index)     
        else:
            print('Neispravan unos, pokusajte ponovo!')


        nastavak = True

        while True: # da li se nastavlja
            unos = ''
            unos = input('\nUnesite \'da\' da bi nastavili da blokirate korisnike, u suprotnom \'ne\': ').upper()
            if unos == 'DA':
                break
            elif unos == 'NE':
                nastavak = False
                break
            else:
                print('Neispravan unos, pokusajte ponovo!')
        
        if not nastavak:
            break

def brisanje_korisnika(kljuc):
    lista_kljuceva = []
    username_korisinka = korisnici[kljuc]['username']

    for key in rezervacije:
        if rezervacije[key]['gost'] == username_korisinka:
            lista_kljuceva.append(key)

    # brisu se sve rezervacije za datog korisnika
    for key in lista_kljuceva:
        primena_odustanka_rezervacije_na_dostupnost(rezervacije[key]['pocetni_datum'], rezervacije[key]['broj_nocenja'], rezervacije[key]['apartman'])
        del rezervacije[key]
        

    lista_kljuceva = []
    # ako je domacin brisu se apartmani i rezervacije za te apartmane
    if korisnici[kljuc]['uloga'] == 'DOMACIN':
        for key in rezervacije:
            if apartmani[rezervacije[key]['apartman']]['domacin'] == username_korisinka:
                lista_kljuceva.append(key)

        for key in lista_kljuceva:
            del rezervacije[key]

        lista_kljuceva = []
        for key in apartmani:
            if apartmani[key]['domacin'] == username_korisinka:
                lista_kljuceva.append(key)

        for key in lista_kljuceva:
            del apartmani[key]
    
    del korisnici[kljuc]

def admin_izvestavanje():
    os.system('cls' if os.name=='nt' else 'clear')
    opcije = 'ABCDEF'
    while True:
        while True: # unos opcije
            print('-'*30)
            print('a) lista potvrdjenih apartmana za izabran dan')
            print('b) lista potvrdjenih rezervisanih aparatmana za izabranog domacina')
            print('c) godisnji pregled angazovanja domacina')
            print('d) mesecni pregled angazovanja domacina')
            print('e) ukupan broj i cena potvrdjenih rezervacija na izbrani dan i izabranog domacina')
            print('f) pregled zastupljenosti pojedinacnih gradova u odnosu na ukupan broj rezervacija')
            print('-'*30)
            unos = ''
            unos = input('Unesite slovo izvestaja koje zelite da prikazete: ').upper()
            if len(unos) != 1 or not unos in opcije:
                print('Neispravan unos pokusajte ponovo!')
            else:
                break

        if unos == 'A': # apartmani koji su rezervisani na zadati datum
            datum = ''
            while True: # unos datuma
                datum = ''
                datum = input('\nUnesite dan realizacije u formatu \'dd/mm/yyyy\': ')
                try:
                    datum = datetime.datetime.strptime(datum, '%d/%m/%Y')
                except:
                    print('Neispravan unos, pokusajte ponovo!')
                    continue

                break

            print('\nApartmani rezervisani',datetime.datetime.strftime(datum, '%d/%m/%Y'), 'su:')

            for key in rezervacije.keys():
                pocetni_datum = datetime.datetime.strptime(rezervacije[key]['pocetni_datum'], '%d/%m/%Y')
                krajnji_datum = pocetni_datum + datetime.timedelta(int(rezervacije[key]['broj_nocenja']))

                if rezervacije[key]['status'] == 'PRIHVACENA':
                    if datum >= pocetni_datum and datum <= krajnji_datum:
                        print('Apartman sa sifrom', rezervacije[key]['apartman'], 'je rezervisan u periodu:', datetime.datetime.strftime(pocetni_datum, '%d/%m/%Y'), '-',datetime.datetime.strftime(krajnji_datum, '%d/%m/%Y'))
            print()
 
        elif unos == 'B':
            domacin  = ''
            while True: # unos domacina
                domacin = input('\nUnesite username domacina: ')
                if not domacin in korisnici.keys():
                    print('Nepostojeci korisnik!')
                elif korisnici[domacin]['uloga'] != 'DOMACIN':
                    print('Nepostojeci domacin, pokusajte ponovo!')
                else:
                    break

            print()
            print('-'*30)
            print('Sve potvrdjene rezervacije za domacina', domacin, 'su:')

            for key in rezervacije:
                if apartmani[rezervacije[key]['apartman']]['domacin'] == domacin and rezervacije[key]['status'] == 'PRIHVACENA':
                    pocetni_datum = datetime.datetime.strptime(rezervacije[key]['pocetni_datum'], '%d/%m/%Y')
                    krajnji_datum = pocetni_datum + datetime.timedelta(int(rezervacije[key]['broj_nocenja']))
                    print('Apartman sa sifrom', rezervacije[key]['apartman'], 'rezervisan u prediodu', datetime.datetime.strftime(pocetni_datum, '%d/%m/%Y'), '-', datetime.datetime.strftime(krajnji_datum, '%d/%m/%Y') )
            
            print('-'*30)
            print()

        elif unos == 'C':
            niz_za_ispis = []
            danas = datetime.datetime.today()
            for key in korisnici:
                if korisnici[key]['uloga'] == 'DOMACIN':
                    domacin = key
                    zarada = 0
                    broj_rezervacija = 0
                    for key_rezervacija in rezervacije:
                        pocetni_datum = datetime.datetime.strptime(rezervacije[key_rezervacija]['pocetni_datum'], '%d/%m/%Y')
                        delta = danas - pocetni_datum
                        if delta > datetime.timedelta(days=365) or delta < datetime.timedelta(days=0):
                            continue
                        if apartmani[rezervacije[key_rezervacija]['apartman']]['domacin'] == domacin and rezervacije[key_rezervacija]['status'] == 'ZAVRSENA':        
                            broj_rezervacija += 1
                            zarada += float(rezervacije[key_rezervacija]['ukupna_cena'])
                    
                        if rezervacije[key_rezervacija]['status'] == 'PRIHVACENA':
                            broj_potvrdjenih +=1 
                    
                    temp = []
                    temp.append(domacin)
                    temp.append(broj_rezervacija)
                    temp.append(zarada)
                    niz_za_ispis.append(temp)
            
            headers = ['Domacin', 'Broj rezervacija', 'Ukupna zarada']
            print()
            print(tabulate(niz_za_ispis, headers))
            print()
       
        elif unos == 'D':
            niz_za_ispis = []
            danas = datetime.datetime.today()

            for key in korisnici.keys():

                if korisnici[key]['uloga'] == 'DOMACIN':
                    ukupna_zarada = 0
                    broj_potvrdjenih = 0

                    for key_rezervacija in rezervacije.keys():

                        if apartmani[rezervacije[key_rezervacija]['apartman']]['domacin'] == korisnici[key]['username']:
                            pocetni_datum = datetime.datetime.strptime(rezervacije[key_rezervacija]['pocetni_datum'], '%d/%m/%Y')
                            delta = danas - pocetni_datum
                            
                            if delta > datetime.timedelta(days=30) or delta < datetime.timedelta(days=0):
                                continue 
          
                            if rezervacije[key_rezervacija]['status'] == 'ZAVRSENA':
                                ukupna_zarada += float(rezervacije[key_rezervacija]['ukupna_cena'])
           
                            if rezervacije[key_rezervacija]['status'] == 'PRIHVACENA':
                                broj_potvrdjenih +=1 
            
                    temp = []
                    temp.append(key)
                    temp.append(broj_potvrdjenih)
                    temp.append(ukupna_zarada)
                    niz_za_ispis.append(temp)
            
            headers = ['Sifra', 'Broj potvrdjenih', 'Ukupna zarada']
            print()
            print(tabulate(niz_za_ispis, headers))
            print()

        elif unos == 'E':
            dan = ''
            domacin = ''
            while True: # unos dana
                dan = ''
                dan = input('\nUnesite dan u obliku \'dd/m/yyyy\': ')
                try:
                    dan =datetime.datetime.strptime(dan, '%d/%m/%Y')
                except:
                    print('Neispravan unos, pokusajte ponovo!')
                    continue
                break
            while True: # unos domacina
                domacin = ''
                domacin = input('\nUnesite username domacina: ')
                if not domacin in korisnici.keys():
                    print('Korisnik ne postoji!')
                elif not korisnici[domacin]['uloga'] == 'DOMACIN':
                    print('Nepostojeci domacin, pokusajte ponovo!')
                else:
                    break

            broj_rezervacija = 0
            ukupna_zarada = 0

            for key_rezervacija in rezervacije.keys():
                if apartmani[rezervacije[key_rezervacija]['apartman']]['domacin'] == domacin and rezervacije[key_rezervacija]['status'] == 'PRIHVACENA':
                    pocetni_datum = datetime.datetime.strptime(rezervacije[key_rezervacija]['pocetni_datum'], '%d/%m/%Y')
                    krajni_datum = pocetni_datum + datetime.timedelta(days=int(rezervacije[key_rezervacija]['broj_nocenja']))
                    if dan >= pocetni_datum and dan <= krajni_datum:
                        broj_rezervacija +=1 
                        ukupna_zarada += float(rezervacije[key_rezervacija]['ukupna_cena']) 
            
            print()
            print('Za domacina \'' + domacin + '\' ukupan broj potvrdjenih rezervacija:', str(broj_rezervacija) + ', a ukupna zarada je:', ukupna_zarada)
            print()

        elif unos == 'F':
            ukupan_broj_rezervacija_po_gradu = {}
            ukupan_broj_rezervacija = 0
            for key in rezervacije: # broj zavrsenih rezervacija
                if rezervacije[key]['status'] == 'ZAVRSENA':
                    ukupan_broj_rezervacija += 1           
                    grad = apartmani[rezervacije[key]['apartman']]['adresa'].split(', ')[1]
                    if grad in ukupan_broj_rezervacija_po_gradu.keys():
                        ukupan_broj_rezervacija_po_gradu[grad] += 1
                    else:
                        ukupan_broj_rezervacija_po_gradu[grad] = 1
            print()
            print('Pregled zastupljenosti pojedinacnih gradova u odnosu na ukupan broj rezervacija:')            
            print('-'*30)
            for grad in ukupan_broj_rezervacija_po_gradu:
                procenat = '%.2f' % ((ukupan_broj_rezervacija_po_gradu[grad]/ukupan_broj_rezervacija)*100)
                print(grad, str(ukupan_broj_rezervacija_po_gradu[grad]) + '/' + str(ukupan_broj_rezervacija), procenat + '%')
            print('-'*30)

        nastavak = True
        while True: # nastavak
            unos = ''
            unos = input('\nUnesite \'da\' ako zelite da nastavite da birate izvestaje, u suprotnom \'ne\': ').upper()
            if unos == 'DA':
                break
            elif unos == 'NE':
                nastavak = False
                break
            else:
                print('Neispravan unos, pokusajte ponovo!')
        if not nastavak:
            break

        os.system('cls' if os.name=='nt' else 'clear')