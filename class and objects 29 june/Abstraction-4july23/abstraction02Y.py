

# ABSTRACTION

""" First we create a class - abstract class.  This abstract class will gives the structure,
and based on this structure we create multiple sub-classes and according to our requirement we create classes.
  We cant create an object for an abstract class
  Abstract class will gives a plan(structure)- and also contains code
   Abstract class contains both abstract methods and normal methods"""
# we will import ABC(abstract base class) from abc (its a prebuilt abc module)
#  in line- 12 -abstract method is a decorator

from abc import ABC,abstractmethod


class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    def __init__(self):
        pass

    def no_of_sides(self):
        print("I have 3 sides")

class Rectangle(Polygon):
    def __init__(self):
            pass
    def no_of_sides(self):
        print("I have 4 sides")

obj1 = Triangle()
obj2 = Rectangle()

obj1.no_of_sides()
obj2.no_of_sides()


