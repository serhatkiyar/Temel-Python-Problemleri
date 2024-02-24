# 17. 1 ile 100 arasındaki tek sayıları ekrana yazdıran bir `for` döngüsü yazın.

for i in range(1, 100 + 1):
    if i % 2 == 1:
        print(i, end=" ")
        