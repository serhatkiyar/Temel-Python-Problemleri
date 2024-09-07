# Matrisin Belirli Bir Satırındaki Elemanları Çarpan Bir Matris Oluşturma:
# Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla çarpan bir matris
# oluşturan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

satir_sec = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> "))
carpan_sayi = int(input(f"{satir_sec}. satırı hangi sayı ile çarpmak istersiniz: \n>>> "))

for j1 in range(len(matris_1[0])):
    matris_1[satir_sec][j1] *= carpan_sayi

matrisciz(matris_1)
