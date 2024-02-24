import random


def asalsayac(a, b, c):

    sayac = 0
    lis = [random.randint(a, b) for _ in range(c)]
    print(lis)

    for i in lis:

        carpansayi = 0
        if i == 1:
            sayac -= 1
        for j in range(2, i):
            if i % j == 0:
                carpansayi += 1

        if carpansayi == 0:

            sayac += 1

    return sayac


print(asalsayac(1, 10, 10))
