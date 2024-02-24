# 13. Bir listedeki elemanları belirli bir değere göre filtreleyin.

import random

filtrelenmis_liste = []
liste = [random.randint(0, 9) for _ in range(15)]
print(liste)

filtrenilen_sayi = int(input("Hangi sayıyı filtrelemek istersiniz: \n>>> "))

for i in range(len(liste)):
    if filtrenilen_sayi != liste[i]:
        filtrelenmis_liste.append(liste[i])

print(filtrelenmis_liste)
