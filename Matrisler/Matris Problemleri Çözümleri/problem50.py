# Matrisin Sütunları Arasındaki Farkları Bulma:
# Verilen bir matrisin ardışık sütunları arasındaki farkları bulan bir Python programı yazın.

import random


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

print()

for i1 in range(len(matris_1[0]) - 1):
    print(f"{i1}. sütun ile {i1 + 1}. sütun farkı: ")
    for j1 in range(len(matris_1)):
        print(f"{matris_1[j1][i1] - matris_1[j1][i1 + 1]:2}")
    print()
