# s1={'Hyderabad',"Tokyo", "Madrid", "Berlin", "Delhi"}
# s2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# s3=s1.union(s2)
# print(s3)#The union() method returns a new set
# s1.update(s2)
# print('s1 is:',s1,'s2 is:',s2)#update() method adds item into the existing set from another set.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)# The intersection() method returns a new set
# cities.intersection_update(cities2)
# print(cities)#intersection_update() method updates into the existing set from another set.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)#The symmetric_difference() method returns a new set
# cities.symmetric_difference_update(cities2)
# print(cities)#symmetric_difference_update() method updates into the existing set from another set.

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)
# print(cities.difference(cities2))


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)