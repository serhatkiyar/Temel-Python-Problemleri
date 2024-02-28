# Matris Elemanlarını Üs Alma:
# Verilen bir matrisin elemanlarını belirli bir üs kuvvetine yükselten bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

us = int(input("Üs değerini giriniz: \n>>> "))

for i2 in range(len(matris_1)):
    for j2 in range(len(matris_1[0])):
        matris_1[i2][j2] = matris_1[i2][j2] ** us

matrisciz(matris_1)
