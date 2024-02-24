def asal_mi(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


print(list(filter(asal_mi, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])))
