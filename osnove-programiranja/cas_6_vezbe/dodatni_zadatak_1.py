a = -1
while a <= 0:
    a = eval(input("Unesite broj: "))
i = 1
print("Delioci broja %d su: ", a)
while a+1!=i:
    if a%i==0: 
        print(i, end=' ')
    i = i+1