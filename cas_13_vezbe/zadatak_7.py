def log_in():
    while True:
        username = input('Unesite vas username: ') 
        pw = input('Unesite vasu lozinku: ')

        fajl = open('prodavci.txt', 'r')
        for linija in fajl.readlines():
            kombinacija = linija.replace('\n', '').split('|')
            if username == kombinacija[0] and pw == kombinacija[1]:
                print('Uspesno ulogovani!')
                return
        fajl.close()
        print('Ne uspesno logovanje!')
        print('----------------------')

def dodavanje_proizvoda():
    print('Unesite novi proizvod:')
    naziv = ''
    cena = 0
    kol = 0
    naziv = input('Unesite ime prozivoda: ')
    cena = input('Unesite cenu proizvoda: ')
    kol = input('Unesite kolicinu proizvoda: ')

    linija = naziv + '|' + cena + '|' + kol + '\n'
    fajl = open('proizvodi.txt', 'a')
    fajl.write(linija)
    fajl.close()
    ispis_proizvoda()


def ispis_proizvoda():
    fajl = open('proizvodi.txt', encoding="utf-8")
    for line in fajl.readlines():
        line = line.replace('\n', '').split('|')
        for item in line:
            print(item, end=' ')
        print()
    fajl.close()


if __name__ == '__main__':
    log_in()
    dodavanje_proizvoda()