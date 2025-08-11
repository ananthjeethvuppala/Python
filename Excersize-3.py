questions=[
    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facesrbook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Fsvacebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebfvsrook','Python','Java','c','c++',3],

    ['Which Language is used to create Favsvcebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facesrgvbook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3],

    ['Which Language is used to create Facebook','Python','Java','c','c++',3]


]    

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,5000000,10000000]
money=0
for i in range(0,15):
    question=questions[i]
    print(f"\n\nQuestion of Rs.{levels[i]} is")
    print(question[0])
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")

    reply=int(input('Enter the Optinon Number(1-4) or 0 to Quit: '))
    if (reply==0):
        money=levels[i-1]
        break
    elif (reply==question[-1]):
        print(f"Correct Answer!,You have won Rs.{levels[i]}\-")
        if(i==4):
            money=levels[4]
        elif(i==9):
            money=levels[9]
        elif(i==14):
            money=levels[14]
    else:
        print('Worng Answer!')
        break

print(f"Your won a total of {money}")
    