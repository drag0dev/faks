n = eval(input("Unesite kolko brojeva zelite da uneset: "))
sum = 0
for i in range(n):
    broj = eval(input("Unesite broj: "))
    sum = sum + broj

print("Prosek je: ", sum/n)