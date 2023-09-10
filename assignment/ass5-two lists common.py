#WRITE A PYTHON PROGRAM THAT TAKES TWO LISTS AND RETURNS-TRUE IF THEY HAVE AT LEAST ONE COMMON MEMBER

# my_list1= [6,7,4,3,8]
# my_list2= [4,2,3,10,1]
def com_mon(my_list1,my_list2):
    result = False
    for x in my_list1:
        for y in my_list2:
            if x==y:
                result = True
                return(result)

print(com_mon([6,7,4,3,8],[4,2,3,10,1]))
print(com_mon([5,6,7],[8,9,2]))

#or we can simply write

my_list1= [6,7,4,3,8]
my_list2= [4,2,3,10,1]
for x in my_list1:
    for y in my_list2:
        if x == y:
            result = True
print(result)

#using the methods in python
lis_1= [1,2,3,4,5]
lis_2= [6,7,8]
set1= set(lis_1)
set2= set(lis_2)
set3= set1.intersection(set2)
if(len(set3)==0):
    print("lists do not have any common elements)
else:
    print("lists have common elements)

#we have converted our lists to sets by using set method
#now we have to check the length of set3 , its intersection equals to zero or not
#the concept of checking length 0 or not is to check if the set3 has any elements or not
#if set3 does not have any common elements that means those lists are not having common elements
