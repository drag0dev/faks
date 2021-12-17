# ime m ft lanac drazava
# e i f nisu uradjeni
def ucitaj_fajl():
    lista = []
    fajl = open('mountains.txt', 'r')

    for linija in fajl.readlines():
        linija_list = linija.split('|')
        lista.append(linija_list)
    fajl.close()
    return lista

def planiniski_vrhovi_drzava(lista, drzava):
    print('Planiniski vrhovi u drzavi: ', drzava, 'su:')
    for vrh in lista:
        if drzava in vrh[4]:
            print(vrh)

def dve_zemlje(lista):
    print('Planinski vrhovi na granici dve zemlje >7700m i <8100m:')
    for vrh in lista:
        if '/' in vrh[4]: #ako imamo u imenu / onda znaci da ima dve drzave
            if int(vrh[1])>7700 and vrh[1]<8100:
                print(vrh)

def planiniski_vrhovi_drzava_visina(lista, drzava):
    print('Planiniski vrhovi u drzavi preko 6000m: ', drzava, 'su:')
    for vrh in lista:
        if drzava in vrh[4]:
            if int(vrh[1]) > 6000:
                print(vrh)

def planiniski_vrhovi_drzava_tabela(lista):
    dict_drzava = {}
    for vrh in lista:
        if int(vrh[1])>6000:
            drzava = vrh[4]
            if '\n' in drzava:
                drzava = drzava[:-1]
            
            drzava = drzava.split('/')
            for drz in drzava:
                if not drz in dict_drzava.keys():
                    dict_drzava[drz] = 1
                else:
                    dict_drzava[drz] += 1
    print('Country Num')
    print('------------')
    for drzava in dict_drzava.keys():
        print(drzava, dict_drzava[drzava])
            




if __name__ == '__main__':
    lista = ucitaj_fajl()
    planiniski_vrhovi_drzava_tabela(lista)
