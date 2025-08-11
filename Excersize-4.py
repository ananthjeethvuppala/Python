import random
import string
st=input('Enter your string: ')
words=st.split(" ")
coding=int(input("01.Codeing 02.Decodeing : "))
coding = True if(coding==1) else False
print(coding)

if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1= ''.join(random.choices(string.ascii_letters,k=3))
            r2= ''.join(random.choices(string.ascii_letters,k=3))
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


