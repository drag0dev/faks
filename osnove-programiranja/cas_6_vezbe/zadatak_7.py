broj_atoma_H = -1
while broj_atoma_H <= 0:
    broj_atoma_H = eval(input(("Unesite broj atoma vodonika: ")))
broj_atoma_C = -1
while broj_atoma_C <= 0:
    broj_atoma_C = eval(input("Unesite broj atoma ugjlenika: "))

masa_molekula = broj_atoma_H*1.0079 + broj_atoma_C*12.011
print("Masa molekula koji ima %d atoma H i %d atoma C je: %.2f" % (broj_atoma_H, broj_atoma_C, masa_molekula))
