# Product sınıfını yazın. Fiyat ve stok bilgilerini içeren özellikler ekleyin. Ürünü satın alan bir metod yazın.

class Product:
    def __init__(self, item, cost, stock):
        self.item = item
        self.cost = cost
        self.stock = stock

    def add_stock(self, amount):
        self.stock += amount

    def buy(self, amount):
        if self.stock >= amount:
            self.stock -= amount
        else:
            print(f"Stock is not enough! Stock: {self.stock}")

    def showFeatures(self):
        features = f"""
        Item: {self.item}
        Cost: {self.cost}
        Stock: {self.stock}
"""
        return features


keyboard = Product("Keyboard", 2850, 3)
print(keyboard.showFeatures())
keyboard.add_stock(4)
print("Stock Amount: ", keyboard.stock)
keyboard.buy(5)
print(keyboard.showFeatures())
