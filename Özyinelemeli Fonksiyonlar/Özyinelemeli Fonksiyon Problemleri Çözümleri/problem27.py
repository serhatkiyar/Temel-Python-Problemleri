# 27. **Dizi İçinde Belirli Bir Değeri Arama Fonksiyonu:**
# Bir dizinin içinde belirli bir değeri arayan özyinemeli bir fonksiyon yazın.

def liste_eleman_ara(lis, deger, n=0):

    if n == len(lis):
        return False

    if lis[n] == deger:
        return True

    return liste_eleman_ara(lis, deger, n + 1)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(liste_eleman_ara(liste, 7))
