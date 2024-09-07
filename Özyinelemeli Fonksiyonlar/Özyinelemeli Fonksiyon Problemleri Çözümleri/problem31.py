# 31. **Dizi Elemanlarını Belirli Bir Değere Kadar Olan Çift Sayıları Bulma Fonksiyonu:**
# Belirli bir değere kadar olan çift sayıları bulan özyinemeli bir fonksiyon yazın.

def cift_bul(lis, deger, n=0, cift=[]):

    if n == len(lis):
        return cift

    if lis[n] % 2 == 0 and lis[n] <= deger:
        cift.append(lis[n])
        return cift_bul(lis, deger, n + 1, cift)
    return cift_bul(lis, deger, n + 1, cift)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cift_bul(liste, 7))
