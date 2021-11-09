# futval.py
# Izracunava buduce stanje orocenog novca

print("Ovaj program izracunava stanje stednog racuna.")

godina = int(input("Unesite na kolko godina zelite da orocite novac: "))
principal = eval(input("Unesite pocetni ulog: "))
apr = eval(input("Unesite godisnju kamatu: "))

for i in range(godina):
    principal = principal * (1 + apr)

print("Stanje nakon", godina, "godina: ", principal)
