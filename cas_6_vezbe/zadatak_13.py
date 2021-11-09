from math import sqrt

a = -1
while a <= 0:
    a = eval(input("Unesite strainuc a trougla: "))

b = -1
while b <= 0:
    b = eval(input("Unesite strainuc b trougla: "))

c = -1
while c <= 0:
    c = eval(input("Unesite strainuc c trougla: "))

s = (a+b+c)/2
povrsina = sqrt(s*(s-a)*(s-b)*(s-c))
print("Povrsina trougla stranica %d, %d i %d je: %.2f" % (a,b,c,povrsina))