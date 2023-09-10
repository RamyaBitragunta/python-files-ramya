#ENCAPSULATION - OOPS IN PYTHON
"""encapsulation is the process of combining attributes(variables) and methods within a class
_data protection- eg: bank balance
variables-data protection- public, private and protected
private- we change the variables -data only inside the class
protected- inside the class + and its subclass"""


#private
class BankAccount:
    def __init__(self,balance,password):
        self.__balance = balance #private variable
        self.__password = password #private variable
    def show_data(self):
        print(self.__balance)
        print(self.__password)

obj1 = BankAccount(30,"ram")

obj1.show_data()


#protected

class A:
    def __init__(self):
        self._a = 10 #single underscore we r using(protected)
        self._b = 20
class B(A): #inheriting the values of A in sub-class B
    def __init__(self):
        A.__init__(self) #we have to call the parent class and have to call init method

    def show_data(self):
        print(self._a)
        print(self._b)

obj2 = B()

obj2.show_data()



