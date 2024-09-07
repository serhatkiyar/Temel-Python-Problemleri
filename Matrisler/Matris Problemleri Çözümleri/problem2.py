# *Matrisin İki Sütununu Çarpma:*
import random

boyut = int(input("Boyut Giriniz: \n>>> "))


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
matrisciz(matris)
islem_sutunu = int(input("işlem yapmak istediğini sütunu giriniz: \n>>> ")) - 1
print(f"{islem_sutunu + 1}. sütundaki elemanlar 2 katına alındı. \nYeni Matris")

for x in range(len(matris)):
    matris[x][islem_sutunu] *= 2

matrisciz(matris)
