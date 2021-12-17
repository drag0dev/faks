fajl = open("Korisnici.txt", "a")
user_name = input("korisnicko ime: ")
pwd = input("lozinka: ")
fajl.write(user_name + "|" + pwd + "\n")

fajl.close()