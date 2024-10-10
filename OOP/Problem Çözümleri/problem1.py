# Bir Car sınıfı oluşturun. Bu sınıfta brand, model, year özellikleri ve start(), stop() metodları olsun.
# brand -> Marka

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.isRunning = False

    def showFeatures(self):
        features = f"****** CAR FEATURES ****** \n\nBrand: {self.brand} \nModel: {self.model} \nYear: {self.year} \nSituation: {self.isRunningn}\n"
        return features

    def start(self):
        if self.isRunning:
            print("? The car is already running")
        else:
            self.isRunning = True
            print("? The car was stopped.")

    def stop(self):
        if self.isRunning:
            self.isRunning = False
            print("? The car was started.")
        else:
            print("? The car is already stopping")



mercedes = Car("Mercedes", "i53", 2024)

print(mercedes.showFeatures())
mercedes.stop()
mercedes.start()
print(mercedes.showFeatures())


