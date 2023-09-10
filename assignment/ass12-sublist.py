#TO CHECK FOR A SUBLIST IN A LIST

my_list = [5,8,9,4,23,16,56,34,68]
my_list2 = [5,9,4,23,34,68]
if my_list2 in my_list:
    print("True")
else:
    print("False")


#To check wheather a lsit contains a sublist
y_lis= ['a','x',[1,3,4,5,'ramya']]
for i in y_lis:
    if len(i)>0:
        print("sublist is present in list")
        break
else:
    print("sublist is not present in the list")
