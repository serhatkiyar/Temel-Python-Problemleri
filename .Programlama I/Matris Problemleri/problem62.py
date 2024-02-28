# Matrisin Sütunlarını Rasgele Yer Değiştirme:
# Verilen bir matrisin sütunlarını rasgele yer değiştiren bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for i1 in range(len(matris_1[0])):
    sutun = []
    for i2 in range(len(matris_1)):
        sutun.append(matris_1[i2][i1])
    for j1 in range(len(matris_1)):
        a = random.randint(0, len(sutun) - 1)
        matris_1[j1][i1] = sutun[a]
        sutun.pop(a)

print("Yeni Matris")
matrisciz(matris_1)
