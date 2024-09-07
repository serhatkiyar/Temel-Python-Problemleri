# 1. Bir listedeki elemanları tersine çevirin.

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(liste)):
    liste.append(liste.pop(-(i + 1)))

print(liste)
