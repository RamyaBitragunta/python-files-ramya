#what is map() function in python?

#the map() function inpython is used for applying a function on all elements of a specified iterable
#it consists of two paramters, function and iterable.


def mul_func(n):
    return n*3

num = [1, 2, 3, 4, 5, 6]
result = map(mul_func,num)

print(list(result))