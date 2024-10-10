# Bir BankAccount sınıfı oluşturun. Bu sınıf para yatırma ve çekme işlemleri için metodlar içersin.

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def withdrawMoney(self, amount):
        self.balance += amount

    def depositMoney(self, amount):
        self.balance -= amount

    def accountFeatures(self):
        features = f"""
        Name: {self.name}
        Balance: {self.balance}
        """
        return features

serhat = BankAccount("Serhat")
print(serhat.accountFeatures())
serhat.withdrawMoney(54000)
serhat.depositMoney(3000)
print(serhat.accountFeatures())
