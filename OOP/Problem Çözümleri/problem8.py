# Bir Employee sınıfı oluşturun. Maaşını ve pozisyonunu tutan metodlar tanımlayın.

class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def makeraise(self, amount):
        self.salary += amount

    def showFeatures(self):
        features = f"""
        Position: {self.position}
        Salary: {self.salary}
"""
        return features


computer_engineer = Employee("Bilgisayar Mühendisi", 53000)
print(computer_engineer.showFeatures())
computer_engineer.makeraise(-5000)
print(computer_engineer.showFeatures())