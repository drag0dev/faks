#ne dobijam ista resenja kao u zadatom primeru
# '18:35','22:50' = 546din

def dadilja(pocetak, kraj):
    zarada = 0
    pocetak_list = pocetak.split(':')
    kraj_list = kraj.split(':')

    pocetak_minuti = int(pocetak_list[0])*60 + int(pocetak_list[1]) #pocetak u minutima
    kraj_minuti = int(kraj_list[0])*60 + int(kraj_list[1]) #kraj u minutima

    if pocetak_minuti<1260:

        if kraj_minuti<1260:
            zarada = (kraj_minuti-pocetak_minuti) * 150
        else: zarada = (1260-pocetak_minuti) * 150 + (kraj_minuti-1260)*100
        
        zarada = zarada / 60
        return 'Zarada dadilje je %.0f' % zarada
    else: return 'greska'
    # 21:00 u minutima 1260



    return zarada    

if __name__ == '__main__':
    print(dadilja('18:35', '22:50'))