#bikes-honda, pep, vespa
# name, color, mileage

class BikeBrand:
    def __init__(self,name,color,mileage):
        self.name = name
        self.color = color
        self.mileage = mileage

    def name_color(self):
        print(self.name, "is",self.color, "with",self.mileage,"mileage")

v1 = BikeBrand("Honda","Black",28)
v2 = BikeBrand("pep","pink",22)
v3 = BikeBrand("vespa","yellow",26)

v1.name_color()
v2.name_color()
v3.name_color()
