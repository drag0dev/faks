def kazna(brzina, ogranicenje):
    kazna = 0

    if brzina<ogranicenje:
        return kazna
    
    if brzina>ogranicenje:
        kazna = 5000 + (brzina-ogranicenje)*500
    
    if brzina>120:
        kazna += 10000
    
    return kazna


if __name__ == '__main__':
    k = kazna(130,60)
    if k > 0:
        print('Vasa kazna je', k)
    else:
        print('Niste prekoracili brzinu')