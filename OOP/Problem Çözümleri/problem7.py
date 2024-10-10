# Bir Person sınıfı oluşturun. Bu sınıfta kişinin adını ve yaşını tanımlayın. Yaşını artıran bir metod yazın.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age_increase(self, amount=1):
        self.age += amount

    def showFeatures(self):
        features = f"""
        Name: {self.name}
        Age: {self.age}
        """
        return features


Serhat = Person("Serhat", 19)
print(Serhat.showFeatures())
Serhat.age_increase()
print(Serhat.showFeatures())
Serhat.age_increase(20)
print(Serhat.showFeatures())
