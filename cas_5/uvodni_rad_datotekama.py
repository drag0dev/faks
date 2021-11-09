ime_fajla = "datoteka.txt"

while str.find(ime_fajla, ".txt")==-1: 
    ime_fajla = input("Unesite ime fajla: ")

fajl = open(ime_fajla, "a")
data = fajl.readlines()

data.append("Ovo je nova linija pog")

print(data)

fajl.writelines(data)


print(data)
fajl.close()