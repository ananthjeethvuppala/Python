class person:                #A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword
    name='Ananth Jeeth'
    age=19
    occupation='student'
    surename='Vuppala'
    def info(self):
        print(f'{self.name} is {self.age} years old and is a {self.occupation}') # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

a=person()  # Object is the instance of the class used to access the properties of the class Now lets create an object of the class.
a.name='Rinku'
a.age='18'
a.occupation='Python Developer'
a.info()

b=person()
b.name='NTR'
b.age=38
b.occupation='Actor'
b.info()

c=person()
c.info()
