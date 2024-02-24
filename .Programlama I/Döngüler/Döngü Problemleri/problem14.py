# 14. 1 ile 10 arasındaki sayıların faktöriyellerini ekrana yazdıran bir `for` döngüsü yazın.

def faktoriyel(x):
    if x == 0:
        return 1
    return x * faktoriyel(x - 1)


for i in range(1, 10 + 1):
    print(faktoriyel(i), end=" ")
