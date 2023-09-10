
# Python io module allows us to manage the file related input and output operations
# The advantage of using io module is that the classes and functions available allows us to extend the functionality
# to enable writing to the unicode data

# FILE HANDLING IN PYTHON

""" If we want to store the data in a persistent way for longer period.. we need permanent storage
 One of the day is by using a relational database - MYSQL, ORACLE- these provides table structures-
 that's an entire complex stuff
 But what if we want to store something for a longer period but in a simple format- then we have to go for
 text(text file)
 suppose  we have a text file named - and mydata and we have some data in it.
 If we want to use this data(present in mydata) in a code . so how can we use this file in a code ?
 - for this we have inbuilt functions
 so open is a function or method we can use - and we have to pass two basic parameters
 The first one is the file name itself and we need to also mention the mode(reasons/purpose for opening the file-
 it may be read, write,overwrite something in it)
 for reading a file - we use r.
 so for handling that file we have to save that file, so we use any object or reference
 and when we say read -it will print evrything in that file """


f = open('MyData','r')
print(f.read())
f.close()

""" if we dont want to print entire file and if we want to print only one line or first line-
 we have an option- we can click on cntrl and space - we can see readline and many options"""

f = open('MyData','r')
print(f.readline())

# when we say readline it wil print only first line
# what if i want to print second line, its just simpe - we have to copy the code

f = open('MyData','r')
print(f.readline())
print(f.readline())

# so everytime when we print readline- it wil have inbuilt pointer inside it and it wil fetch and print the next line

# if we add end- it mentions we r done with line 1 and line 2 (there wil be no space b/w the lines)

f = open('MyData','r')
print(f.readline(),end='')

# if the file is present in same folder then path of the file is not required but if it is present
# in different folder then path is required

# file = open('../directoryname/file name','r')
# print(file.read())
# file.close()
# or we can copy the path reference
