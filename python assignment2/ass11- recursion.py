# HOW CAN U FIND THE FACTORIAL OF THE NUMBER USING RECURSION

# Recursion is a concept where a functtion can call itself any number of times till a certain condition is met
# The condition is important to avoid infinite number of loops
# what is 2 factorial= its 2*1 i.e., 2* 2-1
# then what is 3 factorial = 3*2*1
# then x factorial is x * x-1 * x-2.......

# here a is an attribute
def factorial(a):
    if a==1:
        return 1
    else:
        return (a * factorial(a-1))

input_number = 5
print("The factorial of", input_number, "is", factorial(input_number))

