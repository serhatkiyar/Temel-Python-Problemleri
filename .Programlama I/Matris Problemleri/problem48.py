# Matrisin Belirli Bir Sütunundaki En Küçük ve En Büyük Elemanları Bulma:
# Verilen bir matrisin belirli bir sütunundaki en küçük ve en büyük elemanları bulan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i1 in matrix:
        for j1 in i1:
            print(j1, end=" ")
        print()


def listemakmin(liste):
    maksimum = liste[0]
    minumum = liste[0]

    for sayi in liste:
        if maksimum < sayi:
            maksimum = sayi
        if minumum > sayi:
            minumum = sayi
    return [minumum, maksimum]


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sutunlar = []

for i in range(len(matris_1[0])):
    gecici_liste = []
    for j in range(len(matris_1)):
        gecici_liste.append(matris_1[j][i])
    sutunlar.append(gecici_liste)

print()

for i2 in range(len(sutunlar)):
    print(f"{i2}. sütunun maksimum değeri= {listemakmin(sutunlar[i2])[1]} / "
          f"minumum değeri= {listemakmin(sutunlar[i2])[0]}")
