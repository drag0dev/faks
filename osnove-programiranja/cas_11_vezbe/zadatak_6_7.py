def uskrs(godina):
    if godina< 1900 or godina > 2099:
        print('Godina nije u opsegu 1982-2048!')
        return
    
    a = godina % 19
    b = godina % 4
    c = godina % 7
    d = (19*a+24)%30
    e = (2*b+4*c+6*d+5)%7

    datum = 22 + d + e

    if godina in [1954, 1981, 2049, 2076]:
        datum -= 7

    if(datum>31):
        print('Uskrs je', str(datum-31) + '. aprila', str(godina) + '. godine.')
    else:
        print('Uskrs je', str(datum) + '. marta', str(godina) + '. godine.')

if __name__ == '__main__':
    uskrs(2049)