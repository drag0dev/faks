import re
import datetime
from xml.etree.ElementPath import ops
from globalne_promenljive import neradni_dani

def validacija_email(email):
    expression = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    return re.fullmatch(expression, email)

def validacija_slova(str):
    if not str:
        return False
    elif not str.isalpha() and not str.isnumeric():
        return True
    elif str.isalpha():
        return True
    else: return False


def validacija_adresa(adresa):
    # trazeni format je ulica broj, grad, postasnki broj
    # gde ulica moze da se sastoji od vise reci
    
    temp = adresa.split(', ')
    if len(temp) != 3:
       return False 
    
    if temp[2].isnumeric() and temp[1].replace(' ', '').isalpha(): # ako su postanski broj i grad validni 
        
        temp = temp[0].split(' ')
        
        if temp[len(temp)-1].isnumeric(): # ako je broj validan
            
            for i in range(len(temp)-1):
                if not temp[i].isalpha(): # ako ime/deo imena ulice nisu karakteri
                    return False
        
        else: return False
    else: return False
    return True

def praznicni_dan(dan): # ocekuje se datetime objekat
    for neradni_datum in neradni_dani:
        if not '-' in neradni_datum: # jedan dan
            neradni_datum = datetime.datetime.strptime(neradni_datum, '%d/%m/%Y')
            if neradni_datum == dan:
                return True
        else:
            temp = neradni_datum.split('-')
            pocectni_datum = datetime.datetime.strptime(temp[0], '%d/%m/%Y')
            krajnji_datum = datetime.datetime.strptime(temp[1], '%d/%m/%Y')
            if dan >= pocectni_datum and dan <= krajnji_datum:
                return True
    return False

def vikend(dan): # ocekuje se datetime objekat
    redni_broj_dana = dan.weekday()
    if not redni_broj_dana < 4:
        return True
    return False