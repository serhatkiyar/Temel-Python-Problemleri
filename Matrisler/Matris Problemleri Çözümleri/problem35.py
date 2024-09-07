# Matrisin Belirli Bir Satırını Ters Çevirme:
# Verilen bir matrisin belirli bir satırını ters çeviren bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10 * random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

satir_sec = int(input("Hangi satırı ters çevirmek istersiniz: \n>>> "))
print("işlem yapılacak satır=", matris_1[satir_sec])

for i in range(len(matris_1[0])//2):
    matris_1[satir_sec][i], matris_1[satir_sec][len(matris_1) - i - 1] =\
        matris_1[satir_sec][len(matris_1) - i - 1], matris_1[satir_sec][i]

print("Ters çevirilmiş Matris")
matrisciz(matris_1)
