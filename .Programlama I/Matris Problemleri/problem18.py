# Matris Elemanlarının Mutlak Değerini Alma:
# Verilen bir matrisin elemanlarının mutlak değerini alan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[random.randint(-9, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris)

for i1 in range(len(matris)):
    for j1 in range(len(matris[0])):
        if matris[i1][j1] < 0:
            matris[i1][j1] = -1 * matris[i1][j1]

print("Yeni Matris")
matrisciz(matris)
