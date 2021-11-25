def ucitaj_radne_sate():
    fajl = open('radnici.txt', 'r')
    radni_sati = {}
    for linija in fajl.readlines():
        linija = linija.split('|')
        ukupan_broj_sati = 0
        
        if '\n' in linija[len(linija)-1]:
            print('ima')
            str = linija[len(linija)-1]
            linija[len(linija)-1] = str[:-1]

        for i in range(1,len(linija)):
            ukupan_broj_sati += eval(linija[i])

        radni_sati[linija[0]] = ukupan_broj_sati
    return radni_sati

def plata(radni_sati):
    plate = {}
    for key in radni_sati.keys():
        if radni_sati[key]>40:
            plate[key] = radni_sati[key]*1000*1.5
        else: plate[key] = radni_sati[key]*1000

    return plate

if __name__ == '__main__':
    radni_sati = ucitaj_radne_sate()
    print(radni_sati)
    print()

    print(plata(radni_sati))