def asallistele(x):
    asallar = []
    sayac = 0
    for i in range(1, int(x) ** 3):

        for j in range(1, i + 1):
            if i % j == 0:
                sayac += 1
        if sayac == 2:
            sayac += 1
            asallar.append(i)
        if sayac == x:
            break
    return asallar

print(asallistele(5))