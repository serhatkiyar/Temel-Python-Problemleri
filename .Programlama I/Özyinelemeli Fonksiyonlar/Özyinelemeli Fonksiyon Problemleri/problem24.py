# 24. **Dizi Elemanlarını Belirli Bir Değere Kadar Olan Çift Sayıları Toplama Fonksiyonu:**
# Belirli bir değere kadar olan çift sayıların toplamını hesaplayan özyinemeli bir fonksiyon yazın.

def alt_cfit_topla(lis, deger, n=0, toplam=0):

    if n == len(lis):
        return toplam

    if lis[n] <= deger and lis[n] % 2 == 0:
        toplam += lis[n]

    return alt_cfit_topla(lis, deger, n + 1, toplam)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(alt_cfit_topla(liste, 7))
