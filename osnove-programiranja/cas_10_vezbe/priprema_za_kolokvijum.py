# dictionary = { ime_korisnikka: {suma: x, broj_uplata: x},
#               ime_korisnikka: {suma: x, broj_uplata: x},
#               ime_korisnikka: {suma: x, broj_uplata: x},
#               }
#izlged dictionaryija koji se koristi

def string_is_number(str): #funkcija koja proverava da li je string broj ili
    for chr in str:
        if not(chr.isdigit() or chr=='.'): return False
    return True

def ucitaj_korisnike(ime_fajla): #funkcija koja parsuje bank_log.txt i vraca dictionary sa korsinicima
    dictionary = {}
    fajl = open(ime_fajla, "r")
    
    for linija in fajl.readlines():
        
        korisnik = linija.split(' ')
        
        if len(korisnik)<=1 : continue #ako je u linij u bank_log.txt samo ime korinsika ne radi se nista
        
        str = korisnik[1]
        if '\n' in korisnik[1]: korisnik[1] = str[:-1]
        
        if len(korisnik)==3: #ako imamo treci argument
            str = korisnik[2]
            if korisnik[2]!="\n" and '\n' in korisnik[2]: korisnik[2] = str[:-1]
        

        if korisnik[0] in dictionary.keys(): #da li postoji korisnik koji se unosi
            
            if(korisnik[1]=='income' and len(korisnik)==3): #ako je akcija income
                if korisnik[2]!='' and string_is_number(korisnik[2]): #ako je treci argument broj
                    dictionary[korisnik[0]]['suma'] += eval(korisnik[2])
                    dictionary[korisnik[0]]['broj_uplata'] += 1
                
            elif(korisnik[1]=='withdrawal' and len(korisnik)==3):
                if korisnik[2]!='' and string_is_number(korisnik[2]): #ako je treci argument broj
                    dictionary[korisnik[0]]['suma'] -= eval(korisnik[2])
                    
                
        else: #ako korisnik ne postoji
            if korisnik[1] == 'newaccount':
                dictionary[korisnik[0]] = {'suma': 0, 'broj_uplata':0}
                
    fajl.close()
    print(dictionary)
    print('\n\n\n')
    return dictionary

def izvestaj(dictionary): #ispisuje se izvestaj u report.txt
    fajl = open('report.txt', 'w')
    for korisnik in dictionary:
        fajl.writelines(korisnik + "|" + str(dictionary[korisnik]["suma"]) + "\n")
    fajl.close()
    
def korisnik_sa_zadatim_imenom(str, dictionary): #traze se korisnici koji u imenu imaju str
    pronadjen = False
    for korisnik in dictionary:
        if str in korisnik: 
            print("Korisnik ", korisnik, "ima", str)
            pronadjen = True
    
    if not pronadjen:
        print("Korisnik sa", str, "nije pronadjen")
    
def korisnici_sa_manje_na_racunu(broj,dictionary): #ispisuju se korisnici koji imaju manje na racunu od broj
    pronadjen = False
    print("Korsnici koji imaju manje od", broj, "na racunu:")
    for korisnik in dictionary:
        if  dictionary[korisnik]['suma']<broj:
            print("Korisnik", korisnik, "na racunu ima", str(dictionary[korisnik]['suma'])) 
            pronadjen = True
    if not pronadjen:
        print("Korisnik sa manje od", broj, "nije pronadjen")
    print()

def najveci_broj_uplata(dictionary): #traze se svi korisnici koji imaju max uplata
    max = 0
    korisnik_max = ''
    for korisinik in dictionary: #prvo nadjemo koji je najveci broj uplata
        if dictionary[korisinik]['broj_uplata'] > max:
            max = dictionary[korisinik]['broj_uplata']
            korisnik_max = korisinik
    
    print("Korisnik/ci sa najvecim brojem uplata: ")
    for korisinik in dictionary: #onda se ispisuju svi korisnici koji imaju jednak max broj uplata
        if dictionary[korisinik]['broj_uplata'] == max:
            print("Korisnik", korisinik, "sa:", str(dictionary[korisinik]['broj_uplata']), "brojem uplata")
    print()

def najveca_suma(dictionary): #traze se korisnici sa najvecom sumom
    max = 0
    korisnik_max = ''
    for korisinik in dictionary:
        if dictionary[korisinik]['suma'] > max:
            max = dictionary[korisinik]['suma']
            korisnik_max = korisinik
    print("Korisnik/ci sa najvecim stanjem na racunu: ")
    for korisinik in dictionary:
        if dictionary[korisinik]['suma'] == max:
            print("Korisnik", korisinik, "ima najvece stanje na racunu: ", str(dictionary[korisinik]['suma']))
    if max != 0: print('Korsinik sa najvecom sumom je', korisnik_max, ':', max)
    print()

def stanje_korisnika(kljuc, dictionary): #ispisuje se stanje na racunu za korisnika kljuc
    if kljuc in dictionary.keys():
        print("Stanje korisnika:", kljuc, "je:", str(dictionary[kljuc]['suma']))
    else: print("Korisnik", kljuc, "ne postoji")
    print()

def main():
    dict_korisnika = ucitaj_korisnike("bank_log.txt")
    stanje_korisnika('milan34', dict_korisnika)
    najveca_suma(dict_korisnika)
    najveci_broj_uplata(dict_korisnika)
    korisnici_sa_manje_na_racunu(25000, dict_korisnika)
    korisnik_sa_zadatim_imenom('mi', dict_korisnika)
    izvestaj(dict_korisnika)
    
if __name__ == '__main__':
    main()