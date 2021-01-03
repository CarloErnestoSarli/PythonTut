# ----LISTS---

# Lists can contain mutable pieces of data of
# varying data types or even functions
l1 = [1, 3.14, "Derek", True]
 
# Get length
print("Length ", len(l1))
 
# Get value at index
print("1st", l1[0])
print("Last", l1[-1])
 
# Change value
l1[0] = 2
 
# Change multiple values
l1[2:4] = ["Bob", False]
 
# Insert at index without deleting
# Also l1.insert(2, "Paul")
l1[2:2] = ["Paul", 9]
 
# Add to end (Also l1.extend([5, 6]))
l2 = l1 + ["Egg", 4]
 
# Remove a value
l2.remove("Paul")
 
# Remove at index
l2.pop(0)
print("l2", l2)
 
# Add to beginning (Also l1.append([5, 6]))
l2 = ["Egg", 4] + l1
 
# Multidimensional list
l3 = [[1, 2], [3, 4]]
print("[1, 1]", l3[1][1])
 
# Does value exist
print("1 Exists", (1 in l1))
 
# Min & Max
print("Min ", min([1, 2, 3]))
print("Max ", max([1, 2, 3]))
 
# Slice out parts
print("1st 2", l1[0:2])
print("Every Other ", l1[0:-1:2])
print("Reverse ", l1[::-1])


# Static type list 
from typing import List

statList: List[int] = [1] 

# Tuples

# Tuples are just like lists except they are
# immutable
t1 = (1, 3.14, "Derek", False)
 
# Get length
print("Length ", len(t1))
 
# Get value / values
print("1st", t1[0])
print("Last", t1[-1])
print("1st 2", t1[0:2])
print("Every Other ", t1[0:-1:2])
print("Reverse ", t1[::-1])

# static type tuple

from typing import Tuple

statTuple: Tuple[str] = ('a', 'b')


# ----DICTIONARIES----

# Dictionaries are lists of key / value pairs
# Keys and values can use any data type
# Duplicate keys aren't allowed
heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne",
    "Spiderman": "Peter Parker"
}
 
villains = dict([
    ("Lex Luthor", "Lex Luthor"),
    ("Loki", "Loki")
])
 
print("Length", len(heroes))
 
# Get value by key
# Also heroes.get("Superman")
print(heroes["Superman"])
 
# Add more
heroes["Flash"] = "Barry Allan"
 
# Change a value
heroes["Flash"] = "Barry Allen"
 
# Get list of tuples
print(list(heroes.items()))
 
# Get list of keys and values
print(list(heroes.keys()))
print(list(heroes.values()))
 
# Delete
del heroes["Flash"]
 
# Remove a key and return it
print(heroes.pop("Batman"))
 
# Search for key
print("Superman" in heroes)


# ----SETS----

# ----- SETS -----
# Sets are lists that are unordered, unique
# and while values can change those values
# must be immutable

s1 = set(["Derek", 1])
 
s2 = {"Paul", 1}
 
# Size
print("Length", len(s2))
 
# Join sets
s3 = s1 | s2
print(s3)
 
# Add value
s3.add("Doug")
 
# Remove value
s3.discard("Derek")
 
# Remove random value
print("Random", s3.pop())
 
# Add values in s2 to s3
s3 |= s2
 
# Return common values (You can include multiple
# sets as attributes)
print(s1.intersection(s2))
 
# All unique values
print(s1.symmetric_difference(s2))
 
# Values in s1 but not in s2
print(s1.difference(s2))
 
# Clear values
s3.clear()
 
# Frozen sets can't be edited
s4 = frozenset(["Paul", 7])