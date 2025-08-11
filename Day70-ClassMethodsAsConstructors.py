class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromStr(cls,str):
        return cls(str.split("-")[0],int(str.split('-')[1]))

e1=Employee("Ananth",1200000)
print(e1.name)
print(e1.salary)

String="JBK-1000000"
e2=Employee.fromStr(String)
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,str):
        name,age=str.split(',')
        return cls(name,int(age))

p1=Person("Matt",9000000000)
print(p1.name," ",p1.age)
p2=Person.from_string("murdock,9000000000")
print(p2.name," ",p2.age)