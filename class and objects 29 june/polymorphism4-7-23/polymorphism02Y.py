
""" Polymorphism in python refers to the ability of a variable, function, or object to
take on multiple forms.
In a programming language exhibiting polymorphism, class objects belonging to the same hierarchial tree
(inherited from a common parent class) may have functions with same name, but different behaviors."""

# polymorphism- different ways
# 1. Method overriding and 2. Method overloading


# method overloading -  we use the same function but different parameters
# eg:- add(2,3)
#      add(2,3,4),    add(2,3,4,5)

def add(a,b,c=0,d=0,e=0):
    ans = a+b+c+d+e
    print("Answer:",ans)

add(2,3)
add(2,3,4)
add(2,3,4,5)
add(2,3,4,5,6)

# here there are 5 parameters,bt for c,d and e - we have given parameter default values= zero
# by using default parameters,we have given different no of parameters.

l = [1,2,3,4,5]
s = "Hello world"
print(len(l))
print(len(s))
# here we have used the same function bt it handled different data types, its bcz of polymorphism


