x=4
print(x)
def my_func():
    global x
    x=2 # this will change the value of the global variable x
    y=8 # Local Variable

my_func()
print(x)
print(y)# this will cause an error because y is a local variable and is not accessible outside of the function
