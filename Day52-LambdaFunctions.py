mult=lambda x,y:x*y # lambda function is a small anonymous function without a name.
print(mult(2,3))

sq=lambda x:x*x
def cube(fx,value):
    return value*fx(value)

print(cube(sq,2))
print(cube(lambda x:x*x,2))

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.