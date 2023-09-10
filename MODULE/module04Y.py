
#upto now we have specified functions in modules; suppose if the modules have classes and methods,then how
# we can access them in main module?

""" Now we have another two modules- newmodule.py and newmodule01.py
IF these modules have same common function called display method but both belong to different classes"""

#approach 1

import newmodule
import newmodule01

obj1 = newmodule.Animal()
obj1.display()

obj2 = newmodule01.Bird()
obj2.display()

#now we need to call these classes , for access these classes in main module, there should be an object for these classes.
# obj = Animal()
# bt it doesnot know from which module it is coming from; so we must specify modulname.classname
# by using this object we can call the display method.


#------------------------------------------------------------------------------------------

#approach 2

from newmodule import Animal
from newmodule01 import Bird

obj = Animal()
obj.display()

obj3 = Bird()
obj3.display()