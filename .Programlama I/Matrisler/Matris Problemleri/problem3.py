# *Matrisin Belirli Bir Satırını Sıfırlama:*
import random


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()

boyut = int(input("Boyut giriniz: \n>>> "))

matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
matrisciz(matris)

islem_satiri = int(input("Hangi satırı 0' lamak istersiniz: \n>>> ")) - 1

print(f"{islem_satiri + 1}. satırdaki elemanlar 0' a eşitlendi.")

for i in range(len(matris[0])):
    matris[islem_satiri][i] *= 0

matrisciz(matris)