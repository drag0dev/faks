def indeks_telesne_mase(masa, visina):
    bmi = masa / (visina**2)
    if bmi<18.5:
        return 'Pothranjenost'
    elif bmi>=18.5 and bmi <= 25:
        return 'Idealna telesna masa'
    elif bmi>=25 and bmi<=30:
        return 'Preterana telesna masa'
    elif bmi>=30:
        return 'Gojaznost'

    return 'greska'

if __name__ == '__main__':
    print(indeks_telesne_mase(193, 69))