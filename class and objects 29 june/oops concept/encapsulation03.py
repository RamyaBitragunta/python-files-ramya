
#what will be the output of the following python code?

class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b
obj = Demo()
print(obj.get())
 #output -1
 # here, get(self) is a member of the class. Hence, it can even return a private member of the class.
 #because if this reason, the program runs fine, and 1 is printed.



#what is the output of the following
class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1
    def get(self):
        return self.__b
obj = Demo()
obj.a = 45
print(obj.a)

#the program runs properly and prints 45
# it is possible to change the values of public class members using the object of the class.