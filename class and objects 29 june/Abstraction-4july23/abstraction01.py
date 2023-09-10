
# abstraction is a fundamental concept in object- oreinted programming that allows us to represent
# complex systems by simplifying and hiding unnecessary details.


# ABSTRACT BASE CLASS (ABC)
""" An abstract base class is a class that cannot be instantiated and is meant to be subcalssed.
 It serves as a blueprint for derived classes and defines a common interface or set of methods that
  derived classes must implement.
  In python, ABCs are created using the ABC metaclass from the abc module"""

from abc import ABC, abstract method
# ABC is abstract method class, it is a inbuilt class created in python


class Shape(ABC):
