

from collections import namedtuple

Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt)
print(pt.x,pt.y)

# namedtuples are easy to create  and light-weight object type.
# we have defined our namedtuple - Point
# and in named tuple we have given first argument - the class name= (Point)
# and here the second argument we use the other string(x,y)
# this will create a class called Point with a fields of x and y
# if we print..we wil get a point(x =1 and y = -4)
# and we can also access the field by writing pt.x, pt.y and this will print the values of x and y

#------------------------------------------------------------------------------------------------------------------


#from collections import OrderedDict

# orderdedict are like regular dictionary...bt they remember their order that the items were inserted
# bt recent versions of normal dictionary can remember the order

# -------------------------------------------------------------------------------------------------------


from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c'])



# defaultdict is similar to normal dictionary with only difference .that it wil have a default value if the
# key has not been set yet
# for c- it wil return the default values of integers- i.e., zero (0)


d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c'])

# for float it will return 0.0(zero point zero)


d = {}
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c'])

# it would raise the- key error

