def binarydonusum(sayi, binary=""):

    if sayi == 0 or sayi == 1:
        binary += str(sayi)
        return binary[::-1]
    return binarydonusum(sayi//2, binary + str(sayi % 2))


print(binarydonusum(30))
