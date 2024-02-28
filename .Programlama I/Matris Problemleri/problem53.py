# Matrisin Satırlarındaki Elemanların Toplamının Sıfır Olup Olmadığını Kontrol Etme:
# Verilen bir matrisin satırlarındaki elemanların toplamının sıfır olup olmadığını
# kontrol eden bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[int(random.randint(-9, 9)) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris)

for i1 in range(len(matris)):
    toplam = 0
    for j1 in range(len(matris[0])):
        toplam += matris[i1][j1]
    if toplam == 0:
        print(f"{i1}. satır toplamı 0' dır")
    else:
        print(f"{i1}. satır toplamı 0 değildir.")
