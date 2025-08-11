num=input('Enter the Number: ')
print(f"The Multiplication Table of {num} is : ")
try:
    for i in range(1,11):
        print(f"{int(num)} x {i} = {int(num)*i}")
except Exception as e:
    print(e)
    


num=input('Enter the Number: ')
print(f"The Multiplication Table of {num} is : ")
try:
    for i in range(1,11):
        print(f"{int(num)} x {i} = {int(num)*i}")
except:
    print("Invalid Input!")



try:
    num=int(input("Enter an Integer: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print('Number entered is not an Integer')

except IndexError:
    print('Index Error')


print("End of CODE!")

