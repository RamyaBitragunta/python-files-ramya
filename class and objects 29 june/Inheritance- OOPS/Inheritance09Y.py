# METHOD OVER-RIDING IN PYTHON

# method over-riding can be achieved to change functionality of parent class function.

class Parent:
    def func1(self):
        print("this is function 1")

class Child(Parent):
    def func1(self):
        print("this is function 2")

obj = Child() #object creation
obj.func1() #calling the function

# if we r calling func1 technically it should call the parent function bt
# it overwrites the parent class method and calls child's class function.