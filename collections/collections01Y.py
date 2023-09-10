

#COLLECTIONS  MODULE

""" Collection modules implements special container data types and provoides alternatives with some additional
functionalities compared to the general built in containers like dictionaries, lists and tuples
----5 duff data types from the collections module
the counter,namedtuple, ordereddict, defaultdict, deque

First we have to import then

Counter is a container that stores the elements as dictionary keys and their counts as dictionary values"""

from collections import Counter
a = "aaaaaaabbbbbcccc"
my_counter = Counter(a)
print(my_counter)

# and if we print this - then we can see a dictionary with all the diff characters as keys and their count as values

print(my_counter.items())
# we can see all the items like key value pair

print(my_counter.keys())
# this will iterate over the keys

print(my_counter.values())
# this will iterate over the values

# if we want to look at the most common element in our counter dictionary
print(my_counter.most_common(1)) # this will return a list with tuples in it.
print(my_counter.most_common(2)) # wil give two most common types

print(my_counter.most_common(1)[0]) # this will return the tuple at index 0(zero)
print(my_counter.most_common(1)[0][0])  # if we only want to see the element -first element of tuple- most common

# we can also have a lists with all dif elements
print(list(my_counter.elements()))
# we can get elements as a list
