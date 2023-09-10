
""" Abstraction is one of the most important features of object oriented programming.
It is used to hide the background details or any unnecessary implementation.
Abstraction keeps the all unnecessary information hidden from the users.
It hides the implementation details from the user,and only highlighted set of services is provided to the user.

Any class that contains abstractmethod is called Abstract class.
abc - module or the library from ABC-Abstract Base class is imported

What is abstract class and why do we need it?
Basically a method is nothing but function so how can we create a method?
so the method has its name and parameters/ arguments and also have body
if we want to not mention anything in body or if we want to keep it blank then we declare the method.
declare- means dont have anything in the body - simply we can say pass
def name_method():
    pass

So these methods which have only declaration but not have any definition - are called abstract methods.
And the class which have these abstract methods are called abstract class .

But python by default could not support abstract classes. for support we need to import a module -abc
from this we need to import ABC and also abstractmethod.
if we write @abstractmethod- it is a decorator ..so by using decorator- we can say that this
method is abstract method to compiler.
so when u inherit an abstract class as a parent to the child class,the child class should define all
the abstract class present in the parent class.
if it is not done then the child class also becomes the abstract class automatically.
"""