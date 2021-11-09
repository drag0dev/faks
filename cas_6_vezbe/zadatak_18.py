n = -1
while n <= 0:
    n = eval(input("Unesite koliko ocena zelite da unesete: "))
suma = 0
for i in range(n):
    broj = -1
    while broj < 0 or broj > 5:
        broj = eval(input("Unesite %d. ocenu: " % (i+1)))
    suma = suma + broj

prosek = suma / n

print("Prosek ocena je %.2f" % prosek)