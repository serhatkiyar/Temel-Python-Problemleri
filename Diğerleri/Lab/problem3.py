def linear_arama(dizi, hedef, index=0):
    if hedef == dizi[index]:
        return index
    return linear_arama(dizi, hedef, index + 1)


dizi1 = [46, 23, 56, 78, 44, 12, 9, 4, 50]
print("Index:", linear_arama(dizi1, 9))
