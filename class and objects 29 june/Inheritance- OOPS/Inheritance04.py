
# MULTI-LEVEL INHERITENCE

""" Multi-level iheritance involves a class inheriting from a derived class"""
 #vehicle- car- Tesla
 #there will be is a relationship - i.e., car is a vehicle and tesla is a car.

class Vehicle:
    def start_engine(self):
         print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("Driving the car")

class Tesla(Car):
    def race(self):
        print("Tesla car")

my_car = Tesla()


my_car.start_engine()
my_car.drive()
my_car.race()

#or we can write

my_vehicle = Vehicle()
my_car.drive()