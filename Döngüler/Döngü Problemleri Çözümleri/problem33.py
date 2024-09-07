while True:
    print("""
    _____________________________________________
    SİPARİŞ KARGO ÜCRETLENDİRME SORGU SİSTEMİ
    _____________________________________________
    """)
    siparis_tutari = float(input("Sipariş tutarınızı giriniz: "))
    if siparis_tutari < 50:
        print("Güncel sipariş fatura tutarınız {}' dir.".format(siparis_tutari+7))
    elif siparis_tutari >= 50:
        print("Kargo ücretsiz...")
        print("Güncel sipariş fatura tutarınız {}' dir.".format(siparis_tutari))


