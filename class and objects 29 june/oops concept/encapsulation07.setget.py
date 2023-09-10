
class Student:
    def setName(self,n):  #setter method always starts with first word as set
        self.__name = n    #fisrt  parameter will be self and let us assume 2nd parameter as n
    def getName(self):       #we use self since it is an instance variable and also a private variable
        return self.__name   #getter method strts with get- this method return the value of private
                             #-instance variable-name

    def setMarks(self,m):    #let us assume we have another private instance variable marks and we define setter
        self.__marks = m     # and getter method for marks
    def getMarks(self):
        return self.__marks

    def display(self):                   #user-defined method or instance method i.e display
        print("Name:",self.__name)       #which takes one parameter -self
        print("Marks",self.__marks)

s = Student()   # object creation to a class
s.setName("ramya")  # use setter method to assign values of private instance variables i.e name and marks
s.setMarks(85.25)
s.display()   # call the display method

#remember - private instance variables are always preceeded by double underscores.
if """In display method instead of accessing the private instance variables directly we can also use
the getter methods 
i.e., print("Name:",self.getName())
      print("Marks",self.getmarks())
      and after executing the program we get the same result."""
