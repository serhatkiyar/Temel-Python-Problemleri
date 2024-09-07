# *Matrisin Satırlarını Sıralama:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]

matrisciz(matris)

islem_satiri = int(input("İşlem yapmak istediğiniz satiri giriniz: \n>>> ")) - 1
print(f"{islem_satiri + 1}. satırdaki sayılar sıralandı.")

for i in range(len(matris[islem_satiri])):
    for j in range(len(matris[islem_satiri]) - i - 1):
        if matris[islem_satiri][j] > matris[islem_satiri][j + 1]:
            matris[islem_satiri][j], matris[islem_satiri][j + 1] = matris[islem_satiri][j + 1], matris[islem_satiri][j]

matrisciz(matris)
