# Bir Student sınıfı oluşturun ve öğrencilerin adını, yaşını ve notlarını tutun.
# get_average() metodu ile öğrencinin not ortalamasını hesaplayın.

class Student:
    def __init__(self, name, age, *points):
        self.name = name
        self.age = age
        self.points = points

    def showFeatures(self):
        features = f"""
        Name: {self.name}
        Age: {self.age}
        Points: {self.points}
        Average: {self.get_average()}
        """
        return features

    def get_average(self):
        return sum(self.points)/self.points.__len__()


Serhat = Student("Serhat", 19, 75, 95, 100)
print(Serhat.showFeatures())
print(Serhat.get_average())

