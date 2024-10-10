# Vehicle sınıfı oluşturun. Car ve Bike sınıfları bu sınıftan türesin.
# Her biri için hız ve yakıt bilgilerini içeren metodlar ekleyin.

from abc import abstractmethod

class Vehicle:
    def __init__(self, wheel_count, color):
        self.wheel_count = wheel_count
        self.color = color

    @abstractmethod
    def run(self):
        pass

class Car(Vehicle):
    def __init__(self, wheel_count, color):
        super().__init__(wheel_count, color)

    def run(self):
        print("The car was started!")


class Bike(Vehicle):
    def __init__(self, wheel_count, color):
        super().__init__(wheel_count, color)

    def run(self):
        print("The bike was started!")





