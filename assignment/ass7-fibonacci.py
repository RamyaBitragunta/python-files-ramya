#WRITE A PROGRAM TO GET THE FIBONACCI SERIES BETWEEN 0 AND 50
#In mathematics - the fibonacci series- is a sequence of integer numbers formed by the addition of preceeding
#two numbers in the series
#eg: 0,1,1,2,3,5,8,13,21,34,55,89,144...
#0 and 1 are the first two numbers of the series
#methods- loop, using recursion, optimized technique
# using loop method

num = int(input('Enter any number:'))
n1,n2 = 0,1 #(n1=0, n2=1)
sum = 0
if num<=0:
    print("please enter the number greater than zero")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1+ n2

#lets declare two variables n1 and n2
#lets declare any variable which is sum, which will store addition value- and lets set it to zero- initially
#now we can add validation to our number
#we have to interchange the variables so the second number considered as 1st value
#and the sum value will be considered as the second number
#so for every iteration n2 value will be stored in n1 and sum value will be stored in n2.
#this process will be repeated until the conditon is satisfied


