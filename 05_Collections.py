# Collection Module

# The collections module provides alternatives to built-in container data types 
# such as list, tuple and dict.

####################
#  namedtuple()    #
####################

# this function returns a tuple-like object with named fields. 
# These field attributes are accessible by lookup as well as by index.

import collections
student = collections.namedtuple('student', ["name", "age", "marks"])

s1 = student("Divyansh", 27, 42)

# access attribute by lookup
s1.name
s1.age
s1.marks

# access attribut by index
s1[0]
s1[1]
s1[2]

####################
#  deque()         #
####################

# double ended que

from collections import deque
u = ["united"]
u1 = deque(u)

# appending
u1.appendleft("manchester")
print(u1)

# removing values

u1.popleft()
print(u1)


################
# ChainMap     #
################

# It is a dictionary like class which is able to make a single view of multiple mappings. 
# It basically returns a list of several other dictionaries

from collections import ChainMap
a = { "club" : 'manchester united' , "country": 'England'}
b = { "player ": 'cristiano ronaldo' , "position": 'striker'}
c = ChainMap(a,b)
print(c)

c["club"]
c["country"]

# "to add a new dictionary in the ChainMap we use the following approach."

a1 = { "season": "2021-2022" , "goals": 18}
c = c.new_child(a1)
print(c)