import math


class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getDistance(self,p):
        dx = self.x - p.getX()
        dy = self.y - p.getY()
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance
point1 = MyPoint(3, 4)
point2 = MyPoint(6, 8)
print("p1("+str(point1.getX())+","+str(point1.getY())+")")
print("p1("+str(point2.getX())+","+str(point2.getY())+")")
print("Distance:", point1.getDistance(point2))