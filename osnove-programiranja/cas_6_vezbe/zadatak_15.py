n = -1
while n <= 0:
    n = eval(input("Unesite broj prirodnih brojeva: "))

suma = 0
for i in range(1, n+1):
    suma = suma + i

print("Suma prvih %d brojeva je %d." % (n,suma))