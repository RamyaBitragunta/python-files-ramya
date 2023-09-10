#HOW TO SEARCH AN ELEMENT IN A LIST
#using loop- statement
my_lis = [4,7,8,3,2,1]
ele = 4
flag = 0
for i in my_lis:
    if(i==ele):
        print("element found in the list")
        flag=1
        break
if(flag==0):
    print("element not present in the list")

#if we dont take flag variable which initially is zero, as soon as we found the element
#flag value becomes one and if we could not found any elemnt still the flag value remains zero.
#if ele = 9, then flag value becomes zero and it prints element not present in the list.

#another method- using in operator
my_li = [4,6,7,8,3,2,1]
ele_m = 8
if(ele_m in my_li):
    print("Element found")
else:
    print("Element not found")




