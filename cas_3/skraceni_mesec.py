meseci_tri_slova = "JanFebMarAprMajJunJulAvgSepOktNovDec"
n= -1
while(n<0 or n>12):
    n = eval(input("Unesite mesec (1-12): "))

pos = (n-1) * 3

mesecSkr = meseci_tri_slova[pos:pos+3]

print("Skracenica je " + mesecSkr + ".")