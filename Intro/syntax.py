# comment start with hash (shortcut is ctrl + /)

"""
Multi line comment 
"""
# ----INDENTATION-----
# only tab is acceptable

# ----BASE FUNCTIONS----

# print stuff to console
print('Hello World!')

# ----VARIABLES----

# Variables are names assigned to values
# The 1st character must be _ or a letter
# Then you can use letters, numbers or _
# Variable names are type sensitive

a = 10
print(a)

# variables are written in camelCase
aNewVariable: int = 5

# constants are written all caps in snake_case
THIS_IS_A_CONSTANT = 3.14
print(THIS_IS_A_CONSTANT)

# ----TYPES----

# python is a dynamically typed language so type is usually inferred
# but luckily we can statically type if we want

# find type of variable or element
print(type(a))

# integer
b: int = 10
print(type(b))

# floating point number 
f: float = 1.5
print(type(f))

# boolean
g: bool = True
print(type(g))

# strings
c: str = 'String'
print(type(c))
d: str = "Still a string"
print(type(d))
e: str = '''A string with apostrophe' and quotes" '''
print(type(e))

# ----MATHS----

# --Operators--

tmp: int = 10
tmp2: int = 5

# plus +
print(tmp + tmp2)
# minus -
print(tmp - tmp2)
# times *
print(tmp * tmp2)
# divide /
print(tmp / tmp2)
# modulus %
print(tmp % tmp2)
# exponent **
print(tmp ** tmp2)
# floor division //
print(tmp // tmp2)

# --Logic--

# equals ==
print(tmp == tmp2)
# not equals !=
print(tmp != tmp2)
# greater than >
print(tmp > tmp2)
# greater equal >=
print(tmp >= tmp2)
# lesser than <
print(tmp < tmp2)
# lesser equal than <=
print(tmp <= tmp2)

# --Assignement--

# assign =
# plus equals +=
# subtract equals -=
# multiply equals *=
# divide equals /=

# --Logic Operators--

# and  &
# or |
# not !

# --Membership Operators--
# checks if element in sequence  in
# checks if element is not in sequence not in

