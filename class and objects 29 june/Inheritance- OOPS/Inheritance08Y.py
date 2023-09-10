# python super function
# SUPER FUNCTION directly calls the parent class method

class Parent:
    def func1(self):
        print("this is function 1")

class Child(Parent):
    def func2(self):
        super().func1()
        print("this is function 2")

obj = Child()
obj.func2()


#instead of calling the parent function from the object, we can use super function
# super function can call directly the parent method without calling it using object