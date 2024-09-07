# 30. **Dizi Elemanlarını Belirli Bir Değere Kadar Olan Üslerini Hesaplama Fonksiyonu:**
# Belirli bir değere kadar olan üslerini hesaplayan özyinemeli bir fonksiyon yazın.

def alt_ust_al(lis, deger, n=0, m=1, lis1=[]):

    if n == len(lis):
        return lis

    if m == deger + 1:
        lis[n] = tuple(lis1)
        return alt_ust_al(lis, deger, n + 1, 1, [])

    lis1.append(lis[n] ** m)
    return alt_ust_al(lis, deger, n, m + 1, lis1)


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(alt_ust_al(liste, 5))
