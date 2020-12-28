# ----- LOOPS -----
# While : Execute while condition is True
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1
 
w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        w2 += 1
        # Skips to the next iteration of the loop
        continue
    w2 += 1
 
# Cycle through list
l4 = [1, 3.14, "Derek", True]
while len(l4):
    print(l4.pop(0))


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")    
 
# For Loop
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
# end="" eliminates newline
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')
 
# Cycle through list
l4 = [1, 3.14, "Derek", True]
for x in l4:
    print(x)
 
# You can also define a list of numbers to
# cycle through
for x in [2, 4, 6]:
    print(x)
 
# You can double up for loops to cycle through lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
 
# ----- ITERATORS -----
# You can pass an object to iter() which returns
# an iterator which allows you to cycle
l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr))  # Grab next value
 
# ----- RANGES -----
# The range() function creates integer iterables
print(list(range(0, 5)))
 
# You can define step
print(list(range(0, 10, 2)))
 
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])