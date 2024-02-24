# *Matrisin İki Sütununu Değiştirme:*
import random


def matrixciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))

matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrixciz(matris)

x = int(input("Değiştirmek istediğiniz 1. sütunu giriniz: \n>>> "))
y = int(input("Değiştirmek istediğiniz 2. sütunu giriniz: \n>>> "))

for m in range(len(matris)):
    matris[m][x - 1], matris[m][y - 1] = matris[m][y - 1], matris[m][x - 1]

matrixciz(matris)
