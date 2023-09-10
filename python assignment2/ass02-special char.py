#TO CHECK IF A STRING CONTAINS ANY SPECIAL CHARACTER
#speecial characters - @,*, %,!.^....
#at first we have to import regular expression module  from python
#re is a built-in package in python
#and we will create a variable called regX
#and from re package we have to call a method called compile (pre-defined method)
#and we need to check that if all special characters are present in the string or not
#search - method to check


import re
my_str = "welc**^*ometopyth@nwor!d$"
regX = re.compile('[!@$%^&*()<>?/|~`:}{]')
if(regX.search(my_str)== None):
    print("No special characters present in the string")
else:
    print("special characters found in a string")



import re
str_i = "welcome to python programming"
regX = re.compile('[!@$%^&*()<>?/|~`:}{]')
if(regX.search(str_i)== None):
    print("No special characters present in the string")
else:
    print("special characters found in a string")



