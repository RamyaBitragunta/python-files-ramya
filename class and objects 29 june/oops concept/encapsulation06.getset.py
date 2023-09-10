
# USING GETTER AND SETTER METHODS WITH PRIVATE VARIABLES IN PYTHON

""" Instance methods are of two types
setter method- set values of instance variables (to change value of instanc variable from old to new )
setter method is also called as mutator method
getter method- get values of instance variables (fetches the values(to get the values))
getter method is also called as accessor method
"""

# class A:
#     __age = 0 # now if we try to access this variable ouside the class we get an error
#
# v1 = A()         #object creation
# print(v1.__age) #using object reference we r trying to access particular variable
# we get error. bcz it is a private variable(as it can be accessed only inside the class)
# then how to access those private variable outside the class
# for this we have to create non-private getter and setter methods.
""" the purpose of these methods is to get that is return and set that is assign private instance 
variables of a class.
The restricted access to private members allows the methods to control what values are assigned.
This is one of the fundamental concept of the information hiding"""

class B:
    __age = 0
    def set_age(self,age):
        B.__age = age  #accessing the particular variable with class
    def get_age(self):
        return B.__age

obj = B()
obj.set_age(14)
print(obj.get_age())


