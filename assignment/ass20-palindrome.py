#HOW TO FIND IF THE STRING IS PALINDROME OR NOT
#if any string after reversing, if we get the same string then we call it as palindrome
#eg: madam- palindrome
#welcome- not a palindrome

my_string = input("Enter a string:")
#for reversing the string we dont have reverse operator so we use slicing operator
print(my_string[ : ])
#if we dont specify anything we will get the string from the begining to the end
#print(my_string[ : :-1])
#this expression will gives the reverse string
#now we have to store the reversed string
rev_string = (my_string[ : :-1])
if rev_string==my_string:
    print("this is a palindrome")
else:
    print("not palindrome")