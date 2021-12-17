fajl = open("Korisnici.txt", "r")

print()

for line in fajl.readlines():
    podeljena_linija = line.split('|')
    print("Korisnicko ime: " + podeljena_linija[0] + '\n' + "lozinka: " + podeljena_linija[1])

fajl.close()