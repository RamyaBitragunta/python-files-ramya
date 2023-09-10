
""" Inheritance - is used for reusing the already existing code(usage of existing code.
- used for removal of duplicate code
"""

#single level inheritance

class A:
    def __init__(self,a_value):
        self.a = a_value

    def print_a(self):
        print("A value:",self.a)

class B(A):
    def __init__(self,a_value,b_value):
        A.__init__(self,a_value)
        self.b = b_value

    def print_b(self):
        print("B value:",self.b)

obj1 = B(10,20)
obj1.print_a()
obj1.print_b()

# 
