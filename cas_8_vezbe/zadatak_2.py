str1 = input("Unesite prvi string: ")
str2 = input("Unesite drugi string: ")
rez = ""
if len(str1)%2!=0 and len(str2)%2!=0: 
    rez += str1[0] + str2[0] #prva slova
    rez += str1[len(str1)//2] +  str2[len(str2)//2] #srednja sloav
    rez += str1[len(str1)-1] + str2[len(str2)-1] #poslednja slova
    print(rez)