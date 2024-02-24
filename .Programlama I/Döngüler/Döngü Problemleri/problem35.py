print("""
_____________________
İŞ BAŞVURU SİSTEMİ
_____________________
""")
bilme_java = int(input("Java dilini biliyor musunuz? (Evet = 1, Hayır = 0): "))
bilme_python = int(input("Python dilini biliyor musunuz? (Evet = 1, Hayır = 0): "))
bilme_ingilizce = int(input("İngilizce dilini biliyor musunuz? (Evet = 1, Hayır = 0: "))

if bilme_ingilizce == 1 and (bilme_python == 1 or bilme_python == 1):
    print("İş alım süreciniz olumlu geçti...")

else:
    print("Aranan pozisyona nitelikleriniz uymamaktadır...")