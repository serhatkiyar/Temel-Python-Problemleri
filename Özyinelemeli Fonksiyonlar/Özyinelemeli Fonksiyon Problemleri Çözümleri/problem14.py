# 14. **Asal Sayı Kontrolü Fonksiyonu:**
# Bir sayının asal olup olmadığını kontrol eden özyinemeli bir fonksiyon yazın.

def asal_bul(sayi, n=1, bolen_sayac=0):

    if sayi % n == 0:
        bolen_sayac += 1

    if bolen_sayac > 2 or sayi == 1 or sayi == 0:
        return False

    elif sayi == n:
        return True

    return asal_bul(sayi, n + 1, bolen_sayac)


print(asal_bul(5))
