def geometrik_seri(sayi, n):
    if n == 0:
        return 1
    return (sayi ** n) + geometrik_seri(sayi, n - 1)

sayi = float(input("Sayı giriniz: \n>>> "))
N = int(input("N: \n>>> "))
print(geometrik_seri(sayi, N))
