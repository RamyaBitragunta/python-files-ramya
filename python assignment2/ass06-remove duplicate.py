# HOW WILL YOU REMOVE DUPLICATE ELEMENTS FROM A LIST

#there are various methods to remove duplicates from the list
#the easiest way is to convert the list into a set by using set() function and using the list() function
#to covert it back to list if required
#set- is a collection of unique elements and there are no repetative elements in the set.
#set always deletes the duplicate element


my_list = [3,4,6,78,9,9]
my_set  = set(my_list)
print(my_set)

#using- fromkeys
my_lis = [3,4,6,78,9,6]
my_lis = list(dict.fromkeys(my_lis))
print(my_lis)

