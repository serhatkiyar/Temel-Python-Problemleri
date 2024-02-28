# Matrisin Satırlarını Tersine Çevirme:
# Verilen bir matrisin satırlarını tersine çeviren bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for i1 in range(len(matris_1)):
    for j1 in range(len(matris_1[0])):
        for u in range(len(matris_1[0]) - j1 - 1):
            if matris_1[i1][u] < matris_1[i1][u + 1]:
                matris_1[i1][u], matris_1[i1][u + 1] = matris_1[i1][u + 1], matris_1[i1][u]

print("Yeni Matris")
matrisciz(matris_1)
