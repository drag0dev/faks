from math import sqrt

x = -1
while x <= 0:
    x = eval(input("Unesite broj koji je >=0:"))

n= -1
while n <= 0:
    n = eval(input("Unesite broj pokusaja: "))

guess = x/2

for i in range(n):
    print("%d. pokusaj: %.2f" % (i+1,guess))
    if(guess==sqrt(x)):
        print("Koren %.2f je pogodjen iz %d. pokusaja." % (sqrt(x), i+1))
        break
    else:
        guess = ((guess + x)/guess)/2
