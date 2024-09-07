# *Matrisin İki Satırını Çarpma:*
import random

boyut = int(input("Boyut giriniz: \n>>> "))


def matrisciz(matrix):
    for i in matrix:
        for x in i:
            print(x, end=" ")
        print()


matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]

print("Matrisiniz oluşturuldu.")
matrisciz(matris)

islem_satiri = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> ")) - 1

print(f"{islem_satiri + 1}. satırdaki elemanlar 2 katına alındı. \nYeni Matris")


for i in range(len(matris)):
    matris[islem_satiri][i] *= 2

matrisciz(matris)
