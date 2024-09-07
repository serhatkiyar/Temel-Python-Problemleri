# 16. Listenin ortanca elemanını bulun.

def ortanca(list):

    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    if len(list) % 2 == 0:
        return (list[int(len(list) / 2)] + list[int(len(list) / 2 - 1)]) / 2
    return list[len(list)//2]


liste = [2, 3, 4, 3, 2, 1, 5]

print(f"{liste} \n{ortanca(liste)}")
