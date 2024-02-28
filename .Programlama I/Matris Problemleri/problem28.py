# Matrisin Belirli Bir Elemanını Bulma:
# Verilen bir matrisin belirli bir elemanını bulan bir Python programı yazın.

import random
boyut = int(input("Boyut giriniz: \n>>> "))


def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris)

eleman_bul = int(input("Hangi elemanı arıyorsunuz: \n>>> "))
print(f"Aranan eleman= {eleman_bul}")
for x in range(len(matris)):
    for y in range(len(matris[0])):
        if matris[x][y] == eleman_bul:
            print(f"{x}. satır {y}. sütun")
