print("""
_______________________________
İDEAL KİLO SORGULAMA SİSTEMEİ
_______________________________
""")

cinsiyet = int(input("1-Erkek\n2-Kadın\nSeçim \n>> "))

boy = float(input("Boyunuzu santimetre cinsinden giriniz: "))
kilo = float(input("Kilonuzu kilogram cinsinden giriniz: "))

if cinsiyet == 1:
    print("Boyunuza göre ideal kilonuz = {}".format(boy-108))

    if boy-108 < kilo:
        print("Fazla kilonuz var...")
        print("İdeal kiloya ulaşmanız için {} kilogram kadar vermeniz gerekiyor...".format(kilo-boy-108))

    elif boy-108 > kilo:
        print("Az kilonuz var...")
        print("İdeal kiloya ulaşmanız için {} kilogram kadar almanız gerekiyor...".format(boy-108-kilo))

    else:
        print("Kilonuz ideal")


elif cinsiyet == 2:
    print("Boyunuza göre ideal kilonuz = {}".format(boy - 110))

    if boy - 110 <= kilo:
        print("Fazla kilonuz var...")
        print("İdeal kiloya ulaşmanız için {} kilogram kadar vermeniz gerekiyor...".format(kilo - boy - 110))

    elif boy - 110 > kilo:
        print("Az kilonuz var...")
        print("İdeal kiloya ulaşmanız için {} kilogram kadar almanız gerekiyor...".format(boy - 110 - kilo))

    else:
        print("Kilonuz ideal...")
