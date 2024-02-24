def tarih(gun, ay, yil, sayac=7, liste=[]):

    if sayac == 0:
        return liste

    if gun < 30:
        gun += 1
    else:
        gun = 1
        if ay < 12:
            ay += 1
        else:
            yil += 1
            ay = 1

    tarih1 = f"{gun}.{ay}.{yil}"
    liste.append(tarih1)
    return tarih(gun, ay, yil, sayac - 1)


print(tarih(28, 12, 2023))
