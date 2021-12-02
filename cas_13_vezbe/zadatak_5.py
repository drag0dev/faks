def prosti_brojevi(n):
    i=1
    j=1
    lista = []
    for i in range(1, n):
        for j in range(1, i+1):
            if i%j==0 and j!=i and j!=1: break
        if i==j: lista.append(i)
    return lista

if __name__ == '__main__':
    print(prosti_brojevi(20))