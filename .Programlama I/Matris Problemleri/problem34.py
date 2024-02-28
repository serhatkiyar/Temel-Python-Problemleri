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

sutunlar = []

for x in range(len(matris_1)):
    listeleyici = []
    for y in range(len(matris_1[0])):
        listeleyici.append(matris_1[y][x])
    sutunlar.append(listeleyici)

for m in range(len(sutunlar)):

    for o in range(len(sutunlar)):
        for t in range(len(sutunlar) - o - 1):
            sutunlar[m][t], sutunlar[m][t + 1] = sutunlar[m][t + 1], sutunlar[m][t]

    for x2 in range(len(matris_1)):
        matris_1[x2][m] = sutunlar[m][x2]

print("Tersten yazılmış matrix")
matrisciz(matris_1)
