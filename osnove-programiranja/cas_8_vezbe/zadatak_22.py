str = input("Unesite string: ")
akronim = ''
prethodni_space = 1

if str!='':
    for chr in str:
        if chr.isalpha() and prethodni_space==1:
            akronim += chr.upper()
            prethodni_space = 0
        if chr == ' ':
            prethodni_space = 1
    print(akronim)