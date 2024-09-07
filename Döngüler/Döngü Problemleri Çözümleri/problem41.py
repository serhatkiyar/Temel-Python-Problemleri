liste = []


for i in range(1, 6):
    sayi = int(input("{}. sayıyı giriniz: ".format(i)))
    liste.append(sayi)

for i in range(len(liste)):
    for j in range(0, len(liste) - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]


print(f"Oluşturulan listedeki minumum değer {liste[0]} iken maximum değer {liste[len(liste) - 1]}' dir.")
