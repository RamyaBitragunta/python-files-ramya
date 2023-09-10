#TO SUM ALL THE NUMBERS IN A LIST - VERY IMP

#using sum() function
my_list = [86,75,42,38,20]
super_lis = sum(my_list)
print(super_lis)

#or
# add_list1 = int(input("Enter your first number:"))
# add_list2 = int(input("Enter your second number:"))
# add_list3 = int(input("Enter your third number:"))
# add_list4 = int(input("Enter your fourth number:"))
# add_list5 = int(input("Enter your fifth number:"))
# final_list = [add_list1+add_list2+add_list3+add_list4+add_list5]
# print(final_list)


#without using a built-in-function
#using for loop

my_list = [86,75,42,38,20]
sum_lis_1= 0
for i in my_list:
    sum_lis_1 = sum_lis_1+i

print("sum of the list is:",sum_lis_1)

#at first we need to take input and after that we need to go through each element of the list and add them
#so in the program we took a variable i.e sum_lis_1 and initially took the value zero
#so we take the first element of the list and add that element to variable
#so here comes  sum_lis_1 = sum_lis_1+ first element i.e = 0+86= 86
#again we take the second element and add it to the sum_lis_1
#so we need to iterate the elements to sum and finally we have to print them

#or

my_list = [86,75,42,38,20]
total=0

for i in range(0,len(my_list)):
    total=total+my_list[i]

print("sum of the list is:",total)



