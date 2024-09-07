# 11. **Dizi Elemanlarını Filtreleme Fonksiyonu:**
# Bir dizi içinde belirli bir kriteri sağlayan elemanları filtreleyen özyinemeli bir fonksiyon yazın.

def liste_bol_2(lis, n=0, lis2=[]):
    if len(lis) == n + 1:
        return lis2

    if lis[n] % 2 == 0:
        lis2.append(lis[n])

    return liste_bol_2(lis, n + 1, lis2)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(liste_bol_2(liste))
