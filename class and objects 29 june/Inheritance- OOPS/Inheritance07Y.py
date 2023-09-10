
#parent class(Base class) -----> child class (derived class)

class Parent:
    def __init__(self,f_name,f_age):
        self.f_name = f_name
        self.f_age = f_age

    def view(self):
        print(self.f_name, self.f_age)

class Child(Parent):
    def __init__(self,f_name,f_age,last_name):
        Parent.__init__(self,f_name,f_age)
        self.last_name = last_name

    def hide(self):
        print(self.f_name,self.f_age,self.last_name)

obj = Child("Python","Edurekha",23)
obj.view()
obj.hide()
