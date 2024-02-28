# *Matrisin İki Satırını Değiştirme:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))
matrix = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matrix)

x = int(input("Değiştirmek istediğiniz 1. satırı giriniz: \n>>> "))
y = int(input("Değiştirmek istediğiniz 2. satırı giriniz: \n>>> "))

matrix[x - 1], matrix[y - 1] = matrix[y - 1], matrix[x - 1]

matrisciz(matrix)

