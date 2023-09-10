

# we can also create a constructor in abstract class

from abc import ABC,abstractmethod

class Cal(ABC):
    def __init__(self,value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
         pass

class Mob(Cal):
     def add(self):
         print(self.value+100)

     def sub(self):
         print(self.value-10)

obj1 = Mob(100)
obj1.add()
obj1.sub()



""" abstrct class should be extended from the ABc class i.e., predefined class
we have to import this ABC class from abc package along with the abstractmethod qualifier
Abstract class - is required only for security ..if we want to secure our methods and everything we 
have to make them as abstract class
and if we know the requirement and if we dont know how to implement them just create an abstract class
and as soon as we know the design part or implementation part, we can crete the subclasses and  we can 
implement them """

""" how to define a constructor ... with underscores  init method and self
 So constructors normally used for initialising the values. what ever we give beside self, we call it as 
 local variable. 
 so we need to make local variable as class variable so that we can access that class variable in 
 the subclasses in the other methods
 so how we can make it as class variable by adding to self
 eg: def __init__(self,value): #here value is a local variable belonging to constructor
           self.value = value ( by adding value to self. local variable is converted to a class variable.

 """