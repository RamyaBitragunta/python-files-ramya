# NAME MANGLING IN PYTHON

# so 3 types of attributes- access modifiers-public, private, protected
# normally in python every attribute is public
# so we can access public variables within the class or outside of the class.
# we can also access by using class name or object reference.
""" the name mangling process helps to access the class variables outside the class
In NM process any idntifier with two leading underscore and one trailing under score is textually replaced with
_classname_identifier"""



# PuBLIC ATTRIBUTES
class Test:
    x = 30
    def display(self):
        print(Test.x)
t = Test() #object creation
t.display() #calling
print(Test.x) #access using class name)
print(t.x) # access using object reference


# PROTECTED
# protected attributes we can access within the class any where but from outside of the class in child class

class Test:
    def __init__(self):
        self._x = 30   #protected variable
    def display(self): # here we r using display method
        print(self._x) #we r acessing the protected member inside the class
class SubTest(Test):    # from child class
    def show(self):  # we r using show method
        print(self._x)
t = SubTest()  # object creation
t.display()   # calling
t.show()
print(t._x) # if we want to access outside of the class
# i.e here we r using object reference._variable name


#PRIVATE ATTRIBUTES
"""private attributes can be accessed within the class and we cannot access outside of the class.
"""

class Fruits:
    def __init__(self):
        self.__apple = 40 # private variable
    def display(self):
        print(self.__apple)

v1 = Fruits() #object creation
v1.display()  # calling

#from outside the class- we can access by objectreference._classname__variable name
print(v1._Fruits__apple)
