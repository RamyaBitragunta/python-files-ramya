# Getter and setter method

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

person = Person("John",23)
print(person.get_name())
person.set_name("Ramya")
print(person.get_name())


#if we want certain conditions on variables then only getter and setter wil be used
# not to change data
#for eg if we want to change name from ramya to john (under private class variable) we cant change it

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self,name):
        if name == "John":
            print("Not a real name")
        else:
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >=0:
            self.__age = age
        else:
            print('Invalid age value.Age cannot be negative.')


person = Person("Ramya",23)
print(person.get_name())
person.set_name("John")
print(person.get_name())
print(person.get_age())
person.set_age(-1)





