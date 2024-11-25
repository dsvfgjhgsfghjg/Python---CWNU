import math


class InvalidRadius(Exception):
    def __init__(self, message="半径不得为负数"):
        self.message = message
        super().__init__(self.message)

class Circle:
    def __init__(self, radius):
        if radius<0:
            self.radius = 0
            raise InvalidRadius
        self.radius = radius
    def CalculateArea(self):
        return self.radius * self.radius*math.pi
def main():
    try:
        inputRadius= float(input('输入半径'))
        circle = Circle(inputRadius)
        print(f"计算得出圆的面积：{circle.CalculateArea()}")
    except InvalidRadius as e:
        print(f"发生错误：{e}")

main()