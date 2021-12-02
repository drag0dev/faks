def nzd(n,m):
    n_temp = n #i
    m_temp = m #i

    while m!=0:
        n = m_temp
        m = n_temp % m_temp
        
        n_temp = n
        m_temp = m

    return str(n)

if __name__ == '__main__':
    print(nzd(25,15))