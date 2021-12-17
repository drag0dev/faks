n = -1
while n <= 0:
    n = eval(input("Unesite koliko brojeva zelite da unesete: "))
suma = 0
for i in range(n):
    broj = eval(input("Unesite %d. broj: " % i+1))
    suma = suma + broj

print("Suma brojeva je %d." % suma)