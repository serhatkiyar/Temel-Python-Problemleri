# Matrisin Satırlarını Ortalama ile Değiştirme:
# Verilen bir matrisin satırlarını ortalamayla değiştiren bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for i1 in range(len(matris_1)):
    toplam = 0

    for j1 in range(len(matris_1[0])):
        toplam += matris_1[i1][j1]

    for j2 in range(len(matris_1[0])):
        (matris_1[i1][j2]) = float(str(toplam / 3)[:3])

print("Yeni Matris")
matrisciz(matris_1)
