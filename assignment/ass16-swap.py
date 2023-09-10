#HOW TO SWAP FIRST AND LAST ELEMENTS OF THE LIST


# by using temporary variable
my_lis = [24, 56, 73, 39,40]
size = len(my_lis)
temp = my_lis[0]
my_lis[0] = my_lis[-1]
my_lis[-1] = temp
print("List after swapping:",my_lis)

#not using temp variable
my_lis = [24, 56, 73, 39,40]
my_lis[0],my_lis[-1]= my_lis[-1],my_lis[0]
print(my_lis)
