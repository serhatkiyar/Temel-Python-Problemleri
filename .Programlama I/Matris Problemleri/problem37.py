# Matrisin Belirli Bir Bölgesini Sıfırlama:
# Verilen bir matrisin belirli bir bölgesini sıfırlayan bir Python programı yazın.
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
for x in range(1, 3):
    satir_sec = int(input(f"{x}. Noktanın satırını giriniz: \n>>> "))
    sutun_sec = int(input(f"{x}. Noktanın sütununu giriniz: \n>>> "))
    sozluk["nokta" + str(x)] = [satir_sec, sutun_sec]

print(sozluk)

for i in range(len(matris_1)):
    for j in range(len(matris_1[0])):
        if (sozluk["nokta1"][0] <= i <= sozluk["nokta2"][0] or sozluk["nokta1"][0] >= i >= sozluk["nokta2"][0]) and \
                (sozluk["nokta1"][1] <= j <= sozluk["nokta2"][1] or sozluk["nokta1"][1] >= j >= sozluk["nokta2"][1]):
            matris_1[i][j] = 0

matrisciz(matris_1)
