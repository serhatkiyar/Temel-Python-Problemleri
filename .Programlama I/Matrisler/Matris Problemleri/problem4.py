# *Matrisin Belirli Bir Sütununu Sıfırlama:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut giriniz: "))

matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]

matrisciz(matris)

islem_sutunu = int(input("İşlem yapmak istediğiniz sütunu giriniz: \n>>> ")) - 1

print(f"{islem_sutunu + 1}. sütunundaki elemanlar 0' a eşitlendi.")
for i in range(len(matris)):
    matris[i][islem_sutunu] *= 0

matrisciz(matris)
