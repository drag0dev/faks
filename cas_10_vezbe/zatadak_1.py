from math import sqrt

def kvJednacina(a,b,c):
    koren = sqrt(b**2 - 4 * a * c)
    return ((-1)*b + koren)/2*a,  ((-1)*b - koren)/2*a
    
def main():
    print(kvJednacina(-1,5,5))

if __name__ == '__main__':
    main()