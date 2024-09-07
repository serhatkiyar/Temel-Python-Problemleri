# 32. **Dizi Elemanlarını Belirli Bir Değere Kadar Olan Üslerinin Toplamını Hesaplama Fonksiyonu:**
# Belirli bir değere kadar olan üslerinin toplamını hesaplayan özyinemeli bir fonksiyon yazın.

def alt_ust_topla(lis, deger, m=0, n=0, toplam=0):

    if m == len(lis):
        return lis
    if deger >= n:
        toplam += lis[m] ** n
        return alt_ust_topla(lis, deger, m, n + 1, toplam)
    lis[m] = toplam
    return alt_ust_topla(lis, deger, m + 1, 0, 0)


liste = [1, 2, 3, 4, 5]
print(alt_ust_topla(liste, 3))
