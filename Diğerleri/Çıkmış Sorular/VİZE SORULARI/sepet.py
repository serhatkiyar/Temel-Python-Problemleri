# Üç farÜç farklı top sepeti düşünelim. Bunlara sırayla k adet top ekleme veya
# çıkarma yapılıyor. k değeri her adımda [1, 2, 3] değerlerinden rastgele birini alıyor.
# Her adımda ekleme veya çıkarma yapılacağına da rastgele karar veriliyor. Sepetlerden birinde
# 5 veya daha fazla top biriktiğinde program sonlanıyor. Program örnek bir çıktısı
# aşağıdaki gibidirklı top sepeti düşünelim. Bunlara sırayla k adet top ekleme veya
# çıkarma yapılıyor. k değeri her adımda [1, 2, 3] değerlerinden rastgele birini alıyor.
# Her adımda ekleme veya çıkarma yapılacağına da rastgele karar veriliyor.
# Sepetlerden birinde 5 veya daha fazla top biriktiğinde program sonlanıyor.

import random

sepet_1 = []
sepet_2 = []
sepet_3 = []
sepetler = sepet_1, sepet_2, sepet_3

while True:
    k = int(input("Sepetlere kaç adet sayı ekleme çıkarma işlemi yapmak istiyorsunuz: \n >>> "))
    while k > 0:
        islem = random.choice([1, 0])
        adet = random.choice([1, 2, 3])
        sepet_secim = random.choice([1, 2, 3])
        print(f"işlem {islem} / adet {adet}, sepet {sepet_secim}")
        if islem == 1:
            for z in range(adet):
                if sepet_secim == 1:
                    sepet_1.append(1)
                elif sepet_secim == 2:
                    sepet_2.append(1)
                elif sepet_secim == 3:
                    sepet_3.append(1)
        elif islem == 0:
            for z in range(adet):
                if sepet_secim == 1:
                    sayac_1 = 0
                    while sayac_1 > adet:
                        if len(sepet_1) > 0:
                            sepet_2.pop()
                        sayac_1 += 1
                elif sepet_secim == 2:
                    sayac_2 = 0
                    while sayac_2 > adet:
                        if len(sepet_1) > 0:
                            sepet_2.pop()
                        sayac_2 += 1
                elif sepet_secim == 3:
                    sayac_3 = 0
                    while sayac_3 > adet:
                        if len(sepet_1) > 0:
                            sepet_2.pop()
                        sayac_3 += 1
        k -= 1
    print(sepetler)
