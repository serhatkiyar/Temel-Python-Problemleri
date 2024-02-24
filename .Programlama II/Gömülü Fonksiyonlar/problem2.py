liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7), (1, 30, 32)]


def ucgenlik(kenarlar):
    if kenarlar[0] - kenarlar[1] < kenarlar[2] < kenarlar[0] + kenarlar[1]:
        return True
    return False


results = list(filter(ucgenlik, liste))
print(results)
