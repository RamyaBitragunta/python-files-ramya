#to check  a number is a prime number or not -VER VERY IMP
# prime number should be greater than 1
#it should have only two factors 1 and itself

num = int(input("Enter your number:"))
count = 0
if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count = count+1
    if count==2:
        print("number is a prime number")
    else:
        print('number is not a prime number')


#here if the count is greater than 2 , i.e if number is having more than 2 factors and then
#it is not considered as a prime number






