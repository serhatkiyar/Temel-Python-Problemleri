# Matris Elemanlarını Karekök Alma:
# Verilen bir matrisin elemanlarının karekökünü alan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(f"{str(j)[:3]}", end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for i in range(len(matris_1)):
    for j in range(len(matris_1[0])):
        matris_1[i][j] = matris_1[i][j] ** (1/2)

print("Karakök alındı! Yeni Matrix: ")
matrisciz(matris_1)
