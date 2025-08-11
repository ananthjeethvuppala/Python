# These are special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.
# Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.

class Employee:
    def __init__(self, name):
        self.name= name
    # The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already

    def __len__(self):
        i=0
        for item in self.name:
            i=i+1
        return i
        # The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
    
    def __str__(self):
        return f"My name is {self.name}"
        # The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.
    def __repr__(self):
        return f"Hey Hi I am {self.name}"

    def __call__(self):
        print("Now Fuck Off")
        # The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.