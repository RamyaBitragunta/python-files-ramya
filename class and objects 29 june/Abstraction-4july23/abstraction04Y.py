
""" suppose we have an abstract class - A- which contains the abstract methods.. that is these
methods are not implemented
so if we want to use this class we need to create one more subclass -eg:- B ,we have to extend class A into
 subclass and then we can implement the method
 and hence we can create an object for subclass but not to abstract class
 use- if we know the requirement but if we dont know the design part then we acn create teh abstract class
 (abstract method- is a method which contains a definition but not the body or implementation and those methods
  implementation can be done with the subclasses"""


from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        None

class B(A):
    def display(self):
        print("This is display method ")

obj = B()
obj.display()


#-------------------------------------------------------------------------------------------------


from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("Eats- Non-veg")

class Cow(Animal):
    def eat(self):
        print("Eats- veg")

obj1 = Tiger()
obj2 = Cow()
obj1.eat()
obj2.eat()

#  we can create multiple subclasses for the same abstract class and we can implement the abstract class
# in multiple classes also.


#-------------------------------------------------------------------------------


# we can also create a constructor to an abstract class.

