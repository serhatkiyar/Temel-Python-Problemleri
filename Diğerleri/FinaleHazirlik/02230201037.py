import random


def ListeOlustur(m, a, b):
    liste = []
    while True:
        if len(liste) == m:
            break
        sayi = int(random.random()*30)
        if a <= sayi <= b:
            liste.append(sayi)
    return liste


def Topla(Liste):
    liste2 = []

    for i in range(len(Liste)//2 + 1):
        liste2.append(Liste[i] + Liste[len(Liste) - 1 - i])

    return liste2


def BuyukHarf(cumle, n=0, sayi=0):
    if n == len(cumle):
        return sayi

    if ord("A") <= ord(cumle[n]) <= ord("Z"):
        return BuyukHarf(cumle, n + 1, sayi + 1)
    return BuyukHarf(cumle, n + 1, sayi)


def Tr2Eng(cumle):
    Tr = ["ç", "ğ", "ı", "ö", "ş", "ü"]
    Eng = ["c", "g", "i", "o", "s", "u"]
    liste = []

    for i in cumle:
        liste.append(i)

    for i in range(len(liste)):
        if liste[i] in Tr:
            for j in range(len(Tr)):
                if liste[i] == Tr[j]:
                    liste[i] = Eng[j]
    ncumle = ""

    for i in liste:
        ncumle += i

    return ncumle


def MatrisiKucult(M):

    nM = [[0 for _ in range(int(len(M[0])/2))] for _ in range(int(len(M)/2))]

    toplamlar = []
    toplam = 0
    for i in range(int(len(M)/2)):
        for j in range(int(len(M[0])/2)):
            toplam += M[i][j]
    toplamlar.append(toplam)
    toplam = 0
    for i in range(int(len(M)/2)):
        for j in range(int(len(M[0])/2), len(M[0])):
            toplam += M[i][j]
    toplamlar.append(toplam)
    sayac, toplam = 0, 0
    for i in range(int(len(M)/2), len(M)):
        for j in range(int(len(M[0])/2)):
            toplam += M[i][j]
    toplamlar.append(toplam)
    toplam = 0
    for i in range(int(len(M)/2), len(M)):
        for j in range(int(len(M[0])/2), len(M[0])):
            toplam += M[i][j]
    toplamlar.append(toplam)
    for i in range(len(nM)):
        for j in range(len(nM[0])):
            nM[i][j] = toplamlar[sayac]/4
            sayac += 1

    return nM


def BasamakDegeri(Liste):
    toplam = 0

    for i in Liste:
        toplam += len(str(i))

    return toplam

