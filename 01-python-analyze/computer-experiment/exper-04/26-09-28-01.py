class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def __str__(self):
        return f"矩形(长={self.length}, 宽={self.width}, 面积={self.area()}, 周长={self.perimeter()})"

if __name__ == '__main__':
    rectangle = Rectangle(5, 3)
    print(rectangle)