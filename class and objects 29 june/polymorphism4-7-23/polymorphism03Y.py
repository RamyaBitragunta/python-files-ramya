
# METHOD OVERRIDING IN PYTHON

# it is one of the type of polymorphism
# it  is combined with the inheritance concept

class Father:
    def __init__(self):
        pass

    def height(self):
        print ("Height : ", 5.7)

    def education(self):
        print("Education: ", "degree")

    def last_name(self):
        print("Last name: xyz")

class Son(Father):
    def __init__(self):
        Father.__init__(self)

    def height(self):
        print ("Height : ", 5.11)

    def education(self):
        print("Education: ", "Engineering")

father = Father()
son = Son()

son.height()
son.education()
son.last_name()

# we use same methods of parent class in child class, and we change the data according to our needs


class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

obj = A(10,20)
print(obj)

# here we want to print obj value bt it prints the data regarding the memory of obj where it was stored
# so for printing obj value we use __str__ method

class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} {self.b}'

obj = A(10,20)
print(obj)

# so actually when we print (obj) ... it prints memory
# bt we over-rided it to print the data ... this is called method overriding.









