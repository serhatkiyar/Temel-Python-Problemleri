print("""
________________________________________________
               HESAP MAKİNESİ
________________________________________________ """)
total = 0
while True:
    print("""     MENÜ
    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme
    """)
    print("Güncel değer: {}".format(total))
    islem_numarasi = int(input("İşlem numarası seçiniz: "))
    if islem_numarasi == 1:
        print("Toplama işlemi seçildi.")
        count = 1
        while True:
            sayi = input("{}. sayıyı giriniz.(Kaydetmek için 'q' ya basınız): ".format(count))
            if sayi == "q":
                print("Sonuç: {}".format(total))
                break
            count += 1
            total += int(sayi)
            print("Sonuç: {}".format(total))
        continue
    if islem_numarasi == 2:
        print("Çıkarma işlemi seçildi.")
        count = 1
        print("Güncel değer: {}".format(total))
        sayi = input("Çıkarmak istediğiniz {}. sayıyı giriniz.(Kaydetmek için 'q' ya basınız): ".format(count))
        if sayi == "q":
            print("Sonuç: {}".format(total))
        else:
            total -= int(sayi)
            print("Sonuç: {}".format(total))
        count += 1
        while True:
            sayi = input("Çıkarmak istediğiniz {}. sayıyı giriniz.(Kaydetmek için 'q' ya basınız): ".format(count))
            if sayi == "q":
                print("Sonuç: {}".format(total))
                break
            else:
                total -= int(sayi)
                print("Sonuç: {}".format(total))
            count += 1
        continue
    if islem_numarasi == 3:
        total = 1
        print("Çarpma işlemi seçildi.")
        count = 1
        while True:
            sayi = input("Çarpamak için {}. sayıyı giriniz.(Kaydetmek için 'q' ya basınız): ".format(count))
            if sayi == "q":
                print("Sonuç: {}".format(total))
                break
            count += 1
            total *= int(sayi)
            print("Sonuç: {}".format(total))
        continue
    if islem_numarasi == 4:
        print("Bölme işlemi seçildi.")
        count = 1
        while True:
            sayi = input("Bölmek için {}. sayıyı giriniz.(Kaydetmek için 'q' ya basınız): ".format(count))
            if sayi == "q":
                print("Sonuç: {}".format(total))
                break
            count += 1
            total /= int(sayi)
            print("Sonuç: {}".format(total))
        continue