def datum(datum):
    datum = datum.split('/')
    dan = int(datum[0])
    mesec = int(datum[1])
    godina = int(datum[2])

    if mesec > 12:
        return 'datum nije validan'

    if mesec in [1, 3, 5, 7, 8, 10, 12]:
        if dan > 31:
            return 'datum nije validan'
    elif mesec in [4, 6, 9, 11]:
        if dan > 30:
            return 'datum nije validan'
    elif mesec == 2:
        if godina %4 == 0:
            if dan>29: return 'datum nije validan'
        else:
            if dan>28: return 'datum nije validan'


if __name__ == '__main__':
    datum('29/02/1998')