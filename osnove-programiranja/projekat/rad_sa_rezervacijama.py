from pregled_ispis import pregled_rezervacija, pregled_rezervacija_korisnika
from rad_sa_sistemom_i_korisnicima import izlaz
from globalne_promenljive import *
import datetime

def ponistavanje_rezervacije():
    pregled_rezervacija_korisnika()

    sifre = []
    for key in rezervacije.keys():
        if rezervacije[key]['gost'] == ulogovanKorisnik['username'] and (rezervacije[key]['status'] == 'KREIRANA' or rezervacije[key]['status'] == 'ODOBRENA'):
            sifre.append(key)

    sifra = ''
    while True:
        sifra = input('\nUnesite sifru rezervacije koju zelite da ponisitite ili -1 za prekid: ')
        if not sifra:
            print('Neispravan unos, pokusajte ponovo!')
        elif sifra == '-1':
            return
        elif not sifra.isnumeric():
            print('Neispravan unos, pokusajte ponovo!')
        else:
            if sifra in sifre: break
            else:
                print('Neispravan unos, pokusajte ponovo!')

    
    rezervacije[sifra]['status'] = 'ODUSTANAK'
    primena_odustanka_rezervacije_na_dostupnost(rezervacije[sifra]['pocetni_datum'], rezervacije[sifra]['broj_nocenja'], rezervacije[sifra]['apartman'])

def primena_odustanka_rezervacije_na_dostupnost(pocetni_datum, broj_nocenja, sifra_apartmana):
    pocetni_datum_obj = datetime.datetime.strptime(pocetni_datum, '%d/%m/%Y')
    krajnji_datum_obj = pocetni_datum_obj + datetime.timedelta(days=int(broj_nocenja))
    
    termini = apartmani[sifra_apartmana]['dostupnost'].split(' ')

    # postfiks u smislu da dolazi posle traznog opsega
    # prefiks u smislu da dolazi pre trazenog opsega
    novi = False # da li je bio slucaj kada pokriva ceo opseg
    promena = False
    while True:
        prefiks = ''
        postfiks = ''
        for termin in termini:
            pocetni_datum_termin = datetime.datetime.strptime(termin.split('-')[0],'%d/%m/%Y')
            kranji_datum_termin = datetime.datetime.strptime(termin.split('-')[1], '%d/%m/%Y')

            if pocetni_datum_obj == pocetni_datum_termin and krajnji_datum_obj == kranji_datum_termin:
                continue

            if pocetni_datum_termin == krajnji_datum_obj:
                postfiks = termin
            elif kranji_datum_termin == pocetni_datum_obj:
                prefiks = termin
        
        if postfiks != '' and prefiks != '': # ako dodajemo sa obe strane
            novi_pocetni = prefiks.split('-')[0]
            novi_krajnji = postfiks.split('-')[1]
            novi_opseg = novi_pocetni + '-' + novi_krajnji
            pocetni_datum_obj = datetime.datetime.strptime(novi_pocetni, '%d/%m/%Y')
            krajnji_datum_obj = datetime.datetime.strptime(novi_krajnji, '%d/%m/%Y')
            apartmani[sifra_apartmana]['dostupnost'] = apartmani[sifra_apartmana]['dostupnost'].replace(prefiks, '').replace(postfiks, novi_opseg)
            promena = True
            continue

        elif prefiks != '': # ako dodajemo na zadati opseg sa leve strane
            novi_pocetni = prefiks.split('-')[0]
            novi_opseg = novi_pocetni + '-' + datetime.datetime.strftime(krajnji_datum_obj, '%d/%m/%Y')
            pocetni_datum_obj = datetime.datetime.strptime(novi_pocetni, '%d/%m/%Y')
            apartmani[sifra_apartmana]['dostupnost'] = apartmani[sifra_apartmana]['dostupnost'].replace(prefiks, novi_opseg)
            promena = True
            continue

        elif postfiks != '': # ako dodajemo na zadati opseg sa desne strane
            novi_krajnji = postfiks.split('-')[1]
            novi_opseg = datetime.datetime.strftime(pocetni_datum_obj, '%d/%m/%Y') + '-' + novi_krajnji
            krajnji_datum_obj = datetime.datetime.strptime(novi_krajnji, '%d/%m/%Y')
            apartmani[sifra_apartmana]['dostupnost'] = apartmani[sifra_apartmana]['dostupnost'].replace(postfiks, novi_opseg)
            promena = True
            continue

        elif postfiks == '' and prefiks == '' and not novi and not promena:
            novi_opseg = ' ' + datetime.datetime.strftime(pocetni_datum_obj, '%d/%m/%Y') + '-'
            novi_opseg += datetime.datetime.strftime(krajnji_datum_obj, '%d/%m/%Y')
            apartmani[sifra_apartmana]['dostupnost'] += novi_opseg
            novi = True
            continue

        break

    apartmani[sifra_apartmana]['dostupnost'] = ' '.join(apartmani[sifra_apartmana]['dostupnost'].split())

def brisanje_rezervacija(sifra_apartmana):
    niz_kljuceva = []
    for key in rezervacije.keys():
        if rezervacije[key]['apartman'] == sifra_apartmana:
            niz_kljuceva.append(key)
    for key in niz_kljuceva:
        del rezervacije[key]

def potvrda_odbijanje_rezervacija():
    unos = ''
    sifra = ''
    while True: # unos sifre rezervacije
        unos = ''
        unos = input('\nUnesite sifru rezervacije, ostavite prazno za pregled rezervacija, ili -1 da prekinete: ')
        if unos == '-1':
            return
        elif unos == '':
            print('Rezervacije za domacina:', ulogovanKorisnik['username'] + ':')
            pregled_rezervacija()
        elif unos in rezervacije.keys() and apartmani[rezervacije[unos]['apartman']]['domacin'] == ulogovanKorisnik['username'] and rezervacije[unos]['status'] == 'KREIRANA':
            sifra = unos
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')
    
    while True:
        unos = ''
        unos = input('\nUnesite \'da\' ako zelite da odbijete rezervaciju, \'ne\' ako zelite da prihvatite ili -1 ako zelite da odustanete: ').upper()
        if unos == '-1':
            return
        elif unos == 'DA':
            rezervacije[sifra]['status'] = 'ODBIJENA'
            primena_odustanka_rezervacije_na_dostupnost(
                rezervacije[sifra]['pocetni_datum'], rezervacije[sifra]['broj_nocenja'], rezervacije[sifra]['apartman'])
            break
        elif unos == 'NE':
            rezervacije[sifra]['status'] = 'PRIHVACENA'
            break
        else:
            print('Neispravan unos, pokusajte ponovo!')