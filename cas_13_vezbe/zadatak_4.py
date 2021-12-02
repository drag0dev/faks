from math import sqrt
def prost_broj(broj):
    if broj >= 2 and broj <= sqrt(2):
        return True
    if broj<=0: return False

    for i in range(2, broj):
        if broj % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(prost_broj(123))