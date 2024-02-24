sozluk = {}
for i in range(1, 4):
    x = int(input(f"{i}. noktanın x değerini giriniz: \n>>> "))
    y = int(input(f"{i}. noktanın y değerini giriniz: \n>>> "))
    sozluk[i] = x, y

sorgux = int(input("Sorgulamak istediğiniz x değerini giriniz: \n>>> "))
sorguy = int(input("Sorgulamak istediğiniz y değerini giriniz: \n>>> "))

xmax = max([sozluk[1][0], sozluk[2][0], sozluk[3][0]])
xmin = min([sozluk[1][0], sozluk[2][0], sozluk[3][0]])
ymax = max([sozluk[1][1], sozluk[2][1], sozluk[3][1]])
ymin = min([sozluk[1][1], sozluk[2][1], sozluk[3][1]])

if sorgux < xmax and sorgux > xmin and sorguy > ymin and sorguy < ymax:
    print("Sorgulanan nokta üçgenin içindedir.")
