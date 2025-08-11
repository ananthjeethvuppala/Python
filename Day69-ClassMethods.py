class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)


# To define a class method, you simply use the "@classmethod" decorator before the method definition. The first argument of the method should always be "cls," which represents the class itself. Here is an example of how to define a class method:
# class ExampleClass:
#     @classmethod
#     def factory_method(cls, argument1, argument2):
#         return cls(argument1, argument2)
# In this example, the "factory_method" is a class method that takes two arguments, "argument1" and "argument2." It creates a new instance of the class "ExampleClass" using the "cls" keyword, and returns the new instance to the caller.

# It's important to note that class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.

# Python class methods are a powerful tool for defining functions that operate on the class as a whole, rather than on a specific instance of the class.