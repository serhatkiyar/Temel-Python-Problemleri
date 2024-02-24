# 3. 1'den 100'e kadar olan çift sayıları ekrana yazdıran bir `for` döngüsü yazın.

for i1 in range(1, 100 + 1):
    if i1 % 2 == 0:
        print(i1, end=" ")

print()

for i2 in range(2, 100 + 1, 2):
    print(i2, end=" ")
