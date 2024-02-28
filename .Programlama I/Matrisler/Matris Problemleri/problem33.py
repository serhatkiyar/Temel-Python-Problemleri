# Matrisin Satırlarını Tersten Yazma:
# Verilen bir matrisin satırlarını tersten yazan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matirs_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matirs_1)

for i in matirs_1:
    for x in range(len(i)):
        for y in range(len(i) - x - 1):
            i[y], i[y + 1] = i[y + 1], i[y]

print("Tersten yazılmış matrix")
matrisciz(matirs_1)
