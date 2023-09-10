
# last collections type - deque

from collections import deque
d = deque()

d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)

d.pop()
print(d)
d.popleft()
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([8,9]) #note- it will add elements from the left side i.e., 9 wil be the first element followed by 8
print(d)

d.rotate(1) # this will rotate all the elements one place to the right
d.rotate(2) # this will rotate all the elements two places to the right
d.rotate(-1) # this will rotate all the elements one place to the left
print(d)

d.clear()
print(d)
# deque is a double ended queue - it can be used to add or remove the elements from both ends
# pop - removes last element
# clear removes all the elements.
