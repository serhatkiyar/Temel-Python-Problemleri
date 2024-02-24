from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5, 6]))

z = reduce(lambda i, j: i / j, [1024, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
print(z)


def maksimum(x, y):
    if x > y:
        return x
    else:
        return y


print(reduce(maksimum, [9, 8, 7, 6, 11, 4, 3, 2, 1]))
