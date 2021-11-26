def prestupna_godina(godina):
    if godina % 100 == 0: #poslednja godina u veku
        if godina % 400 == 0:
            print(godina,'je prestupna godina')
        else : print(godina, 'nije prestupna godina')
        return
    if godina% 4 ==0:
        print(godina, 'je prestupna')
    else :
        print(godina,'nije prestupna')
    return

if __name__ == '__main__':
    prestupna_godina(2000)