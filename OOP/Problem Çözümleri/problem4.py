# Circle sınıfını yazın. Yarıçapı alın ve get_area() metodu ile dairenin alanını hesaplayın.
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius**2)


circle1 = Circle(3)
print(circle1.get_area())