# Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        print(f"Area of the shape is {self.x*self.y}")
        return self.x*self.y
        

class circle(Shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)

    def area(self):
        print(f"Area of the circle is {3.14*super().area()}")

    
rec=Shape(3,4)
print(rec.area())

cir=circle(2)
print(cir.area())