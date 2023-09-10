
""" So if we want to know how to write the data - we have too use w to write something
if we dont find any file naming abc bt we have mentioned in the method, then it wil create a file fr us
 and if we run the code.. we can see a new file abc and if we open this file we get a file in text format
  and its a new file and we dont have data in it """

f1 = open('abc','w')
# we can print data in it by saying
f1.write("Ramya - you are awesome")
f1.write("  You have to be brave")

""" Suppose if we delete line 9 and 10 and again if we write freshly f1.write("dont lose")
we will loose the previous data in file abc... its because we simply said w that is just to write.
so now we have to use append in order to add new data to already existing data"""

f1 = open('abc','a')
f1.write(' Dont loose your hope')