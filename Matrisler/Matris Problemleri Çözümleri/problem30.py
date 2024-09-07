# Matrisin Belirli Bir Sütununu Silme:
# Verilen bir matrisin belirli bir sütununu silen bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matris_2 = []
matrisciz(matris_1)

sutun_sil = int(input("Kaçıncı index' teki sütunu silmek istiyorsunuz: \n>>> "))

for i in range(len(matris_1)):
    liste_eleman_tasiyici = []
    for j in range(len(matris_1[0])):
        if j != sutun_sil:
            liste_eleman_tasiyici.append(matris_1[i][j])
    matris_2.append(liste_eleman_tasiyici)

matrisciz(matris_2)
