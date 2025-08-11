

# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic
fruits = ['apple', 'banana', 'mango','pineapple','kiwi','banana','grapes']
for index,friut in enumerate(fruits):
    print(index, friut)
print('\n')
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)
