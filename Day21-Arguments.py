# def average(a,b):
#     print('The average of the numbers are',(a+b)/2)

# average(19,27)    

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("ANANTH",'JEETH')
name("Ananth","Jeeth","Vuppala")

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print('Average is: ',sum/len(numbers))

average(30,30,30,29)


def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print('Average is: ',sum/len(numbers))
    return sum/len(numbers)


c=average(2,3,4,5)
print(c)