def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return (num*factorial(num-1)) 

a=int(input("Enter the Number: "))
print('The Number is: ',a)
print('Factorial: ',factorial(a))


def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return (fibonacci(num-1)+fibonacci(num-2))

a=int(input('Enter the Number: '))
print('The Number is: ',a)
b=fibonacci(a)
print('Fibonacci: ',b)