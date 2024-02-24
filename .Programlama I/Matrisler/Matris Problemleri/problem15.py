# *Matrisin Belirli Bir Elemanını Değiştirme:*
import random


def matrixciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut gir: \n>>> "))
matris =[[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrixciz(matris)

satir = int(input("Elemanınız kaçıncı satırda: \n>>> "))
sutun = int(input("Elemanınız kaçıncı sütunda: \n>>> "))

print(f"Seçilen eleman= {matris[satir - 1][sutun - 1]}")

yeni_eleman = int(input("Yeni eleman gir: \n>>> "))

matris[satir - 1][sutun - 1] = yeni_eleman
matrixciz(matris)