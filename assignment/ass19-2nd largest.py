#HOW TO FIND SECOND LARGEST NUMBER IN A LIST

#using sort or sorted method
my_lis = [24,56,78,90,94,38]
sort_lis = (sorted(my_lis))
print(sort_lis[-2])


#using loops
my_lis = [24,56,78,90,94,38]
def find_sec_max(my_lis):
    first_max = max(my_lis[0],my_lis[1])
    sec_max = min(my_lis[0],my_lis[1])
    for i in range(2,len(my_lis)):#here 2 is the 3rd element in the list
        if my_lis[1] > first_max:
            sec_max = first_max
            first_max = my_lis[1]
        elif my_lis[1] > sec_max:
            sec_max = my_lis[1]
    return sec_max

print('second maximum number is:',find_sec_max(my_lis))

#if the list has any duplicate numbers then we have change program code-
my_lis = [24,56,78,90,94,38,90]
def find_sec_max(my_lis):
    first_max = max(my_lis[0],my_lis[1])
    sec_max = min(my_lis[0],my_lis[1])
    for i in range(2,len(my_lis)):#here 2 is the 3rd element in the list
        if my_lis[1] > first_max:
            sec_max = first_max
            first_max = my_lis[1]
        elif my_lis[1] > sec_max and first_max!=my_lis[i]:
            sec_max = my_lis[1]
    return sec_max

print('second maximum number is:',find_sec_max(my_lis))







