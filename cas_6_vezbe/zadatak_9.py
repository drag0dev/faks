kg = -1
while kg <= 0:
    kg = eval(input("Unesite koliko koligrama kafe porucujete: "))
print("Ukupno cena kucne porudzbine: %ddin" % (kg*(105+18)+15))