def novi_korisnik(ime, lozinka, naziv_fajla, delimiter):
    fajl = open(naziv_fajla, "a")
    fajl.writelines(ime + delimiter + lozinka+ '\n')
    fajl.close()

def main():
    novi_korisnik('marko', 'markovic', 'korisnici.txt', '|')

if __name__ == '__main__':
    main()