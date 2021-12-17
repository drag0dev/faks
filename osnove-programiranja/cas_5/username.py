ulazni_fajl = open("imena_prezimena.txt","r+")
izlazni_fajl = open("izlazni_fajl.txt", "w")

izlazni_podaci = []

for line in ulazni_fajl:
    ime, prezime = line.split(" ")
    username = ""
    ime = ime.lower()
    username = username + ime[:7]
    username = username + prezime[:7]
    izlazni_podaci.append(username)

izlazni_fajl.writelines(izlazni_podaci)

ulazni_fajl.close()
izlazni_fajl.close()