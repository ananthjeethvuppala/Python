# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def sound(self):
        print("Sound made by the animal")

class Dog:
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
        
    def sound(self):
        print("Bark!")

class Cat:
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Cat")
        self.breed =breed
        
    def sound(self):
        print("Meow!")

d=Dog("Snowpee","Pug")  
d.sound()

a=Animal("Dog","Dog")
a.sound()

c=Cat("Niko","Neko")
c.sound()

e=Animal("Neko","Cat")
e.sound()