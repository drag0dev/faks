def ocenjivanje(broj_bodova):
    ocena = 0
    if(broj_bodova<=54):
        ocena = 5
    elif(broj_bodova>=55 and broj_bodova <= 64):
        ocena = 6
    elif(broj_bodova>= 65 and broj_bodova <= 74):
        ocena = 7
    elif(broj_bodova>= 75 and broj_bodova <= 84):
        ocena = 8
    elif(broj_bodova>=85 and broj_bodova<= 94):
        ocena = 9
    else:
        ocena = 10 
    return ocena

if __name__ == '__main__':
    broj_bodova = -1
    while broj_bodova<0 or broj_bodova>100:
        broj_bodova = input('Unesite broj bodova: ')
        if not broj_bodova.isnumeric(): broj_bodova = -1
        else: broj_bodova = int(broj_bodova)
    print(ocenjivanje(broj_bodova))