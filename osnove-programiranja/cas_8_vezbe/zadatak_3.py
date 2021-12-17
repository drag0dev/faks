str = input("Unesite string: ")
brojevi = ''
slova = ''
for chr in str:
    if chr.isnumeric():
        brojevi += chr
    elif chr.isalpha():
        slova += chr

print("Brojevi iz stringa: " + brojevi)
print("Slova iz stringa: " + slova)