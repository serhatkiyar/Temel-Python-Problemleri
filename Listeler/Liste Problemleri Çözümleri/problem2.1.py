# 2. İki listenin birleştirilmiş halini oluşturun.

liste_1 = [1, 3, 5, 7, 9]
liste_2 = [0, 2, 4, 6, 8]

for i in range(len(liste_2)):
    liste_1.append(liste_2[i])

print(liste_1)