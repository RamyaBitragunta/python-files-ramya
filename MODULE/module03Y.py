
# sometimes we have multiple modules having the same function
# eg:- there are two modules  a and b; having the same disc function
# if we import a and b in another module; and when i call the disc function,from which module wil be called?

#approach 1

import bird01
import bird02

bird01.fly()
bird01.color()

bird02.fly()
bird02.color()



#approach 2

from bird01 import *
from bird02 import *

fly()
color()

# from which ever module we have imported at the last; from that module ; function will be called and executed
# bt how we can solve this conflict ? For this ----

from bird01 import *

fly()
color()

from bird02 import *

fly()
color()

