proteklo_vreme = -1
while proteklo_vreme <= 0:
    proteklo_vreme = eval(input("Unesite koliko je vremena potrobeno da zvuk dodje do posmatrac: "))

print("Udaljenost posmatraca od munje je: %.2f" % (proteklo_vreme * 340))