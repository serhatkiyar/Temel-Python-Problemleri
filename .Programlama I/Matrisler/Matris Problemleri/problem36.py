# Matrisin Belirli Bir Sütununu Ters Çevirme:
# Verilen bir matrisin belirli bir sütununu ters çeviren bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

s_s = int(input("Hangi sütunu ters çevirmek istersiniz: \n>>> "))
for y in range(len(matris_1[0])//2):
    matris_1[y][s_s], matris_1[len(matris_1[0]) - y - 1][s_s] = matris_1[len(matris_1[0]) - y - 1][s_s], matris_1[y][s_s]

print("Ters çevrilmiş Matrix")
matrisciz(matris_1)