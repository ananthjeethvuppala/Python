# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self, name, dance):
        self.dance=dance
        self.name=name

o=DancerEmployee("Vishnu","Jumba")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())