class student:
    def __init__(self,age,name,caste,study):
        self.age=age
        self.name=name
        self.__caste=caste
        self._study=study

obj=student(21,"Ananth Jeeth","Vyshya","B-Tech")
print(obj.age)
print(obj.name)
# print(obj.__caste) # Cannot be accesed
print(obj._student__caste)# Can be accesed indirectly
print(obj.__dir__())

print(obj._study)
