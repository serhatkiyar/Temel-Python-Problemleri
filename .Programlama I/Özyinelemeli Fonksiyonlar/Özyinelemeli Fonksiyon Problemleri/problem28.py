# 28. **Dizi İçindeki Belirli Bir Değeri Bulan Fonksiyon:**
# Bir dizinin içinde belirli bir değeri bulan ve yerini döndüren özyinemeli bir fonksiyon yazın.iyon yazın.

def liste_eleman_bul(lis, deger, n=0):

    if n == len(lis):
        return ""

    if lis[n] == deger:
        return str(n) + "* " + liste_eleman_bul(lis, deger, n + 1)
    else:
        return "" + liste_eleman_bul(lis, deger, n + 1)


liste = [0, 1, 5, 3, 4, 5, 6, 7, 8, 5]
print(liste_eleman_bul(liste, 5))
