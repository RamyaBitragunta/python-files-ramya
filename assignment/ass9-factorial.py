#TO FIND THE FACTORIAL OF A NUMBER
#eg: if num is 5, then factorial of num 5 is 5*4*3*2*1 = 120

#iterative approach- using loop
#Using for loop
factorial = 1
num = 5
if num<0:
    print("Factorail does not exists for negative number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):#here if we keep num it will take upto num-1 so, we add +1 to it
        factorial= factorial * i
    print("The factorial of", num, "is", factorial)

#by using while loop
num = int(input(" please enter your number"))
org= num
fact=1
while num>0:
    fact = fact * num
    num = num-1
print("The factorial of ", org, "is", fact)

#recursion approach- the function calling the same function- multiple times
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) #if n= 5,(5*4*3*2*1)
num= 5
print("Factoral of", num, "is",factorial(num))

#here the same thing we can write in single code -called as terinary operator
#instead of writing multiple statements we can also write in a single statement

def fac_t(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)
num=5
print("Factoral of", num, "is",factorial(num))




