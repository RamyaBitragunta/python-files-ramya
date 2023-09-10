#HOW TO SWAP  TWO NUMBERS
#Method-1 - using a temporary variable, temp
num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
print("value of num1 before swapping:",num1)
print("value of num2 before swapping:",num2)
temp = num1
num1 = num2
num2 = temp
print("value of num1 after swapping:",num1)
print("value of num2 after swapping:",num2)

#METHOD-2 - without using temp variable
num_1 = int(input("Enter your first number:"))
num_2= int(input("Enter your second number:"))
print("value of num_1 before swapping:",num_1)
print("value of num_2 before swapping:",num_2)
num_1,num_2 = num_2,num_1
print("value of num_1 after swapping:",num_1)
print("value of num_2 after swapping:",num_2)
