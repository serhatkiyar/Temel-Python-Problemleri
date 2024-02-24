# 10. **Dizi Elemanlarını Birleştirme Fonksiyonu:**
# İki diziyi birleştiren özyinemeli bir fonksiyon yazın.

def lis_birlestir(lis_1, lis_2, n=0):
    if n == len(lis_2):
        return lis_1
    lis_1.append(lis_2[n])
    return lis_birlestir(lis_1, lis_2, n + 1)


liste_1 = [1, 2, 3, 4, 5]
liste_2 = [6, 7, 8, 9, 10]

print(lis_birlestir(liste_1, liste_2))
