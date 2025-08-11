class Employee:
    def __init__(self,name,id):
        self.name= name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.name} and ID no is {self.id}")

class programmer(Employee):
    def showLanguage(self):
        print("The default language is python")

e1=Employee("Matt Murdock",4118)
e1.showDetails()
e2=Employee("Peter Parker",208)
e2.showDetails()
e3=programmer("Ananth",411)
e3.showDetails()
e3.showLanguage()



# Inheritance in python
# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

# Types of inheritance:
# 01.Single inheritance
# 02.Multiple inheritance
# 03.Multilevel inheritance
# 04.Hierarchical Inheritance
# 05.Hybrid Inheritance