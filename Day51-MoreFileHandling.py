# Writing to the file
with open('filepy.txt', 'w') as f:
    f.write("0123456789Ananth")

# Reading from the file
with open('filepy.txt', 'r') as g:
    g.seek(10)  # Move cursor to position 10
    print(type(g))  # Print the type of file object
    print(g.tell())
    data = g.read(6)  # Read 6 characters from position 10
    print(data)  # Output: "Ananth"
    print(g.tell())


with open('filepy.txt','a') as h:
    h.write(" Hello World!!!")
    h.truncate(6)

with open('filepy.txt','r') as i:
    print(i.read())
