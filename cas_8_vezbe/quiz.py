lista_pitanja = []
broj_bodova = 0
broj_pitanja = 0 

def ucitavanje_pitanja(): # ucitava linije iz fajla
    global lista_pitanja
    global broj_pitanja
    fajl = open("quiz.txt", "r", encoding="utf-8")
    for line in fajl.readlines():
        lista_pitanja.append(line)
    broj_pitanja = len(lista_pitanja)
    fajl.close()

def zastita_unosa(broj_odg):
    unos = 0
    while True :
        unos = input('Unesite redni broj tacnog odgovora: ')
        if unos.isnumeric() and int(unos)>=1 and int(unos)<=broj_odg:
            return int(unos)

def nastavak():
    odg = input('Ako zelite da nastavite unesite da, u suprotnom bilo sta drugo: ')
    if odg.upper()=='DA': return True
    else: return False

def postavljanje_pitanja():
    global broj_bodova
    for pitanje_el in lista_pitanja:
        print('-----------------------------------')
        pitanje_el = pitanje_el.split('|')
        print(pitanje_el[0].replace('\n', ''))
        i = 1
        while i < len(pitanje_el):
            print(str(i) + '.', pitanje_el[i].replace('\n', '').replace('!', ''))
            i = i+1
        unos = zastita_unosa(len(pitanje_el)-1)
        if '!' in pitanje_el[unos]:
            print('Tacan odgovor!')
            broj_bodova = broj_bodova + 1
        else:
            print('Netacan odgovor!')
            print('Tacan odgovor je: ', end='')
            for p in pitanje_el:
                if '!' in p:
                    print(p.replace('!', ''))
                    break
        if not nastavak():
            print('-----------------------------------')
            print('Vas broj bodova je: ', broj_bodova)
            return
        print('-----------------------------------')
    

    print('-----------------------------------')
    print('Odgovorili ste na sva pitanja!')
    print('Vas broj bodova je:', broj_bodova)


if __name__ == '__main__':
    ucitavanje_pitanja()
    postavljanje_pitanja()