def sirakuza(x):
    lista = [x]
    for i in range(1, x+1):
        if lista[-1]%2==0: lista.append(lista[-1]/2)
        else: lista.append(3*lista[-1]+1)
    print(lista)

if __name__ == '__main__':
    sirakuza(5)