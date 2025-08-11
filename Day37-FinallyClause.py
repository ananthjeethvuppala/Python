# We use finally in fuctions it is not required in the code
# finally is always executed
try:
    l=[1,5,7,4,8]
    i=int(input('Enter the index: '))
    print(l[i])
except:
    print("Some error occured")
finally:
    print('I am always Excecuted')

print('I am same as Finally')


def func1():
    try:
        l=[1,5,7,4,8]
        i=int(input('Enter the index: '))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print('I am always Excecuted')
    

x=func1()
print(x)