def tarih(gun, ay, yil):

    liste = []

    for i in range(7):
        if gun < 30:
            gun += 1
        else:
            gun = 1
            if ay < 12:
                ay += 1
            else:
                yil += 1
                ay = 1
        liste.append(f"{gun}.{ay}.{yil}")

    return liste


print(tarih(29, 12, 2004))
