# 20. 1 ile 50 arasındaki sayıların karelerini ekrana yazdıran bir `for` döngüsü yazın.

def kare_al(x):
    return x ** 2


for i in range(1, 50 + 1):
    print(kare_al(i), end=" ")
