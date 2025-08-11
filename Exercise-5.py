import random

# rock0 paper1 siccsor2


def check(user,comp):
    if (comp==user):
        return 0
    elif(comp==0 and user==2):
        return -1
    elif(comp==1 and user==0):
        return -1
    elif(comp==2 and user==1):
        return -1
    else:
        return 1

print("ROCK - 0\nPAPER - 1\nSCISSOR - 2\n")  
user=int(input("Enter your choice: "))
comp=random.randint(0,2)
print("User - ",user)
print("Computer - ",comp)

fuck=check(user,comp)
if (fuck==0):
    print("It's a DRAW")
elif (fuck==-1):
    print("You have lost Mother Fucker")
else:
    print("Well done you dumb fuck")