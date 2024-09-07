# Matrisin Belirli Bir Satırını Silme:
# Verilen bir matrisin belirli bir satırını silen bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

satir_sil = int(input("Kaçıncı index' teki satırı sileceksiniz: \n>>> "))

matris_2 = []

for i in range(len(matris_1)):
    if i != satir_sil:
        matris_2.append(matris_1[i])

matrisciz(matris_2)
