def asaluret(max1):

    if max1 == 2:
        yield max1

    for i1 in range(max1 + 1):
        if i1 != 1 and i1 != 0:

            kontrol = True
            for j in range(2, i1):
                if i1 % j == 0:
                    kontrol = False
                    break
            if kontrol:
                yield i1


for i in asaluret(19):
    print(i)

iterator = iter(asaluret(10))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
