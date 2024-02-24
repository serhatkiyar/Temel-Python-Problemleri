# 23. Bir listedeki elemanların toplamını ve ortalamasını bulun.

def top_ort(lis):
    top = 0
    for i in lis:
        top += i

    return top, top/len(lis)


liste = [1, 2, 3, 4]
print(liste)

print(top_ort(liste))
