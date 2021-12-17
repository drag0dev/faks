# {"broj_posiljke" : int, "adresa" : string, "vrednost" : float}
dict_posiljki = []

def ucitaj_posiljke():
    global dict_posiljki
    posiljka = {}

    broj_posiljke = input("Unesite broj posiljke: ")
    posiljka["broj_posiljke"] = broj_posiljke

    adresa = input("Unesite adresu posiljke: ")
    posiljka["adresa"] = adresa.replace('\n', '')

    vrednost = int(input("Unesite vrednost paketa: "))
    posiljka["vrednost"] = vrednost
    dict_posiljki.append(posiljka)

def najmanja_vrednost():
    min_vrednost = dict_posiljki[0]["vrednost"]
    for posiljka in dict_posiljki:
        if posiljka["vrednost"] < min_vrednost : min_vrednost = posiljka["vrednost"]
    for posiljka in dict_posiljki:
        if posiljka["vrednost"] == min_vrednost : 
            print("-----------------------------------")
            print("Paket sa najmanjom vrednost:")
            print("Broj posiljke: ", posiljka["broj_posiljke"])
            print("Adresa: ", posiljka["adresa"])
            print("Vrednost: ", posiljka["vrednost"])
            print("-----------------------------------")
    print()

def ukupno_poslato(adresa):
    ukupno = 0
    for posiljka in dict_posiljki:
        if adresa == posiljka["adresa"]: ukupno = ukupno + posiljka["vrednost"]
    print("-----------------------------------")
    print("Za adresu \"", adresa, "\" ukupno je poslato: ", ukupno)
    print("-----------------------------------")
    print()

def ukupno_poslato_svuda():
    dict_poslato = {}
    for posiljka in dict_posiljki:
            if posiljka["adresa"] in dict_poslato.keys():
                dict_poslato[posiljka["adresa"]] += posiljka["vrednost"]
            else:
               dict_poslato[posiljka["adresa"]] = posiljka["vrednost"]
    print("-----------------------------------")
    print("Ukupno poslato na svaku adresu: ", end='\n')
    for posiljka in dict_poslato:
        print("Na adresi ", posiljka, " ukupna poslata vrednost: ", dict_poslato[posiljka])
    print("-----------------------------------")
    print()

def najpopularnija_adresa():
    dict_adresa = {}
    for posiljka in dict_posiljki:
        if posiljka["adresa"] in dict_adresa.keys():
            dict_adresa[posiljka["adresa"]] += posiljka["vrednost"]
        else:
            dict_adresa[posiljka["adresa"]] = 1
    print(dict_adresa)
    max = {"adresa" : "","vrednost" : -1}
    for posiljka in dict_adresa:
        if dict_adresa[posiljka] > max["vrednost"]:
            max["adresa"] = posiljka
            max["vrednost"] = dict_adresa[posiljka]
    print("-----------------------------------")
    print("Najpopularnija adresa je:", max["adresa"], "sa vrednosti:", max["vrednost"])
    print("-----------------------------------")
    print()

if __name__ == '__main__':
    for i in range(2): ucitaj_posiljke()
    najmanja_vrednost()
    ukupno_poslato("asd")
    ukupno_poslato_svuda()
    najpopularnija_adresa()