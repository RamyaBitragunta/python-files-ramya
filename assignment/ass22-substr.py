# HOW TO FIND SUBSTRING PRESENT IN THE STRING

my_str = "Welcome to  python programming"
sub_str = "python"
print(my_str.find(sub_str))
if (my_str.find(sub_str))==-1:
    print("not found")
else:
    print("found")

#find() method finds the first occurance of the specified value
#The find() method returns the -1 if the value is not found
#print(my_str.find(sub_str))- it just gives the position where exactly the string is starting
#if the substring is not present in the main string then ->print(my_str.find(sub_str)) this returns -1
#if it returning any number other than -1 then based on this - we can write simple conditional statement

my_str = "Welcome to  python programming"
sub_str = 'is'
print(my_str.find(sub_str))
if (my_str.find(sub_str))==-1:
    print("not found")
else:
    print("found")
