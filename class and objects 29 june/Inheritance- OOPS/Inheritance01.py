 # SINGLE INHERITANCE

class Animal:
     def speak(self):
         print("Animal speak")

class Dog:
    def bark(self):
        print("Bow -Bow")

myanimal = Animal()
myanimal.speak()

mydog = Dog()
mydog.bark()

#bt its normal , there is no relation b/w animal and dog


class Animal:
     def speak(self):
         print("Animal speak")

class Dog(Animal):  #child class has access to all the methods and variables.
     def bark(self):
         print("Bow -Bow")

mydog = Dog()
mydog.bark()
mydog.speak()