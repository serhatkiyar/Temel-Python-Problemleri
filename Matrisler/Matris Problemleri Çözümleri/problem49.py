# Matrisin Satırları Arasındaki Farkları Bulma:
# Verilen bir matrisin ardışık satırları arasındaki farkları bulan bir Python programı yazın.

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

for i1 in range(len(matris_1) - 1):
    print(f"{i1}. satır ile {i1 + 1}. satırları arasındaki fark: ")
    for j1 in range(len(matris_1[0])):
        print(f"{matris_1[i1][j1] - matris_1[i1 + 1][j1]}", end=" ")
    print()
