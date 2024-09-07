# Matrisin Sütunlarını Tersten Yazma:
# Verilen bir matrisin sütunlarını tersten yazan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for x in range(len(matris_1)):
    for y in range(len(matris_1[0])//2):
        matris_1[y][x], matris_1[len(matris_1) - y - 1][x] = matris_1[len(matris_1) - y - 1][x], matris_1[y][x]

print("Tersten yazılmış matrix")
matrisciz(matris_1)
