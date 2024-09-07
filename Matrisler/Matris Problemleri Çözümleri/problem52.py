# Matrisin Belirli Bir Sütunundaki Elemanları Çarpan Bir Matris Oluşturma:
# Verilen bir matrisin belirli bir sütunundaki elemanları
# belirli bir sayıyla çarpan bir matris oluşturan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> "))
carpan_sayi = int(input(f"{sec_sutun}. sütunu hangi sayı ile çarpmak istersiniz: \n>>> "))

for i in range(len(matris_1)):
    matris_1[i][sec_sutun] *= carpan_sayi

matrisciz(matris_1)
