# 16. **Dizi Elemanlarını Belirli Bir Değere Kadar Olan Tek Sayıları Toplama Fonksiyonu:**
# Belirli bir değere kadar olan tek sayıların toplamını hesaplayan özyinemeli bir fonksiyon yazın.

def alt_topla_tek(lis, deger, n=0, toplam=0):

    if n == len(lis):
        return toplam

    if lis[n] % 2 == 1 and lis[n] <= deger:
        toplam += lis[n]

    return alt_topla_tek(lis, deger, n + 1, toplam)


liste = [1, 2, 3, 4, 3, 5, 6, 7]
print(alt_topla_tek(liste, 5))
