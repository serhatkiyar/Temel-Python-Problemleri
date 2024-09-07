# 7. 1 ile 20 arasındaki tek sayıları ekrana yazdıran bir `for` döngüsü yazın.

for i1 in range(1, 20 + 1):
    if i1 % 2 == 1:
        print(i1, end=" ")

print()

for i2 in range(1, 20, 2):
    print(i2, end=" ")
