sum = 0
n = 0
while(1):
    broj = input("Unesite broj: ")
    if broj == "x":
        break
    broj = int(broj)
    n = n+1
    sum = sum + broj

if n>0:
    print("Prosek je: ", sum/n)