# Point sınıfı oluşturun. İki nokta arasındaki mesafeyi hesaplayan metod yazın.

class Point:
    def __init__(self, primary_point_x, primary_point_y, secondary_point_x, secondary_point_y):
        self.primary_point_x = primary_point_x
        self.primary_point_y = primary_point_y
        self.secondary_point_x = secondary_point_x
        self.secondary_point_y = secondary_point_y


    def distance(self):
        distance = ((self.primary_point_x - self.secondary_point_x) ** 2 + (self.primary_point_y - self.secondary_point_y) ** 2) ** 0.5
        return distance

point1 = Point(0, 4, 3, 9)
print(point1.distance())