statiska_fajl = open("Statistika.txt", "w")
korisnici_fajl = open("Korisnici.txt","r")
racuni_fajl = open("Racuni.txt", "r")

for korisnik_line, racun_line in zip(korisnici_fajl, racuni_fajl):
    ime = korisnik_line.split('|')
    ime = ime[0]

    racun = racun_line.split('|')

    suma = 0
    broj_proizvoda = 0
    for i in racun:
        suma += int(i)
        broj_proizvoda += 1
    statiska_fajl.write(ime + "|" + "%.2f"%suma + "|" + "%.2f"%(suma/broj_proizvoda) + "\n")

statiska_fajl.close()
korisnici_fajl.close()
racuni_fajl.close()