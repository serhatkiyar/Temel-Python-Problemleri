from functools import reduce
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ciftbul(sayi):
    if sayi % 2 == 0:
        return True
    return False


results = list(filter(ciftbul, lis))
print(results)


toplam = reduce(lambda x, y: x + y, results)
print(toplam)
