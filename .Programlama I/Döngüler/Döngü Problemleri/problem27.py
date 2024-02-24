# 27. 1 ile 100 arasındaki çift sayıları ekrana yazdıran bir `for` döngüsü yazın.

for i in range(1, 100 + 1):
    if i % 2 == 0:
        print(i, end=" ")
