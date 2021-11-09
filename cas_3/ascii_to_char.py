#text = input("Unesite poruku: ")

#text = "Hello"

#for ch in text:
#    print(ord(ch), end=' ')
#72 101 108 108 111
ascii = input("Unesite ascii vrednosti poruke: ")

slova_ascii = ascii.split(",")
for i in slova_ascii:
    print(chr(int(i)), end='')