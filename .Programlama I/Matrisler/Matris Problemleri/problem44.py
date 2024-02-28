# Matrisin Belirli Bir Sütununu Belirli Bir Değerle Çarpma:
# Verilen bir matrisin belirli bir sütununu belirli bir değerle çarpan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

hangi_sutun = int(input("Hangi sütunu çarpmak istiyorsunuz: \n>>> "))
hangi_sayi = int(input(f"{hangi_sutun}. sütunu hangi sayı ile çarpmak istiyorsunuz: \n>>> "))

for j2 in range(len(matris_1)):
    matris_1[j2][hangi_sutun] = matris_1[j2][hangi_sutun] * hangi_sayi

matrisciz(matris_1)
