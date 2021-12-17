def palindrom(s):
    return s == s[::-1]

def main():
    if palindrom("anavolimilovana"):
        print("Jeste palindrom!")
    else: print("Nije palindrom!")

if __name__ == '__main__':
    main()