# *Matrisin Sütun Ortalamalarını Bulma:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))
print("Matris")
matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
matrisciz(matris)
print("Sütun ortalamaları")

for i in range(len(matris[0])):
    toplam = 0
    for j in range(len(matris)):
        toplam += matris[j][i]
    print(f"{i + 1}. sütun ortalaması= {toplam/len(matris)}")
