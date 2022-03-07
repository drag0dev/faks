from admin_funckije import kreiranje_dodatne_opreme
from globalne_promenljive import *
import datetime

def auto_odbijanje_rezervacija():
    today = datetime.datetime.today()
    
    # rezervacije koje su kreirane ciji je datum >= danas se automatski odbijaju
    for key in rezervacije:
        pocetni_datum = datetime.datetime.strptime(rezervacije[key]['pocetni_datum'], '%d/%m/%Y')
        if rezervacije[key]['status'] == 'KREIRANA' and pocetni_datum <= today:
            rezervacije[key]['status'] = 'ODBIJENA'
    
    # rezervacije koje su prihacene ciji je zavrsni datum >= danas se automatski zavrsavaju
    for key in rezervacije:
        pocetni_datum = datetime.datetime.strptime(rezervacije[key]['pocetni_datum'], '%d/%m/%Y')
        krajnji_datum = pocetni_datum + datetime.timedelta(days=int(rezervacije[key]['broj_nocenja']))
        if rezervacije[key]['status'] == 'PRIHVACENA' and today >= krajnji_datum:
            rezervacije[key]['status'] = 'ZAVRSENA'

def auto_update_dostupnost(): 
    # ako je dasasnji datum >= pocetni datum dostupnost odsece se datum do sutrasjneg datuma
    today = datetime.datetime.today()
    for key in apartmani:
        temp = apartmani[key]['dostupnost'].split(' ')

        for opseg in temp:
            if len(opseg)==0:
                continue
            pomocna = opseg.split('-')
            pocetni_datum = datetime.datetime.strptime(pomocna[0], '%d/%m/%Y')
            krajnji_datum = datetime.datetime.strptime(pomocna[1], '%d/%m/%Y')

            if pocetni_datum<= today and krajnji_datum > today:  # {  | }
                delta = (today - pocetni_datum).days
                pocetni_datum = pocetni_datum + datetime.timedelta(days=(1+delta))
                novi_str = datetime.datetime.strftime(pocetni_datum, '%d/%m/%Y') + '-'
                novi_str += datetime.datetime.strftime(krajnji_datum, '%d/%m/%Y')
                apartmani[key]['dostupnost'] = apartmani[key]['dostupnost'].replace(opseg, novi_str)

            elif pocetni_datum <= today and krajnji_datum <= today: # { } |
                apartmani[key]['dostupnost'] = apartmani[key]['dostupnost'].replace(opseg, '')
        apartmani[key]['dostupnost'] = ' '.join(apartmani[key]['dostupnost'].split())

def sortiranje_opsega():
    for key in apartmani.keys():
        opsezi = apartmani[key]['dostupnost'].split(' ')

        if len(opsezi)==0:
            continue

        for i in range(len(opsezi)):
            for j in range(len(opsezi)-1):
                pocetni_prvog_opsega = datetime.datetime.strptime(opsezi[j].split('-')[0], '%d/%m/%Y')
                pocetni_drugog_opsega = datetime.datetime.strptime(opsezi[j+1].split('-')[0], '%d/%m/%Y')
                if pocetni_drugog_opsega < pocetni_prvog_opsega:
                    temp = opsezi[j]
                    opsezi[j] = opsezi[j+1]
                    opsezi[j+1] = temp
        
        opsezi = ' '.join(opsezi)
        apartmani[key]['dostupnost'] = opsezi