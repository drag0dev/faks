dict_knjiga = []

def ucitavanje():
    fajl = open('knjige.txt', 'r', encoding='utf-8')
    for linija in fajl.readlines():
        linija = linija.replace('\n', '')
        linija = linija.split('|')
        if len(linija)!=7:continue
        dict = {"id" : linija[0], "autori" : linija[1], "naslov" : linija[2], "izdavac" : linija[3],
                "cena" : linija[4], "kolicina" : linija[5], "godina" : linija[6]}   
        dict_knjiga.append(dict)
    fajl.close()

def ispis_svih_knjiga():
    print('id \t naslov \t autori \t izdavac \t cena \t kolicina \t godina')
    print('-------------------------------------------------', end='')
    print('-------------------------------------------------')
    for knjiga in dict_knjiga:
        print(knjiga["id"] , '\t' , knjiga["naslov"] , '\t' , knjiga["autori"] , '\t' , knjiga["izdavac"]
              , '\t' , knjiga["cena"], '\t' , knjiga["kolicina"], '\t' , knjiga["godina"])
    print('-------------------------------------------------', end='')
    print('-------------------------------------------------')

def novi_id():
    max = -1
    for dict in dict_knjiga:
        if int(dict["id"]) > max: max = int(dict["id"])
    return max+1

def dodavanje_knjige():
    global dict_knjiga
    nova_knjiga = {}
    nova_knjiga["id"] = novi_id()
    naslov = input("Unesite naslov knjige:")
    autori = input("Unesite autore knjige:")
    izdavac = input("Unesite izdavac knjige:")
    cena = input("Unesite cena knjige:")
    kolicina = input("Unesite kolicina knjige:")
    godina = input("Unesite godina knjige:")
    nova_knjiga["naslov"] = naslov
    nova_knjiga["autori"] = autori
    nova_knjiga["izdavac"] = izdavac
    nova_knjiga["cena"] = cena
    nova_knjiga["kolicina"] = kolicina
    nova_knjiga["godina"] = godina
    dict_knjiga.append(nova_knjiga)
    
    str_knjiga = ''
    for el in nova_knjiga:
        str_knjiga = str_knjiga + str(nova_knjiga[el]) +'|'
    str_knjiga = str_knjiga[:-1]
    str_knjiga = str_knjiga + '\n'
    fajl = open('knjige.txt', 'a', encoding='utf-8')
    fajl.writelines(str_knjiga)
    fajl.close()
    print()

    ispis_svih_knjiga()

if __name__ == '__main__':
    ucitavanje()
    #dodavanje_knjige()
    ispis_svih_knjiga()