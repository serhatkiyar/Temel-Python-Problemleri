# Matrisin Belirli Bir Satırını Belirli Bir Değerle Çarpma:
# Verilen bir matrisin belirli bir satırını belirli bir değerle çarpan bir Python programı yazın.

import random

def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

hangi_satir = int(input("Hangi satırı çarpmak istersiniz: \n>>> "))
hangi_sayi = int(input(f"{hangi_satir}. satırı hangi sayı ile çarpmak istersiniz: \n>>> "))

for j2 in range(len(matris_1[0])):
    matris_1[hangi_satir][j2] = matris_1[hangi_satir][j2] * hangi_sayi

print("İşte yeni matrixin canım: ")
matrisciz(matris_1)
