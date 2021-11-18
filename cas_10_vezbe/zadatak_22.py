def niz_reci(niz):
    str = ''
    novi_niz = []
    for rec in niz:
        if not rec in novi_niz:
            print(rec)
            novi_niz.append(rec)
    for rec in novi_niz:
        str += rec + ' '
    str = str[:len(str)-1]
    return str
def main():
    print("'" + niz_reci(['hello', 'world', 'hello', 'and', 'practice', 'and', 'makes', 'perfect', 'and', 'hello', 'world', 'again']) + "'")

if __name__ == '__main__':
    main()