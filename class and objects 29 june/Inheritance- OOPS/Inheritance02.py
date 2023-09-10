
# multiple Inheritance

#multiple inheriance is supported in case of python bt not in case of Java(by using classes).
#multiple inheritance allows a class to inherit from multiple base classes.

class A:
    def method_a(self):
        print("Method A")

    def greet(self):
        print("HelloA")

class B:
    def method_b(self):
        print("Method B")

    def greet(self):
        print("HelloB")

class C(A,B):
    def method_c(self):
        print("Method C")

my_object = C()
my_object.greet()


# so greet function is present in both class Aand Class B
# then which greet it is going to call ? it calls class A or class B greet?
# Java was not able to resolve this issue bt python can resolve it
# - By using a concept called MRO - Method Resolution order - The order in which base classes are searched for
# a particular attribute or method.
# so what is the order of the class C we have given in line 21 ..it is A,B
# so which greet function is first it is _A....
# supposeif the order is B,A then which function it will call -i.e., B


