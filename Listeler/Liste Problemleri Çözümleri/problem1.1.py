# 1. Bir listedeki elemanları tersine çevirin.

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(liste)//2):
    liste[i], liste[-(i + 1)] = liste[-(i + 1)], liste[i]

print(liste)
