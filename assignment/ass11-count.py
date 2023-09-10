#NUMBERS IN A LIST WITHIN A GIVEN RANGE


for i in range(0,20):
    print(i)

#HOW TO COUNT OCCURANCES OF AN ELEMENT IN A LIST
#for eg:
# li_s= [15,6,10,3,2,10,78,23,44,10]
# x=10; output=3 i.e 10 appers 3 times in a list


#method-1- by using loop method
my_lis= [15,23,6,10,3,2,10,78,23,44,10]
x=10
count=0  #lets take count=0 initially, ele = element
for ele in my_lis:
    if(ele==x):
        count= count+1
print("{} has occured {} times".format(x,count))

#just printing the output in format- i.e. formatted output, here 1st{}-curly braces returns the x value and 2nd one
#returns  the count value.


#method-2 - count method
y_lis= [15,15,23,6,10,3,2,10,78,23,44,10]
x= 15
print("{} has occured {} times".format(x,y_lis.count(x)))
#here x is the element i.e 15 and count method will find how many times x is repeated inside the lst


#method-3- counter method- using Counter()
from collections import Counter
li_s= [15,78,23,6,10,3,2,10,78,23,44,10]
x=78
dic = Counter(li_s)  #{  }
print("{} has occured {} times".format(x,dic[x]))

#counter method is presrent inside the collections package
#this will basically returns a dictionary variable, so dic is a variable name
# and dictionary contains key and value
#every element  and how many times  it was repeated
#{15:1, 78:2, 23:2, 6:1...} here 15 is a key and 1 is the value ...





