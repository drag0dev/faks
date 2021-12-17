sum = 0
n = 0
unos = "Da"
while(unos=="Da"):
    broj = eval(input("Unesite broj: "))
    n = n+1
    sum = sum + broj
    unos = input("Jos?: ")

print("Prosek je: ", sum/n)