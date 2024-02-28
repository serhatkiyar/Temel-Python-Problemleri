# Matrisin Belirli Bir Bölgesini Toplama:
# Verilen bir matrisin belirli bir bölgesinin elemanlarını toplayan bir Python programı yazın.

import random

def matrisciz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


boyut = int(input("Boyut giriniz: \n>>> "))

matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
matrisciz(matris_1)

sozluk = {}
for i in range(1, 3):
    satir_sec = int(input(f"{i}. noktanın satırını giriniz: \n>>> "))
    sutun_sec = int(input(f"{i}. noktanın sütununu giriniz: \n>>> "))
    sozluk["n" + str(i)] = [satir_sec, sutun_sec]

toplam = 0

for i in range(len(matris_1)):
    for j in range(len(matris_1[0])):
        if (sozluk["n1"][0] <= i <= sozluk["n2"][0] or sozluk["n1"][0] >= i >= sozluk["n2"][0]) and \
                (sozluk["n1"][1] <= j <= sozluk["n2"][1] or sozluk["n1"][1] >= j >= sozluk["n2"][1]):
            toplam += matris_1[i][j]

print("toplam=", toplam)

