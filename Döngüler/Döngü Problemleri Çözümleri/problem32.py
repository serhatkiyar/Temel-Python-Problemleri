hediye_puan = 0


while True:
    print("""
    ___________________________________________________
    Alışveriş Merkezi
    ___________________________________________________
    *Hediye Puan Sorgu - 1
    *Alışveriş - 2
    """)
    x = int(input("İşlem seçiniz: "))
    if x == 1:
        print("Hediye Puanınız: ", hediye_puan)
    elif x == 2:
        harcama = int(input("Harcamak istediğiniz tutarı giriniz: "))
        if harcama < 1000:
            print("***10 Hediye Puan Kazandınız.***")
            hediye_puan += 10
        elif 1000 <= harcama < 2000:
            print("***50 Hediye Puan Kazandınız.***")
            hediye_puan += 50
        elif harcama > 2000:
            hediye_puan += 100
            print("***100 Hediye Puan Kazandınız.***")
    else:
        print("Geçersiz İşlem.")
