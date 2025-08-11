def calculateGmean(a,b):
    mean=((a*b)/(a+b))
    print("The Geometric mean is: ",mean)

def isGreater(a,b):
    if(a>b):
        print('First Number is Greater')
    elif(b>a):
        print('Secound Number is Greater')
    else:
        print('Both are same')    


a=int(input('Enter first Number: '))
b=int(input('Enter the other number: '))
isGreater(a,b)
calculateGmean(a,b)

c=8
d=7
isGreater(c,d)
calculateGmean(c,d)