# 17. İki listenin ortak elemanlarını bulun.

liste_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste_2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

ortak_elemanlar = []

for i in liste_1:
    for j in liste_2:
        if i == j and i not in ortak_elemanlar:
            ortak_elemanlar.append(i)

print(f"Ortak elemanlar = {ortak_elemanlar}")
