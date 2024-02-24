# # ❓*Matrisin İki Satırını Çarpma:*❓
# import random
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
#
# print("Matrisiniz oluşturuldu.")
# matrisciz(matris)
#
# islem_satiri = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> ")) - 1
#
# print(f"{islem_satiri + 1}. satırdaki elemanlar 2 katına alındı. \nYeni Matris")
#
#
# for i in range(len(matris)):
#     matris[islem_satiri][i] *= 2
#
# matrisciz(matris)
#
# # ❓*Matrisin İki Sütununu Çarpma:*❓
# import random
#
# boyut = int(input("Boyut Giriniz: \n>>> "))
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
# islem_sutunu = int(input("işlem yapmak istediğini sütunu giriniz: \n>>> ")) - 1
# print(f"{islem_sutunu + 1}. sütundaki elemanlar 2 katına alındı. \nYeni Matris")
#
# for x in range(len(matris)):
#     matris[x][islem_sutunu] *= 2
#
# matrisciz(matris)
#
# # ❓*Matrisin Belirli Bir Satırını Sıfırlama:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
#
# islem_satiri = int(input("Hangi satırı 0' lamak istersiniz: \n>>> ")) - 1
#
# print(f"{islem_satiri + 1}. satırdaki elemanlar 0' a eşitlendi.")
#
# for i in range(len(matris[0])):
#     matris[islem_satiri][i] *= 0
#
# matrisciz(matris)
#
# # ❓*Matrisin Belirli Bir Sütununu Sıfırlama:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
#
# matrisciz(matris)
#
# islem_sutunu = int(input("İşlem yapmak istediğiniz sütunu giriniz: \n>>> ")) - 1
#
# print(f"{islem_sutunu + 1}. sütunundaki elemanlar 0' a eşitlendi.")
# for i in range(len(matris)):
#     matris[i][islem_sutunu] *= 0
#
# matrisciz(matris)
#
# # ❓*Matrisin Satırlarını Sıralama:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
#
# matrisciz(matris)
#
# islem_satiri = int(input("İşlem yapmak istediğiniz satiri giriniz: \n>>> ")) - 1
# print(f"{islem_satiri + 1}. satırdaki sayılar sıralandı.")
#
# for i in range(len(matris[islem_satiri])):
#     for j in range(len(matris[islem_satiri]) - i - 1):
#         if matris[islem_satiri][j] > matris[islem_satiri][j + 1]:
#             matris[islem_satiri][j], matris[islem_satiri][j + 1] = matris[islem_satiri][j + 1], matris[islem_satiri][j]
#
# matrisciz(matris)
#
# # ❓*Matrisin Sütunlarını Sıralama:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# print("Matris")
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
#
# islem_sutunu = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> ")) - 1
# print(f"{islem_sutunu + 1}. sütundaki değerler sıralandı. \nYeni Matris")
# liste_sutun = []
#
# for i in range(len(matris)):
#     liste_sutun.append(matris[i][islem_sutunu])
#
# for i in range(len(liste_sutun)):
#     for j in range(len(liste_sutun) - i - 1):
#
#         if liste_sutun[j] > liste_sutun[j + 1]:
#             liste_sutun[j], liste_sutun[j + 1] = liste_sutun[j + 1], liste_sutun[j]
#
# for i in range(len(matris)):
#     matris[i][islem_sutunu] = liste_sutun[i]
#
# matrisciz(matris)
#
# # ❓*Matrisin Satır Toplamlarını Bulma:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# print("Matris")
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
#
# print("Toplamlar:")
# for i in range(len(matris)):
#     toplam = 0
#     for j in range(len(matris[0])):
#         toplam += matris[i][j]
#     print(f"{i + 1}. satır toplamı = {toplam}")
#
# # ❓*Matrisin Sütun Toplamlarını Bulma:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
# print("Matris")
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
#
# print("Yeni Matris")
# for i in range(len(matris[0])):
#     toplam = 0
#     for j in range(len(matris)):
#         toplam += matris[j][i]
#     print(f"{i + 1}. sutundaki değerlerin tolamı= {toplam}")
#
# # ❓*Matrisin Satır Ortalamalarını Bulma:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
# print("Matris")
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
# print("Satır ortalamaları")
# for i in range(len(matris)):
#     toplam = 0
#     for j in range(len(matris[0])):
#         toplam += matris[i][j]
#     print(f"{i + 1}. satır ortalaması= {toplam/len(matris[0])}")
#
# # ❓*Matrisin Sütun Ortalamalarını Bulma:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
# print("Matris")
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
# print("Sütun ortalamaları")
#
# for i in range(len(matris[0])):
#     toplam = 0
#     for j in range(len(matris)):
#         toplam += matris[j][i]
#     print(f"{i + 1}. sütun ortalaması= {toplam/len(matris)}")
#
# # ❓*Satır ve Sütun Toplamı:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
# matrisciz(matris)
#
# for i in range(len(matris)):
#     toplam = 0
#     for j in range(len(matris[0])):
#         toplam += matris[i][j]
#     print(f"{i + 1}. satır toplamı= {toplam}")
# for x in range(len(matris[0])):
#     toplam = 0
#     for y in range(len(matris)):
#         toplam += matris[y][x]
#     print(f"{x + 1}. sütun toplamı= {toplam}")
#
# # ❓*Matrisin Sıfıra Eşit Olup Olmadığını Kontrol Etme:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris)
#
# matris_elemanlar = []
# for i in range(len(matris)):
#     for j in range(len(matris[0])):
#         matris_elemanlar.append(matris[i][j])
#
# for i in matris_elemanlar:
#     if i != 0:
#         print("Bu matris 0 matrisi değildir.")
#         break
# else:
#     print("Bu matris 0 matrisidir.")
#
# # ❓*Matrisin İki Satırını Değiştirme:*❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for x in i:
#             print(x, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
# matrix = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matrix)
#
# x = int(input("Değiştirmek istediğiniz 1. satırı giriniz: \n>>> "))
# y = int(input("Değiştirmek istediğiniz 2. satırı giriniz: \n>>> "))
#
# matrix[x - 1], matrix[y - 1] = matrix[y - 1], matrix[x - 1]
#
# matrisciz(matrix)
#
# # ❓*Matrisin İki Sütununu Değiştirme:*❓
# import random
#
#
# def matrixciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrixciz(matris)
#
# x = int(input("Değiştirmek istediğiniz 1. sütunu giriniz: \n>>> "))
# y = int(input("Değiştirmek istediğiniz 2. sütunu giriniz: \n>>> "))
#
# for m in range(len(matris)):
#     matris[m][x - 1], matris[m][y - 1] = matris[m][y - 1], matris[m][x - 1]
#
# matrixciz(matris)
#
# # ❓*Matrisin Belirli Bir Elemanını Değiştirme:*❓
# import random
#
#
# def matrixciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
# matris =[[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrixciz(matris)
#
# satir = int(input("Elemanınız kaçıncı satırda: \n>>> "))
# sutun = int(input("Elemanınız kaçıncı sütunda: \n>>> "))
#
# print(f"Seçilen eleman= {matris[satir - 1][sutun - 1]}")
#
# yeni_eleman = int(input("Yeni eleman gir: \n>>> "))
#
# matris[satir - 1][sutun - 1] = yeni_eleman
# matrixciz(matris)
#
# # ❓*Matrisin Satırlarını Kopyalama:*❓
# import random
#
#
# def matrixciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end= " ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrixciz(matris)
#
# kopya_satir = int(input("Kaçıncı satırı kopyalıyacaksın: \n>>> "))
# yapistir_satir = int(input("Kaçıncı satıra yapıştıracaksın: \n>>> "))
#
# for i in range(len(matris)):
#     matris[yapistir_satir - 1][i] = matris[kopya_satir - 1][i]
#
# matrixciz(matris)
#
# # ❓*Matrisin Sütunlarını Kopyalama:*❓
# import random
#
#
# def matrixciz(matris):
#     for i in matris:
#         for j in i:
#             print(j, end= " ")
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
# matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrixciz(matris)
#
# kopya_sutun = int(input("Hangi sütunu kopyalamak istersiniz: \n>>> "))
# yapistir_sutun = int(input("Hangi sütuna yapıştırmak istersiniz: \n>>> "))
#
# for j in range(len(matris)):
#     matris[j][yapistir_sutun - 1] = matris[j][kopya_sutun - 1]
#
# matrixciz(matris)
#
# Matris Elemanlarının Mutlak Değerini Alma:
# Verilen bir matrisin elemanlarının mutlak değerini alan bir Python programı yazın.
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[random.randint(-9, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris)
#
# for i1 in range(len(matris)):
#     for j1 in range(len(matris[0])):
#         if matris[i1][j1] < 0:
#             matris[i1][j1] = -1 * matris[i1][j1]
#
# print("Yeni Matris")
# matrisciz(matris)
#
# # ❓İki matrisin toplamını bul.❓
# import random
#
#
# def matrisciz(liste):
#
#     for i in range(len(liste)):
#
#         for x in range(len(liste[0])):
#
#             print(liste[i][x], end=" ")
#
#         print()
#
#
# boyut = int(input("Matrisinizin boyutunu giriniz: \n>>> "))
#
# matris1 = [[int(10*random.random()) for x in range(boyut)] for i in range(boyut)]
# matrisciz(matris1)
#
# matris2 = [[int(10*random.random()) for x in range(boyut)] for i in range(boyut)]
# matrisciz(matris2)
#
# matristoplam = [[0 for x in range(boyut)] for i in range(boyut)]
# print("Matris toplamları")
#
# for i in range(boyut):
#
#     for j in range(boyut):
#
#         matristoplam[i][j] = matris1[i][j] + matris2[i][j]
#
# matrisciz(matristoplam)
#
# # ❓Matrisin satır ve sütun toplamlarını hesapla.❓
# import random
#
#
# def matrisciz(liste):
#
#     for i in range(len(liste)):
#
#         for x in range(len(liste[0])):
#
#             print(liste[i][x], end=" ")
#
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for x in range(boyut)] for i in range(boyut)]
# matrisciz(matris)
#
# for i in range(len(matris)):
#
#     satirtoplam = 0
#
#     for j in range(len(matris[0])):
#         satirtoplam += matris[i][j]
#
#     print(satirtoplam, end=" ")
#
# print()
#
# for i in range(len(matris[0])):
#
#     sutuntoplam = 0
#
#     for j in range(len(matris)):
#
#         sutuntoplam += matris[j][i]
#
#     print(sutuntoplam, end=" ")
#
# # ❓Matristeki en büyük sayıyı bul.❓
# import random
#
# boyut = int(input("Matris boyutunu giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
# print(matris)
#
# mak = matris[0][0]
#
# for i in matris:
#
#     for x in i:
#
#         if x >= mak:
#             mak = x
#
# print(mak)
#
# # Matristeki en büyük sayıyı bul.
# import random
#
#
# def matrisciz(liste):
#     print("Matris")
#     for i in range(len(liste)):
#         for j in range(len(liste[0])):
#             print(liste[i][j], end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
# matrisciz(matris)
#
# diyagonaltoplam = 0
#
# for i in range(len(matris)):
#
#     for x in range(len(matris[0])):
#
#         if i == x:
#             diyagonaltoplam += matris[i][x]
#
# print("\nDiyagonal Toplam\n", diyagonaltoplam, sep="")
#
# # ❓Verilen sayıyı matrisin k. indeksine yerleştir?❓
# import random
#
#
# def matrisciz(liste):
#     print("Matris")
#     for i in range(len(liste)):
#         for j in range(len(liste[0])):
#             print(liste[i][j], end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
# matrisciz(matris)
#
# sayi = int(input("Yerleştirmek istediğiniz sayı: \n>>> "))
# index = int(input("Hangi indexe yerleştirilecek: \n>>> "))
# sayacindex = -1
#
# for i in range(len(matris)):
#
#     for x in range(len(matris[0])):
#
#         sayacindex += 1
#
#         if sayacindex == index:
#             matris[i][x] = sayi
#
# matrisciz(matris)
#
# # ❓Verilen sayıyı matrisin k. indeksine yerleştir?❓
# import random
#
#
# def matrixciz(liste):
#
#     print("Matris")
#
#     for i in range(len(liste)):
#
#         for x in range(len(liste[0])):
#             print(liste[i][x], end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
# matrixciz(matris)
#
# matristranspoz = [[0 for i in range(boyut)] for x in range(boyut)]
#
# for i in range(len(matris)):
#
#     for j in range(len(matris[0])):
#
#         matristranspoz[i][j] = matris[j][i]
#
# matrixciz(matristranspoz)
#
# # ❓İki matrisin çarpımını hesaplayan prog?❓
# import random
#
#
# def matrisciz(liste):
#
#     print("Matris")
#
#     for i in range(len(liste)):
#
#         for x in range(len(liste[0])):
#
#             print(liste[i][x], end=" ")
#
#         print()
#
#
# boyut = int(input("Boyut gir: \n>>> "))
#
# matris1 = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
# matrisciz(matris1)
#
# matris2 = [[int(10*random.random()) for i in range(boyut)] for x in range(boyut)]
# matrisciz(matris2)
#
# matris3 = [[0 for i in range(boyut)] for x in range(boyut)]
#
# for i in range(len(matris1)):
#
#     for j in range(len(matris1[0])):
#
#         matris3[i][j] = matris1[i][j] * matris2[i][j]
#
# matrisciz(matris3)
#
#
# # ❓Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.❓
# def matrisciz(liste):
#     print("Matris")
#     for i in range(len(liste)):
#         for j in range(len(liste[0])):
#             print(liste[i][j], end=" ")
#         print()
#
#
# N = int(input("Boyut(N) giriniz: \n>>> "))
# matris = [[i for i in range(x + 1 - N, x + 1)] for x in range(N, N ** 2 + 1, N)]
# matrisciz(matris)
#
# # ❓Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.❓
# import random
#
# def matrisciz(liste):
#     print("Matris")
#     for i in range(len(liste)):
#         for j in range(len(liste[0])):
#             print(liste[i][j], end=" ")
#         print()
#
# boyut = int(input("Boyut Gir: \n>>> "))
#
# matris = [[random.choice([0, 1]) for i in range(boyut)] for x in range(boyut)]
#
# matrisciz(matris)
# alan = 0
# for i in range(len(matris)):
#     for j in range(len(matris[0])):
#         if matris[i][j] == 1:
#             alan += 1
# print(alan)
#
# # ❓Matrisin Belirli Bir Elemanını Bulma:❓
# # ❓Verilen bir matrisin belirli bir elemanını bulan bir Python programı yazın.❓
#
# import random
# boyut = int(input("Boyut giriniz: \n>>> "))
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# matris = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris)
#
# eleman_bul = int(input("Hangi elemanı arıyorsunuz: \n>>> "))
# print(f"Aranan eleman= {eleman_bul}")
# for x in range(len(matris)):
#     for y in range(len(matris[0])):
#         if matris[x][y] == eleman_bul:
#             print(f"{x}. satır {y}. sütun")
#
# # ❓Matrisin Belirli Bir Satırını Silme:❓
# # ❓Verilen bir matrisin belirli bir satırını silen bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# satir_sil = int(input("Kaçıncı index' teki satırı sileceksiniz: \n>>> "))
#
# matris_2 = []
#
# for i in range(len(matris_1)):
#     if i != satir_sil:
#         matris_2.append(matris_1[i])
#
# matrisciz(matris_2)
#
# # ❓Matrisin Belirli Bir Sütununu Silme:❓
# # ❓Verilen bir matrisin belirli bir sütununu silen bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matris_2 = []
# matrisciz(matris_1)
#
# sutun_sil = int(input("Kaçıncı index' teki sütunu silmek istiyorsunuz: \n>>> "))
#
# for i in range(len(matris_1)):
#     liste_eleman_tasiyici = []
#     for j in range(len(matris_1[0])):
#         if j != sutun_sil:
#             liste_eleman_tasiyici.append(matris_1[i][j])
#     matris_2.append(liste_eleman_tasiyici)
#
# matrisciz(matris_2)
#
# # ❓Matrisin Satırlarını Karıştırma:❓
# # ❓Verilen bir matrisin satırlarını karıştıran bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matris_2 = []
# matrisciz(matris_1)
#
# karis_satir_elemanlar = []
#
#
# karis_satir1 = int(input("Karıştırmak istediğiniz 1. Satırı giriniz: \n>>> "))
# karis_satir2 = int(input("Karıştırmak istediğiniz 2. Satırı giriniz: \n>>> "))
#
# for i in range(len(matris_1)):
#     for j in range(len(matris_1[0])):
#         if i != karis_satir1 and i != karis_satir2:
#             continue
#         else:
#             karis_satir_elemanlar.append(matris_1[i][j])
# print("Satırlar karıştırılırken kullanılacak elemanlar=", karis_satir_elemanlar)
#
# for i in range(len(matris_1)):
#     liste_eleman_tasiyici = []
#     for j in range(len(matris_1[0])):
#         if i != karis_satir1 and i != karis_satir2:
#             liste_eleman_tasiyici.append(matris_1[i][j])
#         else:
#             a = random.choice(karis_satir_elemanlar)
#             liste_eleman_tasiyici.append(a)
#             karis_satir_elemanlar.remove(a)
#     matris_2.append(liste_eleman_tasiyici)
#
# print("Karıştırılmış Matris: ")
# matrisciz(matris_2)
#
# # ❓Matrisin Sütunlarını Karıştırma:❓
# # ❓Verilen bir matrisin sütunlarını karıştıran bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matris_2 = []
# matrisciz(matris_1)
#
# karistirilan_elemanlar = []
#
# karis_sutun_1 = int(input("Karıştırmak istediğiniz 1. Sütunu giriniz: \n>>> "))
# karis_sutun_2 = int(input("Karıştırmak istediğiniz 2. Sütunu giriniz: \n>>> "))
#
# for x in range(len(matris_1)):
#     for y in range(len(matris_1[0])):
#         if y == karis_sutun_1 or y == karis_sutun_2:
#             karistirilan_elemanlar.append(matris_1[x][y])
#
# print("Sütunlar karıştırılırken kullanılacak elemanlar=", karistirilan_elemanlar)
# for n in range(len(matris_1)):
#     liste_eleman_tasiyici = []
#     for m in range(len(matris_1[0])):
#         if m != karis_sutun_1 and m != karis_sutun_2:
#             liste_eleman_tasiyici.append(matris_1[n][m])
#         else:
#             a = random.choice(karistirilan_elemanlar)
#             liste_eleman_tasiyici.append(a)
#             karistirilan_elemanlar.remove(a)
#     matris_2.append(liste_eleman_tasiyici)
#
# print("Karıştırılmış Matrix")
# matrisciz(matris_2)
#
# # ❓Matrisin Satırlarını Tersten Yazma:❓
# # ❓Verilen bir matrisin satırlarını tersten yazan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matirs_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matirs_1)
#
# for i in matirs_1:
#     for x in range(len(i)):
#         for y in range(len(i) - x - 1):
#             i[y], i[y + 1] = i[y + 1], i[y]
#
# print("Tersten yazılmış matrix")
# matrisciz(matirs_1)
#
# # ❓Matrisin Sütunlarını Tersten Yazma:❓
# # ❓Verilen bir matrisin sütunlarını tersten yazan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sutunlar = []
#
# for x in range(len(matris_1)):
#     listeleyici = []
#     for y in range(len(matris_1[0])):
#         listeleyici.append(matris_1[y][x])
#     sutunlar.append(listeleyici)
#
# for m in range(len(sutunlar)):
#
#     for o in range(len(sutunlar)):
#         for t in range(len(sutunlar) - o - 1):
#             sutunlar[m][t], sutunlar[m][t + 1] = sutunlar[m][t + 1], sutunlar[m][t]
#
#     for x2 in range(len(matris_1)):
#         matris_1[x2][m] = sutunlar[m][x2]
#
# print("Tersten yazılmış matrix")
# matrisciz(matris_1)
#
# # ❓Matrisin Sütunlarını Tersten Yazma:❓
# # ❓Verilen bir matrisin sütunlarını tersten yazan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for x in range(len(matris_1)):
#     for y in range(len(matris_1[0])//2):
#         matris_1[y][x], matris_1[len(matris_1) - y - 1][x] = matris_1[len(matris_1) - y - 1][x], matris_1[y][x]
#
# print("Tersten yazılmış matrix")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Satırını Ters Çevirme:❓
# # ❓Verilen bir matrisin belirli bir satırını ters çeviren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10 * random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# satir_sec = int(input("Hangi satırı ters çevirmek istersiniz: \n>>> "))
# print("işlem yapılacak satır=", matris_1[satir_sec])
#
# for i in range(len(matris_1[0])//2):
#     matris_1[satir_sec][i], matris_1[satir_sec][len(matris_1) - i - 1] =\
#         matris_1[satir_sec][len(matris_1) - i - 1], matris_1[satir_sec][i]
#
# print("Ters çevirilmiş Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Sütununu Ters Çevirme:❓
# # ❓Verilen bir matrisin belirli bir sütununu ters çeviren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# s_s = int(input("Hangi sütunu ters çevirmek istersiniz: \n>>> "))
# for y in range(len(matris_1[0])//2):
#     matris_1[y][s_s], matris_1[len(matris_1[0]) - y - 1][s_s] = matris_1[len(matris_1[0]) - y - 1][s_s], matris_1[y][s_s]
#
# print("Ters çevrilmiş Matrix")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Bölgesini Sıfırlama:❓
# # ❓Verilen bir matrisin belirli bir bölgesini sıfırlayan bir Python programı yazın.❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sozluk = {}
# for x in range(1, 3):
#     satir_sec = int(input(f"{x}. Noktanın satırını giriniz: \n>>> "))
#     sutun_sec = int(input(f"{x}. Noktanın sütununu giriniz: \n>>> "))
#     sozluk["nokta" + str(x)] = [satir_sec, sutun_sec]
#
# print(sozluk)
#
# for i in range(len(matris_1)):
#     for j in range(len(matris_1[0])):
#         if (sozluk["nokta1"][0] <= i <= sozluk["nokta2"][0] or sozluk["nokta1"][0] >= i >= sozluk["nokta2"][0]) and \
#                 (sozluk["nokta1"][1] <= j <= sozluk["nokta2"][1] or sozluk["nokta1"][1] >= j >= sozluk["nokta2"][1]):
#             matris_1[i][j] = 0
#
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Bölgesini Toplama:❓
# # ❓Verilen bir matrisin belirli bir bölgesinin elemanlarını toplayan bir Python programı yazın.❓
#
# import random
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sozluk = {}
# for i in range(1, 3):
#     satir_sec = int(input(f"{i}. noktanın satırını giriniz: \n>>> "))
#     sutun_sec = int(input(f"{i}. noktanın sütununu giriniz: \n>>> "))
#     sozluk["n" + str(i)] = [satir_sec, sutun_sec]
#
# toplam = 0
#
# for i in range(len(matris_1)):
#     for j in range(len(matris_1[0])):
#         if (sozluk["n1"][0] <= i <= sozluk["n2"][0] or sozluk["n1"][0] >= i >= sozluk["n2"][0]) and \
#                 (sozluk["n1"][1] <= j <= sozluk["n2"][1] or sozluk["n1"][1] >= j >= sozluk["n2"][1]):
#             toplam += matris_1[i][j]
#
# print("toplam=", toplam)
#
# # ❓Matrisin Satırlarını Ortalamaya Göre Sıralama:❓
# # ❓Verilen bir matrisin satırlarını ortalamaya göre küçükten büyüğe sıralayan bir Python programı yazın.❓
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# ortalamalar = []
# for i in matris_1:
#     toplam = 0
#     for j in i:
#         toplam += j
#     ortalamalar.append(toplam/len(matris_1[0]))
# print("ortalamalar=", ortalamalar)
#
# for i in range(len(ortalamalar)):
#     for j in range(len(ortalamalar) - i - 1):
#         if ortalamalar[j + 1] > ortalamalar[j]:
#             matris_1[j + 1], matris_1[j] = matris_1[j], matris_1[j + 1]
#             ortalamalar[j + 1], ortalamalar[j] = ortalamalar[j], ortalamalar[j + 1]
#
# print("Sıralanmış Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Sütunlarını Ortalamaya Göre Sıralama:❓
# # ❓Verilen bir matrisin sütunlarını ortalamaya göre küçükten büyüğe sıralayan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut Giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sutunlar = []
#
# for i2 in range(len(matris_1)):
#     gecici_liste = []
#     for j2 in range(len(matris_1[0])):
#         gecici_liste.append(matris_1[j2][i2])
#     sutunlar.append(gecici_liste)
#
# sutun_ortalamalar = []
# for u in sutunlar:
#     toplam = 0
#     for p in u:
#         toplam += p
#     sutun_ortalamalar.append(toplam/3)
#
# print("Sütun ortalamaları=", sutun_ortalamalar)
#
# for i3 in range(len(sutun_ortalamalar)):
#     for j3 in range(len(sutun_ortalamalar) - i3 - 1):
#         if sutun_ortalamalar[j3 + 1] > sutun_ortalamalar[j3]:
#             sutunlar[j3 + 1], sutunlar[j3] = sutunlar[j3], sutunlar[j3 + 1]
#             sutun_ortalamalar[j3 + 1], sutun_ortalamalar[j3] = sutun_ortalamalar[j3], sutun_ortalamalar[j3 + 1]
#
# print(sutunlar)
#
# for a in range(len(sutunlar)):
#     for b in range(len(sutunlar[0])):
#         matris_1[a][b] = sutunlar[b][a]
#
# print("Sıralanmış Matris")
# matrisciz(matris_1)
#
# # ❓Matris Elemanlarını Karekök Alma:❓
# # ❓Verilen bir matrisin elemanlarının karekökünü alan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(f"{str(j)[:3]}", end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i in range(len(matris_1)):
#     for j in range(len(matris_1[0])):
#         matris_1[i][j] = matris_1[i][j] ** (1/2)
#
# print("Karakök alındı! Yeni Matrix: ")
# matrisciz(matris_1)
#
# # ❓Matris Elemanlarını Üs Alma:❓
# # ❓Verilen bir matrisin elemanlarını belirli bir üs kuvvetine yükselten bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# us = int(input("Üs değerini giriniz: \n>>> "))
#
# for i2 in range(len(matris_1)):
#     for j2 in range(len(matris_1[0])):
#         matris_1[i2][j2] = matris_1[i2][j2] ** us
#
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Satırını Belirli Bir Değerle Çarpma:❓
# # ❓Verilen bir matrisin belirli bir satırını belirli bir değerle çarpan bir Python programı yazın.❓
#
# import random
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# hangi_satir = int(input("Hangi satırı çarpmak istersiniz: \n>>> "))
# hangi_sayi = int(input(f"{hangi_satir}. satırı hangi sayı ile çarpmak istersiniz: \n>>> "))
#
# for j2 in range(len(matris_1[0])):
#     matris_1[hangi_satir][j2] = matris_1[hangi_satir][j2] * hangi_sayi
#
# print("İşte yeni matrixin canım: ")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Sütununu Belirli Bir Değerle Çarpma:❓
# # ❓Verilen bir matrisin belirli bir sütununu belirli bir değerle çarpan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# hangi_sutun = int(input("Hangi sütunu çarpmak istiyorsunuz: \n>>> "))
# hangi_sayi = int(input(f"{hangi_sutun}. sütunu hangi sayı ile çarpmak istiyorsunuz: \n>>> "))
#
# for j2 in range(len(matris_1)):
#     matris_1[j2][hangi_sutun] = matris_1[j2][hangi_sutun] * hangi_sayi
#
# matrisciz(matris_1)
#
# # ❓Matrisin Satırlarını Ortalama ile Değiştirme:❓
# # ❓Verilen bir matrisin satırlarını ortalamayla değiştiren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1)):
#     toplam = 0
#
#     for j1 in range(len(matris_1[0])):
#         toplam += matris_1[i1][j1]
#
#     for j2 in range(len(matris_1[0])):
#         (matris_1[i1][j2]) = float(str(toplam / 3)[:3])
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Sütunlarını Ortalama ile Değiştirme:❓
# # ❓Verilen bir matrisin sütunlarını ortalamayla değiştiren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1[0])):
#     toplam = 0
#
#     for j1 in range(len(matris_1)):
#         toplam += matris_1[j1][i1]
#
#     for j2 in range(len(matris_1)):
#         (matris_1[j2][i1]) = float(str(toplam / 3)[:3])
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Satırındaki En Küçük ve En Büyük Elemanları Bulma:❓
# # ❓Verilen bir matrisin belirli bir satırındaki en küçük ve en büyük elemanları bulan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# def listemaxmin(liste):
#
#     maksimum = liste[0]
#     minumum = liste[0]
#
#     for i in liste:
#         if maksimum < i:
#             maksimum = i
#         if minumum > i:
#             minumum = i
#     return [minumum, maksimum]
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# print()
#
# for i1 in range(len(matris_1)):
#     print(f"{i1}. listenin maksimum değeri= {listemaxmin(matris_1[i1])[1]} / "
#           f"Minumum değeri= {listemaxmin(matris_1[i1])[0]}")
#
# # ❓Matrisin Belirli Bir Sütunundaki En Küçük ve En Büyük Elemanları Bulma:❓
# # ❓Verilen bir matrisin belirli bir sütunundaki en küçük ve en büyük elemanları bulan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i1 in matrix:
#         for j1 in i1:
#             print(j1, end=" ")
#         print()
#
#
# def listemakmin(liste):
#     maksimum = liste[0]
#     minumum = liste[0]
#
#     for sayi in liste:
#         if maksimum < sayi:
#             maksimum = sayi
#         if minumum > sayi:
#             minumum = sayi
#     return [minumum, maksimum]
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sutunlar = []
#
# for i in range(len(matris_1[0])):
#     gecici_liste = []
#     for j in range(len(matris_1)):
#         gecici_liste.append(matris_1[j][i])
#     sutunlar.append(gecici_liste)
#
# print()
#
# for i2 in range(len(sutunlar)):
#     print(f"{i2}. sütunun maksimum değeri= {listemakmin(sutunlar[i2])[1]} / "
#           f"minumum değeri= {listemakmin(sutunlar[i2])[0]}")
#
# # ❓Matrisin Satırları Arasındaki Farkları Bulma:❓
# # ❓Verilen bir matrisin ardışık satırları arasındaki farkları bulan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# print()
#
# for i1 in range(len(matris_1) - 1):
#     print(f"{i1}. satır ile {i1 + 1}. satırları arasındaki fark: ")
#     for j1 in range(len(matris_1[0])):
#         print(f"{matris_1[i1][j1] - matris_1[i1 + 1][j1]}", end=" ")
#     print()
#
# # ❓Matrisin Sütunları Arasındaki Farkları Bulma:❓
# # ❓Verilen bir matrisin ardışık sütunları arasındaki farkları bulan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# print()
#
# for i1 in range(len(matris_1[0]) - 1):
#     print(f"{i1}. sütun ile {i1 + 1}. sütun farkı: ")
#     for j1 in range(len(matris_1)):
#         print(f"{matris_1[j1][i1] - matris_1[j1][i1 + 1]:2}")
#     print()
#
# # ❓Matrisin Belirli Bir Satırındaki Elemanları Çarpan Bir Matris Oluşturma:❓
# # ❓Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla çarpan bir matris❓
# # oluşturan bir Python programı yazın.
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# satir_sec = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> "))
# carpan_sayi = int(input(f"{satir_sec}. satırı hangi sayı ile çarpmak istersiniz: \n>>> "))
#
# for j1 in range(len(matris_1[0])):
#     matris_1[satir_sec][j1] *= carpan_sayi
#
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Sütunundaki Elemanları Çarpan Bir Matris Oluşturma:❓
# # ❓Verilen bir matrisin belirli bir sütunundaki elemanları❓
# # ❓belirli bir sayıyla çarpan bir matris oluşturan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[int(10*random.random()) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> "))
# carpan_sayi = int(input(f"{sec_sutun}. sütunu hangi sayı ile çarpmak istersiniz: \n>>> "))
#
# for i in range(len(matris_1)):
#     matris_1[i][sec_sutun] *= carpan_sayi
#
# matrisciz(matris_1)
#
# # ❓Matrisin Satırlarındaki Elemanların Toplamının Sıfır Olup Olmadığını Kontrol Etme:❓
# # ❓Verilen bir matrisin satırlarındaki elemanların toplamının sıfır olup olmadığını❓
# # ❓kontrol eden bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[int(random.randint(-9, 9)) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris)
#
# for i1 in range(len(matris)):
#     toplam = 0
#     for j1 in range(len(matris[0])):
#         toplam += matris[i1][j1]
#     if toplam == 0:
#         print(f"{i1}. satır toplamı 0' dır")
#     else:
#         print(f"{i1}. satır toplamı 0 değildir.")
#
# # ❓Matrisin Sütunlarındaki Elemanların Toplamının Sıfır Olup Olmadığını Kontrol Etme:❓
# # ❓Verilen bir matrisin sütunlarındaki elemanların toplamının sıfır olup❓
# # ❓olmadığını kontrol eden bir Python programı yazına❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(-9, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1[0])):
#     toplam = 0
#
#     for j1 in range(len(matris_1)):
#         toplam += matris_1[j1][i1]
#
#     if toplam == 0:
#         print(f"{i1}. sütun toplamı 0' dır.")
#     else:
#         print(f"{i1}. sütun toplamı 0 değildir.")
#
# # ❓Matrisin Belirli Bir Satırındaki Elemanları Bölme:❓
# # ❓Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla bölen bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sec_satir = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> "))
# bolen_sayi = int(input(f"{sec_satir}. satırı hangi sayı ile bölmek istersiniz: \n>>> "))
#
# for j1 in range(len(matris_1[0])):
#     (matris_1[sec_satir][j1]) = float(str(matris_1[sec_satir][j1] / bolen_sayi)[:3])
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Sütunundaki Elemanları Bölme:❓
# # ❓Verilen bir matrisin belirli bir sütunundaki elemanları belirli bir sayıyla bölen bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> "))
# bolen_sayi = int(input(f"{sec_sutun}. sütunu hangi sayı ile bölmek istersiniz:\n>>> "))
#
# for i1 in range(len(matris_1)):
#     (matris_1[i1][sec_sutun]) = float(str(matris_1[i1][sec_sutun] / bolen_sayi)[:3])
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Satırlarını Tersine Çevirme:❓
# # ❓Verilen bir matrisin satırlarını tersine çeviren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1)):
#     for j1 in range(len(matris_1[0])):
#         for u in range(len(matris_1[0]) - j1 - 1):
#             if matris_1[i1][u] < matris_1[i1][u + 1]:
#                 matris_1[i1][u], matris_1[i1][u + 1] = matris_1[i1][u + 1], matris_1[i1][u]
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Sütunlarını Tersine Çevirme:❓
# # ❓Verilen bir matrisin sütunlarını tersine çeviren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1[0])):
#     for j1 in range(len(matris_1)):
#         for u in range(len(matris_1) - j1 - 1):
#             if matris_1[u][i1] < matris_1[u + 1][i1]:
#                 matris_1[u][i1], matris_1[u + 1][i1] = matris_1[u + 1], matris_1[u][i1]
#
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Satırındaki Elemanları Toplama:❓
# # ❓Verilen bir matrisin belirli bir satırındaki elemanları toplayan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sec_satir = int(input("Hangi satır üzerinde işlem yapmak istersiniz: \n>>> "))
#
# toplam = 0
#
# for j1 in range(len(matris_1[sec_satir])):
#     toplam += matris_1[sec_satir][j1]
# print(f"{sec_satir}. satır toplamı= {toplam}")
#
# # ❓Matrisin Belirli Bir Sütunundaki Elemanları Toplama:❓
# # ❓Verilen bir matrisin belirli bir sütunundaki elemanları toplayan bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# toplam = 0
#
# sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istersiniz: \n>>> "))
#
# for i1 in range(len(matris_1)):
#     toplam += matris_1[i1][sec_sutun]
#
# print(f"{sec_sutun}. sütun toplamı= {toplam}")
#
# # ❓Matrisin Satırlarını Rasgele Yer Değiştirme:❓
# # ❓Verilen bir matrisin satırlarını rasgele yer değiştiren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0,  9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1)):
#     gecici_liste = matris_1[i1].copy()
#
#     for j1 in range(len(matris_1[i1])):
#         a = random.randint(0, len(gecici_liste) - 1)
#         matris_1[i1][j1] = gecici_liste[a]
#         gecici_liste.pop(a)
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Sütunlarını Rasgele Yer Değiştirme:❓
# # ❓Verilen bir matrisin sütunlarını rasgele yer değiştiren bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# for i1 in range(len(matris_1[0])):
#     sutun = []
#     for i2 in range(len(matris_1)):
#         sutun.append(matris_1[i2][i1])
#     for j1 in range(len(matris_1)):
#         a = random.randint(0, len(sutun) - 1)
#         matris_1[j1][i1] = sutun[a]
#         sutun.pop(a)
#
# print("Yeni Matris")
# matrisciz(matris_1)
#
# # ❓Matrisin Belirli Bir Satırındaki Elemanları Güçlendirme:❓
# # ❓Verilen bir matrisin belirli bir satırındaki elemanları belirli bir sayıyla kuvvetine yükselten bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris)
#
# sec_satir = int(input("Hangi satır üzerinde işlem yapmak istiyorsunuz: \n>>> "))
#
# kuvvet = int(input(f"{sec_satir}. satırın alınacağı kuvvet değerini giriniz: \n>>> "))
#
# for j1 in range(len(matris[0])):
#     matris[sec_satir][j1] **= kuvvet
#
# print("Yeni Matris")
# matrisciz(matris)
#
# # ❓Matrisin Belirli Bir Sütunundaki Elemanları Güçlendirme:❓
# # ❓Verilen bir matrisin belirli bir sütunundaki elemanları belirli bir sayıyla❓
# # ❓kuvvetine yükselten bir Python programı yazın.❓
#
# import random
#
#
# def matrisciz(matrix):
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# boyut = int(input("Boyut giriniz: \n>>> "))
#
# matris_1 = [[random.randint(0, 9) for _ in range(boyut)] for _ in range(boyut)]
# matrisciz(matris_1)
#
# sec_sutun = int(input("Hangi sütun üzerinde işlem yapmak istiyorsunuz: \n>>> "))
# kuvvet = int(input(f"{sec_sutun}. sütunun alınacağı kuvvet değerini giriniz: \n>>> "))
#
# for j1 in range(len(matris_1)):
#     matris_1[j1][sec_sutun] **= kuvvet
#
# print("Yeni Matris")
# matrisciz(matris_1)
