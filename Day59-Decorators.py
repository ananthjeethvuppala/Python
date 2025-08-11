def greet(fx):
    def func(*args,**kwargs):
        print("Good Morning!")
        fx(*args,**kwargs)
        print("Thank You!!")
    return func


import logging

def log_func(fx):
    def dec(*args,**kwargs):
        logging.info(f"Calling {fx.__name__} with args={args}, kwargs={kwargs}")
        result=fx(*args,**kwargs)
        logging.info(f"{fx.__name__} returned {result}")
        return result
    return dec


@greet
def hello():
    print("Hello World!!!")

@greet
def add(a,b):
    print(a+b)

@log_func
def sub(a,b):
    print(a-b)

hello()
add(3,4)
sub(4,3)



# Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

# In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.