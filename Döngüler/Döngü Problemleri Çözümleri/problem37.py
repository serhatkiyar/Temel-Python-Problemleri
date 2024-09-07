mevsim_sozluk = {1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan",
                 5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
                 9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"}
print("""
______________________________
MEVSİM BULMA SİSTEMİ
______________________________
""")
ay = int(input("Kaçıncı ayı sorgulamak istiyorsunuz: "))
if 9 <= ay <= 11:
    print("{} ayı sonbahar mevsimindedir.".format(mevsim_sozluk[ay]))
elif 12 <= ay <= 2:
    print("{} ayı kış mevsimindedir.".format(mevsim_sozluk[ay]))
elif 3 <= ay <= 5:
    print("{} ayı ilkbahar mevsimindedir.".format(mevsim_sozluk[ay]))
elif 6 <= ay <= 8:
    print("{} ayı yaz mevsimindedir.".format(mevsim_sozluk[ay]))
