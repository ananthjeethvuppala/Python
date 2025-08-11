info = {'name':'Karan', 'age':19, 'eligible':True, 'Ananth':'22311a0411'}
print(info)
print(info['name'])
print(info.get('eligible'))

print(info.values())
print(info.keys())
print(info.items())

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")