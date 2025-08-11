a=123
b=1234
print(a) if a>b else print('=') if a==b else print(b)

# result = value_if_true if condition else value_if_false
# This syntax is equivalent to the following if-else statement:
# if condition:
#     result = value_if_true
# else:
#     result = value_if_false
#  it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic.