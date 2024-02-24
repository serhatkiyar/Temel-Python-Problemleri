# 6. **En Büyük Ortak Bölen (GCD) Hesaplama Fonksiyonu:
# ** İki sayının en büyük ortak bölenini hesaplayan özyinemeli bir fonksiyon yazın.

def ebob(sayi_1, sayi_2, n=2):

    if sayi_1 == 1 or sayi_2 == 1:
        return 1

    elif sayi_1 % n == 0 and sayi_2 % n == 0:
        return n * ebob(sayi_1/n, sayi_2/n, n)

    elif sayi_1 % n == 0:
        return ebob(sayi_1/n, sayi_2, n)

    elif sayi_2 % n == 0:
        return ebob(sayi_1, sayi_2/n, n)

    else:
        return ebob(sayi_1, sayi_2, n + 1)


print(ebob(60, 60))
