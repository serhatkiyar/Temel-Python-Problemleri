# 24. Bir listedeki elemanları ters sıralayın.

def ters_sirala(lis):
    for i in range(len(lis)):
        for j in range(len(lis) - i - 1):
            lis[j + 1], lis[j] = lis[j], lis[j + 1]

    return lis


liste = [0, 1, 2, 3, 4, 5]
print(liste)

print(ters_sirala(liste))
