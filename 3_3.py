class Shape():
    def area(self):
        print(self.S)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.a=length
        self.b=width
        self.S=self.a*self.b
x=Rectangle(int(input()),int(input()))
x.area()