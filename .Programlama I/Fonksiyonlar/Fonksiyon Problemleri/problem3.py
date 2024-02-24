# Listede en fazla tekrar eden eleman bulan program

def maxtekrarbul(*tuple1):
    sayilar = {}
    tekrarsayilari = []

    for i in tuple1:
        sayac = 0

        for j in tuple1:

            if i == j:
                sayac += 1
        sayilar[i] = sayac

    for i in range(len(sayilar)):
        tekrarsayilari.append(sayilar[i])

    for i in range(len(tekrarsayilari)):
        for j in range(1, i - 1):

            if tekrarsayilari[i] > tekrarsayilari[j]:
                (tekrarsayilari[i], tekrarsayilari[j]) = (tekrarsayilari[j], tekrarsayilari[i])
    print(tekrarsayilari)
    print(tekrarsayilari[0])




print(maxtekrarbul(1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 1, 2, 3, 8))
