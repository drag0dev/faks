r = -1
while r<=0:
    r = eval(input("Unesite poluprecnik sfere: "))

zapremina = 4.0/3 * (r**3)
povrsina = 4 * (r**2)

print("Sfera poluprecnika %d ima zapreminu %.3f Pi i povrsinu %d Pi" % (r, zapremina, povrsina))