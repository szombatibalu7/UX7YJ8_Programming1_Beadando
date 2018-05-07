#2. Feladat: Egyik számrendszerből másik számrendszerbe váltás

#Függvények
def toHex():
    if fromBase == 11 or fromBase == 12 or fromBase == 13 or fromBase == 14 or fromBase == 15 or fromBase == 16:
        nToHex = []
        for i in n:
            if i == 'A':
                nToHex.append('10')
            elif i == 'B':
                nToHex.append('11')
            elif i == 'C':
                nToHex.append('12')
            elif i == 'D':
                nToHex.append('13')
            elif i == 'E':
                nToHex.append('14')
            elif i == 'F':
                nToHex.append('15')
            else:
                nToHex.append(i)
        s = nToHex[::-1]
        m_tiz = 0
        a = 0
        for j in s:
            m_tiz += int(j)*(fromBase**a)
            a += 1
        return m_tiz
    else:
        s = n[::-1]
        m_tiz = 0
        j = 0
        for i in s:
            m_tiz += int(i)*(fromBase**j)
            j += 1
        return m_tiz

def to():
    k = toHex()
    m = ''
    while True:
        if k == 0:
            return m[::-1]
        if k%toBase==10:
            m += 'A'
        elif k%toBase==11:
            m += 'B'
        elif k%toBase==12:
            m += 'C'
        elif k%toBase==13:
            m += 'D'
        elif k%toBase==14:
            m += 'E'
        elif k%toBase==15:
            m += 'F'
        else:
            m += str(k%toBase)
        k = k//toBase
#MAIN:
n = input('Szám: ')
fromBase = int(input('Melyik számrendszerből:'))
toBase = int(input('Melyik számrendszerbe:'))
print(to())