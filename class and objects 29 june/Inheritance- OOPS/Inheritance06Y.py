# Multi-level Inheritance

class Driver:
    def __init__(self,f_name,l_name,age,mob_no):
        self.f_name =  f_name  #first name
        self.l_name =  l_name  #lastname
        self.age = age
        self.mob_no = mob_no

    def full_name(self):
        return f'{self.f_name}{self.l_name}'

class License(Driver):  #parent class- Driver , child class- License
    def __init__(self,f_name,l_name,age,mob_no,license_id,validity_year):
        Driver.__init__(self,f_name,l_name,age,mob_no)
        self.license_id = license_id
        self.validity_year = validity_year

    def is_valid_license(self):
        if self.validity_year>=2021:
            return True
        else:
            return False

class Vehicle(License):
    def __init__(self,f_name,l_name,age,mob_no,license_id,validity_year,veh_no,veh_age):
        License.__init__(self,f_name,l_name,age,mob_no,license_id,validity_year)
        self.veh_no = veh_no
        self.veh_age = veh_age

    def is_valid_driver(self):
        if self.age>=20:
            return True
        else:
            return False

vehicle_one = Vehicle("Ramya","Bitragunta",27,1234,101,2022,201,2)
vehicle_two = Vehicle("Chakry","Gulakaram",28,12334,102,2019,202,4)

print(vehicle_one.full_name())
print('License:',vehicle_one.is_valid_license())
print("Driver eligible:",vehicle_one.is_valid_driver())

print(vehicle_two.full_name())
print(vehicle_two.is_valid_license())
print(vehicle_two.is_valid_driver())

