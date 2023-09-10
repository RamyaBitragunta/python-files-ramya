

# suppose if we have one module, and if we want to find out how many classes have been created
# or how many methods or functions are created in the module

# lets create one module - my module name sunmodule
# now if we want to access sunmodule in this current module., we have to import it
# after importing it., dir is a predefined function, if we pass dir and module name - this will return how
# many classes present in particular module
# bt we cannot see how many methods are created inside these classes
# bt there is one condition- if these methods are created as a functions without having any class -
# then we can count how many methods are created- this we can write code as
# import m    # m- module name
# print(dir(m)) - if it doesnot have any classes in module

import sunmodule
print(dir(sunmodule))

