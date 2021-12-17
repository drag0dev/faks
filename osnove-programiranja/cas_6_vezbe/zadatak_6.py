poluprecnik = -1
while poluprecnik<=0:
        poluprecnik = eval(input("Unesite poluprecnik pice u cm: "))
cena = -1
while cena <= 0:
    cena = eval(input("Unesite cenu cele pice: "))

print("Cena pice po cm kvadratnom je: %.2f dinara" % (cena/((poluprecnik**2)*3.14)))