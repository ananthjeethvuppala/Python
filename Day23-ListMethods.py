l=[2,4,6,5,8,32,1,1]
print(l)
# l.append(74)
l.sort(reverse=True)
l.reverse()
print(l.index(32))#Returns index of that element
print(l.count(4))
m=l
m[0]=0 #m becomes l and changes in m will turn to change in l
m=l.copy()
m[0]=0
print(m)
l.insert(1,899)
m=[900,1000,1100]
# l.extend(m)# Or can use the following method
k=l+m
print(k)
