# Matrisin Satırlarını Rasgele Yer Değiştirme:
# Verilen bir matrisin satırlarını rasgele yer değiştiren bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0,  9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for i1 in range(len(matris_1)):
    gecici_liste = matris_1[i1].copy()

    for j1 in range(len(matris_1[i1])):
        a = random.randint(0, len(gecici_liste) - 1)
        matris_1[i1][j1] = gecici_liste[a]
        gecici_liste.pop(a)

print("Yeni Matris")
matrisciz(matris_1)
