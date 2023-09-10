# NAME MANGLING METHOD
#  private members of the class can be accessed- if it is written as follows:
#  object reference._classname__privatemember
# such renaming of identifiers is called as name mingling.
# name mingling prevents unintentional access of the private members of a class, while still allowing access
#  when needed. Unless the variable is accessed with its mingled name, it will not be found.
# only private class members can be acccessed by name mingling method but protected members can't.

# 1.what will be the output of the following python code
class student:
    def __init__(self):
        self.marks = 97
        self.__cgpa = 8.7
    def display(self):
        print(self.marks)
obj = student()
print(obj._student__cgpa)

# the program runs fine and it prints 8.7
#  Bcz name mingling has been properly implemented in the code given above and hence the program runs properly.



# 2.what will be the output of the following python code

class Fruits:
    def __init__(self):
        self.price = 100
        self.__bags = 5
    def display(self):
        print(self.__bags)
obj = Fruits()
obj.display()

#the program runs fine and prints 5
# bcz private class members can be printed by the methods which are members of class.



# 3. what will be the output of the following python code

class objects:
    def __init__(self):
        self.color = None
        self._shape = "circle"
    def display(self,s):
        self._shape = s
obj = objects()
print(obj._objects_shape)

# output- error, bcz protected members cannot be accessed with name mingling method,
#they can be accessed within a class or by subclasses.