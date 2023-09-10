#PROGRAM TO MULTIPLY ALL THE NUMBERS IN A LIST

#traversal method
my_lis = [3,8,9,2,4,6]
result= 1
for i in my_lis:
    result= result*i
print(result)

#if we keep indentation before print then it comes under for loop and it shows each step of multiplication
#that is 3, 3*8=24, 3*8*9=216....... like this
my_lis = [3,8,9,2,4,6]
result= 1
for i in my_lis:
    result= result*i
    print(result)