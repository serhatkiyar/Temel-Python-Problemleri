class Araba:

    def __init__(self, model="Bilgi yok", renk="Bilgi yok", hiz="Bilgi yok"):

        print("İnit fnksiyonu")
        self.model = model
        self.renk = renk
        self.hiz = hiz

    def araba_hizi(self):
        return self.hiz


model1 = input("Model: ")
renk1 = input("Renk: ")
hiz1 = input("Hız: ")

araba1 = Araba(model1, renk1, hiz1)

print(araba1.model, araba1.renk, araba1.hiz)
print(Araba.araba_hizi(araba1))
