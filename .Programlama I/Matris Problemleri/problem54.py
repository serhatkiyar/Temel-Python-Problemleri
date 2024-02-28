# Matrisin Sütunlarındaki Elemanların Toplamının Sıfır Olup Olmadığını Kontrol Etme:
# Verilen bir matrisin sütunlarındaki elemanların toplamının sıfır olup
# olmadığını kontrol eden bir Python programı yazına

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[random.randint(-9, 9) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

for i1 in range(len(matris_1[0])):
    toplam = 0

    for j1 in range(len(matris_1)):
        toplam += matris_1[j1][i1]

    if toplam == 0:
        print(f"{i1}. sütun toplamı 0' dır.")
    else:
        print(f"{i1}. sütun toplamı 0 değildir.")
