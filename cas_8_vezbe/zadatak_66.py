neformiraniTeks = open("neformiraniTeks.txt", "r")
formiraniTekst = open("formiraniTeks.txt", "w")

def brisanje_visak_space(str):
    novi_str = str.split(" ")
    temp = ''
    for i in novi_str:
        i.strip()
        if i!='': temp = temp + i + ' '
    return temp


#obrada naslova
naslov = neformiraniTeks.readline()
naslov = naslov.lower()
naslov = brisanje_visak_space(naslov)

prethodni_space = 1
novi_naslov = ''
for chr in naslov:
    if chr.isalpha() and prethodni_space==1:
        chr = chr.upper()
        prethodni_space=0
    if chr==' ':
        prethodni_space=1
    novi_naslov += chr
formiraniTekst.write(novi_naslov + "\n")

#obrada pasusa
for pasus in neformiraniTeks.readlines():
    pasus = brisanje_visak_space(pasus)
    formiraniTekst.write("    ")

    tacka = 1
    novi_pasus = ""

    for chr in pasus:
        if chr.isalpha() and tacka==1:
            chr = chr.upper()
            tacka=0
        if chr=='.':
            tacka=1
        novi_pasus += chr
    formiraniTekst.write(novi_pasus)


neformiraniTeks.close()
formiraniTekst.close()