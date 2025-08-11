lists=[20,45,'Ananth','VUPPALA',True,64,86]
print(lists)
print(type(lists))
print(lists[0])
print(lists[1])
print(lists[2])
print(lists[3])
print(lists[4])
print(lists[5])


print(lists[-3])# Negative Index
print(lists[len(lists)-3])# Positive Index
print(lists[6-2])# Positive Index
print(lists[4])# Positive Index

if "6" in lists:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "Ha" in "Harry":
  print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)