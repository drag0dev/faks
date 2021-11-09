a = 0
b = 1
n = -1
while n<=0:
    n = eval(input("Unesite koji element fibonacijevog niza zelite: "))
if (n==1):
    print("%d. element je 0", n)
elif (n==2):
    print("%d. element je 1", n)
else:
    for i in range(n-2):
        temp = b
        b = b + a
        a = temp

print("%d. element je: %d", n, b)