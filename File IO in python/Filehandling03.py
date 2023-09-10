
# now we have 2 files one is abc and other one is MyData
""" If we want to copy everything from mydata to abc... for that we have to read all the data from Mydata
and then write everything  in abc"""

f = open('MyData','r')


f1 = open('abc','w')

# for data in f:
    # print(data) (this for reading the data of file mydata)

for data in f:
    f1.write(data)

""" Suppose if we have jpg image file, and if we want to copy this file
the image file is made up of binary format.
In files we have two different modes i.e., 1. character mode and other one is binary mode
when u work with the file that file have data with characters or numbers- so according
to that we have to go for either character format or binary format
And if we work with an image we dont have the character format we have just binary format."""

""" For that we have to read that file in binary format"""

# f = open('IMG_6609.JPG','rb') # we r saving this image in Mypic file
# f1 = open('Mypic.JPG','wb')
# for i in f:
#f1.write(i)