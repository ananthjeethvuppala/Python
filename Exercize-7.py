import os

# os.rename("clutteredFolder/file.txt","clutteredFolder/OnePiece.txt")
files=os.listdir("clutteredFolder")
i=1
for file in files:
    print(file)
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}","clutteredFolder/{i}.png")
        i +=1