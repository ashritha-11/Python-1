#Abstarction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of rectangle is:",self.length*self.breadth)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=3.14
        print("Area of circle is:",pi*self.radius*self.radius)
a=Rectangle(10,20)
b=Circle(8)
a.area()
b.area()
        

