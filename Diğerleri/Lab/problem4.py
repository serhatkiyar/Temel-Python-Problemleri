def ust_al(sayi, us):
    if us == 0:
        return 1
    return sayi * ust_al(sayi, us - 1)


print(ust_al(2, 4))
