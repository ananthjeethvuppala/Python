# MAP
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. 

def cube(x):
    return x*x*x

listt=[1,3,4,5,2,8]
newlist=[]
for item in listt:
    newlist.append(cube(item))

print(newlist)

newlist1=map(cube,listt)# Returns Map object
print(newlist1)
newlist1=list(map(cube,listt))
print(newlist1)
newlist1=list(map(lambda x:x*x*x,listt))
print(newlist1)


# FILTER
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. 

def filt_func(a):
    return a>=2

newlist2=filter(filt_func,listt)
print(newlist2)
newlist2=list(filter(filt_func,listt))
print(newlist2)
newlist2=list(filter(lambda a:a>=2,listt))
print(newlist2)

# REDUCE
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python
from functools import reduce

def sum(a,b):
    return a+b

newlist3=reduce(sum,listt)
print(newlist3)
newlist3=reduce(lambda a,b:a+b,listt)
print(newlist3)