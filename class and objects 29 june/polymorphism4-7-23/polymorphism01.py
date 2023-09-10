
class Shape:
    def area(self):
        print("Area of a shape")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

shape1 = Rectangle(3,4)
shape2 = Circle(2)

print(shape1.area())
print(shape2.area())

#the refrence - depending upon which object we r refering it will change and it will calls only that function.
# if the object is rectangle then it will call the rectangle area function.
# if the object is rectangle then it will call the rectangle area function.
# But the reference is same- bcz of polymorphism ..bcz of single inheritance
# same function- bt different parameters
# that is...... child can have same function as the parent

