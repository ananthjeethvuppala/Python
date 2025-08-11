f=open('filepu.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    # print('line')
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of stundent {i} is in x1 subject is {m1}")
    print(f"Marks of stundent {i} is in x1 subject is {m2}")
    print(f"Marks of stundent {i} is in x1 subject is {m3}")


g=open('filepu1.txt','w')
uu=['wjc\n','jenci\n','hcbhc\n']
g.writelines(uu)# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
g.close()


# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:
h=open('filepu2.txt','w')
pp=['hello','hi','hey']
for p in pp:
    h.write(p+'\n')
h.close()    