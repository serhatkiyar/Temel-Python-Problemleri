# 13. Bir liste içindeki çift sayıları ekrana yazdıran bir `for` döngüsü yazın.
# (Liste örneği: `[15, 24, 35, 42, 57]`)

liste = [15, 24, 35, 42, 57]

for i in liste:
    if i % 2 == 0:
        print(i, end=" ")
