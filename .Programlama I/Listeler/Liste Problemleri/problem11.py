# 11. Bir listedeki her elemanı bir sayıyla çarpın.

import random

liste = [random.randint(0, 10) for _ in range(10)]
print(liste)

carpan_sayi = int(input("liste elemanlarını hangi sayi ile çarpmak istersiniz: \n>>> "))

for i in range(len(liste)):
    liste[i] *= carpan_sayi

print(liste)