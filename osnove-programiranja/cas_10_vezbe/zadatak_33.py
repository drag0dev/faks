from os import error


def kalkulator(a,b,znak):
    if(znak=='+'): return a + b
    elif(znak=='-'): return a - b
    elif(znak=='*'): return a / b
    elif(znak=='/'): return a / b
    elif(znak=='//'): return a // b
    else: return 0
         
def main():
    a = ''
    b = ''
    operacija = ''
    while 1:
        a = input("Unesite prvi broja: ")
        if a.isdigit(): 
            a = int(a)
            break
        
    while 1:
        b = input("Unesite drugi broja: ")
        if b.isdigit(): 
            b = int(b)
            break
        
    while operacija != '+' and operacija != '-' and operacija != '*' and operacija != '/' and operacija != '//': 
        operacija = input("Unesite znak operacije: ")
        
    print("Rez je:", kalkulator(a,b,operacija))

if __name__ == '__main__':
    main()