# CREATE A LAMBDA FUNCTION WHICH WILL PRINT THE SUM OF ELEMENTS IN THE LIST


# library called function tools or functools from where we are trying to import- lambda function logic
from functools import reduce
my_lis = [5,8,10,20,50,100]
sum = reduce(lambda x,y:x+y, my_lis)
print(sum)
