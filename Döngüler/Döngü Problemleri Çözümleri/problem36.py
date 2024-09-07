print("""
____________________
İNDİRİM MERKEZİ
____________________
""")

tutar = int(input("Alışveriş yaptığınız tutarı giriniz: "))

if 0 > tutar < 200:
    print("%10 indiriminiz var.")
    print("İndirimler uygulanıyor...")
    print("Güncel Tutar {} TL'dir.".format(tutar * 0.9))

elif 400 > tutar >= 200:
    print("%15 indiriminiz var.")
    print("İndirimler uygulanıyor...")
    print("Güncel Tutar {} TL'dir.".format(0.85 * tutar))

elif tutar >= 400:
    print("%20 indiriminiz var.")
    print("İndirimler uygulanıyor...")
    print("Güncel Tutar {} TL'dir.".format(0.8 * tutar))
