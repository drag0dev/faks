from math import sqrt

x1, y1 = eval(input("Uneiste x i y koordinate prve tacke: "))
x2, y2 = eval(input("Uneiste x i y koordinate druge tacke: "))

d = sqrt((x2-x1)**2 + (y2-y1)**2)
print("Rastojanje izmedju tacaka (%d, %d) i (%d, %d) je %.2f" % (x1,y1,x2,y2,d))