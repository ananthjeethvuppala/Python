# Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.

class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class GermanShepard(Dog):
    def __init__(self, name, colour):
        Dog.__init__(self,name, breed="German Shepard")
        self.colour=colour

    def show_details(self):
        Dog.show_details(self)
        print(f"Colour: {self.colour}")

d=GermanShepard("Tuky","Brown")
d.show_details()