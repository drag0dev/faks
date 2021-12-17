def broj_godina(kam_stop):
    i = 0
    x = 1
    while x < 2:
        print(x)
        x = x * (kam_stop+1)
        i = i+1

    return str(i)

if __name__ == '__main__':
    print(broj_godina(0.04))