# 16. 1 ile 50 arasındaki sayıların çarpımını bulan bir `while` döngüsü yazın.

sayi = 1
carpim = 1

while 1 <= sayi <= 50:
    carpim *= sayi
    sayi += 1

print(carpim)
