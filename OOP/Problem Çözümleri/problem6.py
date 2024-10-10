# Bir Book sınıfı oluşturun ve title, author, price özelliklerini tanımlayın.

class Book:
    def __init__(self, title, author, price, number_of_pages):
        self.title = title
        self.author = author
        self.price = price
        self.number_of_pages = number_of_pages

    def showFeatures(self):
        features = f"""
        Title: {self.title}
        Author: {self.author}
        Price: {self.price}
        Number Of Pages: {self.number_of_pages}
        """
        return features


sefiller = Book("Sefiller", "Victor Hugo", 300, 1724)
print(sefiller.showFeatures())

