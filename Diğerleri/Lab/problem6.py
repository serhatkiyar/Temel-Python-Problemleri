def geometrik_toplam(n):
    toplam = 1
    for i in range(2, n):
        toplam *= i
    return toplam

n = int(input("n değerini girin: "))
sonuc = geometrik_toplam(n)
print(f"1'den {n-1}'e kadar olan sayıların geometrik toplamı: {sonuc}")