def asallarcarpanbul(sayi, n=1, sabit=1):

    if n == sayi:
        return sabit

    if sayi % n == 0:
        sabit *= n

    return asallarcarpanbul(sayi, n + 1, sabit)


print(asallarcarpanbul(16))
