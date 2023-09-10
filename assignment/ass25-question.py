# ASK THE USER TO ENTER TWO NUMBER (int) a and b, RETURN True if
#a) either one is 6
#b) or if their sum is 6
#c) or the difference is 6

a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
if (a or b)==6:
    print(True)
elif (a+b)==6:
    print(True)
elif (a-b)==6:
    print(True)
else:
    print(False)

#or simply we can write

a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
if (a or b)==6 or (a+b)==6 or (a-b)==6:
    print(True)
else:
    print(False)

