for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print('In Else Block')
