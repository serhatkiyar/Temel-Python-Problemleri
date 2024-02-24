# # Soru 1 Digital saat
#
# def DigitalSaat(saat, dakika, saniye):
#     liste = []
#     for i in range(5):
#         liste.append(f"{saat}.{dakika}.{saniye}")
#         if saniye < 60:
#             saniye += 1
#             if saniye == 60:
#                 dakika += 1
#                 if dakika == 60:
#                     saat += 1
#         if saniye == 60:
#             saniye = 0
#         if dakika == 60:
#             dakika = 0
#         if saat == 24:
#             saat =0
#     return liste
#
# print(DigitalSaat(18, 23, 58))

# Soru 2 Verilen iki sayı arasında 3 e bölünme

# def Listeyiolustur(baslangic, bitis):
#     liste = []
#     for i in range(baslangic, bitis):
#         if i % 3 == 0:
#             liste.append(i)
#     return liste
# #
# print(Listeyiolustur(20, 25))

# Soru 4 Uzunluğu çift olan ve tam sayı

# def Yerdegis():
#     liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for i in range(0, len(liste), 2):
#         a = liste[i]
#         b = liste[i + 1]
#         liste[i + 1] = a
#         liste[i] = b
#     return liste

# print(Yerdegis())

# Soru 3 baslangıc bitis

# def RasgeleSayiliListeUret(baslangic, bitis, adet):
#     import random
#     liste = []
#     for i in range(adet):
#         liste.append(random.randint(baslangic, bitis))
#     return liste
#
# print(RasgeleSayiliListeUret(5,8,10))

# Soru 6

# def Bozanelemanindeksi():
#     liste2 = []
#     liste = [1, 3, 5, 7, 9, 12, 13]
#     for i in range(0, len(liste)):
#         liste2.append(liste[i] - liste[i + 1])
#     index = 0
#     for x in liste2:
#         if x != max(liste2):
#             return index
#         index += 1
# print(Bozanelemanindeksi())