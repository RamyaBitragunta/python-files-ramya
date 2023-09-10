#TO CHECK IF THE NUMBER IS PALINDROME
#Palindrome - is the number that remains the same when its digits are

#using string slicing method
my_str = int(input("enter your number:"))
rev_e = int(str(my_str)[::-1])
if my_str== rev_e:
    print("its a palindrome number")
else:
    print("its not a palindrome")

#or we can use another method- using while loop

#suppose lets take no.121
n = int(input("please, enter your number:"))
temp = n
rev  = 0
while(temp>0):
    remainder = temp%10
    rev = (rev*10)+remainder
    temp= temp//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("No, its not a palindrome")