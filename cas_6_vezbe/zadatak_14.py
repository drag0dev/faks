from math import sin

ugao = -1
while ugao <= 0:
    ugao = eval(input("Unesite ugao nagiba vremena: "))

visina = -1
while visina <= 0:
    visina = eval(input("Unesite visinu koja treba da se dostigne u m: "))

d = visina / (sin(ugao))
print("Za visinu %dm i nagib od %.2f stepeni su potrebne merdevine duzine %.2fm" % (visina, ugao, d))