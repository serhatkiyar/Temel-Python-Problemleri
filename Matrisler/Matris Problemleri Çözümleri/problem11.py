# *Satır ve Sütun Toplamı:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))

matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
matrisciz(matris)

for i in range(len(matris)):
    toplam = 0
    for j in range(len(matris[0])):
        toplam += matris[i][j]
    print(f"{i + 1}. satır toplamı= {toplam}")
for x in range(len(matris[0])):
    toplam = 0
    for y in range(len(matris)):
        toplam += matris[y][x]
    print(f"{x + 1}. sütun toplamı= {toplam}")

