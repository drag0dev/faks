datum_brojevi = input("Unesite datum u formatu dd.mm.gggg. : ")

mesec = datum_brojevi.split(".")
meseci = ["Januar", "Feberuar", "Mart", "April", "Maj", "Jun", "Jul", "Avgust", "Septembar", "Okotbar", "Novermbar", "Decembar"]

print(mesec[0] + ". " + meseci[int(mesec[1])-1] + " " + mesec[2] + ".")
