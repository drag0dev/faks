def citanjeFajla(ime_fajla, delimiter):
    fajl = open(ime_fajla, 'r')
    list = []
    for line in fajl.readlines():
        ime,lozinka = line.split(delimiter)
        if lozinka[len(lozinka)-1]=='\n':
            lozinka = lozinka[:-1]
        list.append([ime, lozinka])
    fajl.close()
    return list

def main():
    lista = citanjeFajla('korisnici.txt', '|')
    print(lista)

if __name__ == '__main__':
    main()