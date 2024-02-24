# 20. Liste elemanlarını belirli bir kurala göre filtreleyin.

import random
liste = [random.randint(0, 100) for _ in range(20)]
print(liste)
guncel_liste = []

for i in range(len(liste)):
    if liste[i] % 2 == 0:
        guncel_liste.append(liste[i])

print(f"Güncel Liste = {guncel_liste}")
