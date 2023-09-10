
#for class varaible we have to specify self-key window, if it is a local variable need not specify self .
#private variables and private methods have access within the class and outside of the class- we cannot access.
#always we have to specify class variables and class methods with self key window


class Demo:
    def __init__(self):
        self.a = 1
        self._b = 1
    def display(self):
        return self.__b

obj = Demo()
print(obj.a)
#the program has no error bcz the class menber which is public is printed

class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def display(self):
        return self.__b

obj = Demo()
print(obj.__b)
#the program has an error because b is private member of the class and cannot be accessed directly.
