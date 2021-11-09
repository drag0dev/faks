n = -1
while n <= 0:
    n = eval(input("Unesite broj clanova: "))

suma = 0
delilac = 1
for i in range(n):
    if i % 2 == 0:
        suma = suma + (4/delilac)
    else:
        suma = suma - (4/delilac)
    delilac = delilac + 2

print("Dobijeni prozivod je %.2f" % suma)