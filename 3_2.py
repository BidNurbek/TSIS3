class Shape():
    def area(self):
        print(self.S)
    
class Square(Shape):
     def __init__(self, length):
         self.a=length
         self.S=self.a*self.a
x =Square(int(input()))
x.area()