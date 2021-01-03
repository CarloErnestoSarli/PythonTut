""" casting """
# casting is the process of converting a variable type into another, usually it is done by putting the type name in front of the variable
# for instance

varA: int = 5
print(type(varA))
# output <class, int>

varB: float = float(varA)
print(type(varB))
# output <class, float>

# this is useful to convert datatypes and also lists to tuples and viceversa


""" list vs set vs tuple vs dict """

# lists are the most generic and therefore versatile collection type, they are mutable, indexable and ordered.

# tuples are like lists, but are immutable (they can't be changed i.e. adding values etc...). Tuples are ordered and indexable, but by their immutable nature they are faster and occupy less space in memory

# use tuples when you know the data inside will not need to change i.e. a person's anagraphical details

personDeets: tuple[str, str, int] = ('Natalia', 'Sikora', 24)

# tuples by being immutable also remove the issue of potential aliasing. aliasing happens when one variable is assigned (=) to another. while this can be useful, it has side effects

# consider this example:

list1: list[int] = [1,2,4,5]
list2 = list1
list2.insert(2, 3)

print(list1)

# otuput [1, 2, 3, 4, 5]
# as you can see we changed list1 while using list 2
# to avoid this we can either use touples instead or user the .copy() method

list1: list[int] = [1,2,4,5]
list2 = list1.copy()
list2.insert(2, 3)

print(list1)
print(list2)

# output [1, 2, 4, 5]   [1, 2, 3, 4, 5]


# using tuples instead 
# btw to declare a tuple of homogenous data you can use the syntax of [type, ...]

tuple1: tuple[int, ...] = (1,2,4,5)
list2: list[int] = list(tuple1) #this is a cast btw :)

list2.insert(2, 3)

print(tuple1)
print(list2)

# output (1, 2, 4, 5)   [1, 2, 3, 4, 5]

# dictionaries are notorious for causing aliasing problems
# speaking of, touples can be used as keys for dictionaries while lists can't as they are mutable

# dictionaries are very useful when the relationship between data is important, let's take our person details example from before and say that knowing the age of a person is important to us

personName: tuple[str, str] = ('Natalia', 'Sikora')

peopleWithAges: dict[tuple[str, str], int] = {}
peopleWithAges[personName] = 24

print(peopleWithAges)

# output {('Natalia', 'Sikora'): 24}

print(peopleWithAges.get(personName))

# output 24

# to avoid aliasing with dicts use the copy method as with tuples:

peopleWithAges2 = peopleWithAges.copy()
newPerson: tuple[str, str] = ('Carlo', 'Sarli')
peopleWithAges2[newPerson] = 25

print(peopleWithAges)
print(peopleWithAges2)

#output {('Natalia', 'Sikora'): 24}  {('Natalia', 'Sikora'): 24, ('Carlo', 'Sarli'): 25}

# when we look at loops we'll look at more interesting implementations of these

# sets are unordered and mutable, they are very fast but have very specific use. they are great when the important thing is whether an element is in a collection or not
# they are very useful to efficiently find and remove duplicates in a list or tuple

tupleA: tuple[str, ...] = ('n', 'a', 't', 'a', 'l', 'i', 'a')
setA: set[str] = set(tupleA)

print(tupleA)
print(setA)

#output ('n', 'a', 't', 'a', 'l', 'i', 'a')
#output {'i', 'l', 't', 'a', 'n'}
# notice how the set is jumbled up and without duplicates