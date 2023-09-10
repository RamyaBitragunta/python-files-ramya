# real life example of single level inheritance:

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

user1_license = License("Ramya","Bitragunta",27,1234,101,2022)
user2_license = License("chakry","Gulakaram",28,1235,102,2020)

print(user1_license.full_name())
print("Eligibility of license: ",user1_license.is_valid_license())
print(user2_license.full_name())
print("Eligibility of license: ",user2_license.is_valid_license())


