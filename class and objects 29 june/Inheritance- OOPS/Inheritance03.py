

# Multi-level Inheritence

class A:
    def greet(self):
        print("HelloA")
class B:

    def greet(self):
        print("HelloB")

class C(A,B):
    pass
class D(B,A):
    pass

my_object1 = C()
my_object1.greet()

my_object2 = D()
my_object2.greet()

print(C.mro()) # mro functn wil tells us the row of calng methds i.e. first which method it calls nd followed by which
print(D.mro())
