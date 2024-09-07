# 9. Bir listede belirli bir elemanın indeksini bulun.

import random

liste = [random.randint(1, 100) for _ in range(30)]
print(liste)

aranan_sayi = int(input("Hangi sayıyı arıyorsunuz: \n>>> "))

for i in range(len(liste)):
    if aranan_sayi == liste[i]:
        print(f"{aranan_sayi} sayısı {i}. index' te bulunuyor.")
