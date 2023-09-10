
#suppose take an example A is an abstract class and it has two methods m1 and m2
""" Now B is an extended class of A i.e sub class of A
Now in child class i.e. B we have implemented only one method i.e., m1
so can we create an object for B class or not?
As per python.. whenever we create a class we must do implementation for all the methods.then only we can create
an object for the child class and then we can access those methods.
As we implemented only one method in B i.e., m1 (still m2 is left) so B is considered as an abstract class...
and we cannot create an object for this
suppose if we want to create an object- we have to create one more class extended from B eg ., C
and in C class we can implement m2 method.
Finally m1 and m2 are implemented ..and then we can create an object for class C.
"""

from abc import ABC,abstractmethod

class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class Y(X):

    def m1(self):
        print("This is m1")

class Z(Y):

    def m2(self):
        print("This is m2")

obj1 = Z()
obj1.m1()
obj1.m2()

# if we have multple abstarct methods in the abtsract class we can implement them in multiple classes
