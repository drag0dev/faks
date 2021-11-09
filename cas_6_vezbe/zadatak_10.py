x1, y1 = eval(input("Unesite x i y kordinate prve tacke: "))
x2, y2 = eval(input("Unesite x i y kordinata druge tacke: "))

print("Nagib prave koja prolazi kroz tacke (%d, %d) i (%d, %d) je %.3f" % (x1,y1,x2,y2,((y2-y1)/(x2-x1))))