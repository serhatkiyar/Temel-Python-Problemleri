# 10. Bir listedeki elemanları sıralayın (küçükten büyüğe veya büyükten küçüğe).

import random

liste = [random.randint(1, 100) for _ in range(30)]
print(liste)

for i in range(len(liste)):
    for j in range(len(liste) - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print(liste)