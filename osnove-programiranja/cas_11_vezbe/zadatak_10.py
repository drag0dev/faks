def datum(dat):
    dat = dat.split('/')
    dan = dat[0]
    mesec = dat[1]
    godina = dat[2]

    redni_broj = 31 * (mesec-1) + dan
    if mesec>2:
        redni_broj-= (4*mesec+23)/10
    if mesec>2 and godina%4==0:
        redni_broj += 1

if __name__ == '__main__':
    datum('30/9/2000')