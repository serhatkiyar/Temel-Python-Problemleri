# 19. Bir listedeki elemanları belirli bir değere göre güncelleyin.

import random

liste = [random.randint(0, 100) for _ in range(20)]
print(liste)

deger = int(input("Listeyi kaç katına almak istersiniz: \n>>> "))

for i in range(len(liste)):
    liste[i] *= deger

print(f"Yeni Liste \n{liste}")
