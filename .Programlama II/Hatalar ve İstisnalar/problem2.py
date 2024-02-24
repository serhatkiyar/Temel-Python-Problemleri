sayi = int(input("Bir sayı giriniz: "))


def ciftkontrol(x):

    if x % 2 != 0:
        raise ValueError
    else:
        return x


try:
    print(ciftkontrol(sayi))

except ValueError:
    print("Tek sayı olm bu :D ahfjakfldsghsdlgkjl")
