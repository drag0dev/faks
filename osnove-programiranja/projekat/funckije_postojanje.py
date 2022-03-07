from globalne_promenljive import *

def domacin_postoji(username): # funkcija koja trazi da li postoji odredjeni domacin prema username-u
    if username in korisnici.keys():
            if korisnici[username]['uloga']=='DOMACIN':
                return True
            else: return False
    return False

def gost_postoji(username): # funkcija koja trazi da li postoji odredjeni gost prema username-u
    if username in korisnici.keys():
            if korisnici[username]['uloga']=='GOST':
                return True
            else: return False
    return False

def email_postoji(email): # funkcija koja trazi da li postoji odredjeni korisnik sa zadatim emailom
    for korisnik in korisnici:
        if korisnici[korisnik]['email'] == email:
            return True
    return False

def username_postoji(username):
    for korisnik in korisnici:
        if korisnici[korisnik]['username']==username:
            return True
    return False

def sifra_apartmana_postoji(sifra):
    if sifra in apartmani.keys():
        return True
    else: return False

def sifra_rezervacije_postoji(sifra):
    if sifra in rezervacije.keys():
        return True
    return False

def nova_sifra(dict):
    sifra = 0

    if len(dict)==0:
        return '0'

    for key in dict:
        if int(key)>sifra:
            sifra = int(key)

    sifra +=1
    return str(sifra)

def dodatna_oprema_postoji(opis):
    opis = opis.upper()
    for key in dodatna_oprema:
        if dodatna_oprema[key].upper() == opis.upper():
            return True
    return False