# OPENING A FILE
# Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending
# f=open('filepython.txt','r')



# MODES IN FILE
# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if the file already exists.

# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc)


# contents=f.read() # Reading
# print(contents)

# WRITING A FILE
f=open('filepython.txt','w')
f.write('Puka, Konda erripuka') # Keep in mind that writing to a file will overwrite its contents.
f.close()
# If you want to append to a file instead of overwriting it, you can open it in append mode.
f=open('filepython.txt','a')
f.write(' Chi Dengey')
f.close()# It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.


# Alternatively, you can use the with statement to automatically close the file after you are done with it.
with open('filepython.txt', 'a') as f:
    f.write("\nHey I am inside in the text file using with statement")


    