# Matrisin Belirli Bir Satırındaki En Küçük ve En Büyük Elemanları Bulma:
# Verilen bir matrisin belirli bir satırındaki en küçük ve en büyük elemanları bulan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


def listemaxmin(liste):

    maksimum = liste[0]
    minumum = liste[0]

    for i in liste:
        if maksimum < i:
            maksimum = i
        if minumum > i:
            minumum = i
    return [minumum, maksimum]


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

print()

for i1 in range(len(matris_1)):
    print(f"{i1}. listenin maksimum değeri= {listemaxmin(matris_1[i1])[1]} / "
          f"Minumum değeri= {listemaxmin(matris_1[i1])[0]}")
