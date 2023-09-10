#HOW TO CLEAR A LIST

#using- clear()method
my_lis = [3,6,54,38,23]
print("My list before clear",my_lis)
my_lis.clear()
print("My list after clear",my_lis)

 #initializing the list with no value
my_lis = [3,6,54,38,23]
print("My list before clear",my_lis)
my_lis = []
print(my_lis)

#using operator *=0
my_lis = [3,6,54,38,23]
print("My list before clear",my_lis)
my_lis*=0
print(my_lis)

#using del() method
my_lis = [3,6,54,38,23]
print("My list before clear",my_lis)
del my_lis[:]
print(my_lis)

