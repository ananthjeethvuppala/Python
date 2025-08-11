# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    def __add__(self,fuck):
        return Vector(self.x+fuck.x,self.y+fuck.y,self.z+fuck.z)
    
    def __sub__(self,fuck):
        return f"{self.x-fuck.x}i - {self.y-fuck.y}j - {self.z-fuck.z}k"


v1=Vector(1,3,6)
print(v1)
v2 = Vector(3,5,8)
print(v2)
print(v1+v2)
print(v1-v2)
print(type(v1+v2))
print(type(v1-v2))