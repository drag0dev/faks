def rad_sa_nizom(niz):
    min = niz[0]
    max = niz[0]
    suma = 0
    broj_el = 0
    for i in niz:
        if i > max: max = i
        if i < min: min = i
        suma += i
        broj_el +=1
    print("Najveci je:", max)
    print("Najmanji je:", min)
    print("Suma je:", suma)
    print("Srednja vrednost je:", suma/broj_el)

def main():
    niz = [1,2,3,4,5]
    rad_sa_nizom(niz)

if __name__ == '__main__':
    main()