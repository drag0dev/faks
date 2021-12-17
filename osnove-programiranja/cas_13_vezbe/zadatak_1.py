def napravi_tabelu(pocetak_brzina, kraj_brzina, pocetak_temp, kraj_temp):
    #ispis prvog reda
    t = pocetak_temp
    v = pocetak_brzina
    print('\t', end='')

    while t<=kraj_temp:
        print('t=',t,'\t',end='')
        t = t+1
    print()
    while v <= kraj_brzina:
        t = pocetak_temp
        print('v=',v,end='\t')
        while t <= kraj_temp:
            so = 3.74 + 0.6215*t-35.75 * (v ** 0.16) + 0.4275*t * (v**0.16)
            print('%.3f' % so, end='\t')
            t = t+1   
        print()
        v = v+1
    

if __name__ == '__main__':
    napravi_tabelu(0, 10, 5, 10)