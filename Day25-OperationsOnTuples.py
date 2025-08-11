tup=(0,1,2,3,45,67,45,67,88,9,45,9)
print(tup)
print('Count of 3 in Tup is: ',tup.count(45))#Returns the index of first occurence of that element
res=tup.index(67)
print('Index of the element 67 in tup is: ',res)
res=tup.index(88,4,10)
print(res)
res=len(tup)
print(res)

