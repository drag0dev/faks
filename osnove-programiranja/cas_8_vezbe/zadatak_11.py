str1 = input("Unesite prvi string: ")
str2 = input("Unesite drugi string: ")

rez = ''
if len(str1) >=2 and len(str2)>=3:
    rez += 2*str1[0:3]
    rez += str2[len(str2)-3:len(str2)]
    print(rez)