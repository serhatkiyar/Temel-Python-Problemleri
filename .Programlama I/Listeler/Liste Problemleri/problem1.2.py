# 1. Bir listedeki elemanları tersine çevirin.

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(liste)):
    for j in range(len(liste) - i - 1):
        liste[j], liste[j + 1] = liste[j + 1], liste[j]

print(liste)
