# USER INPUT -------------
import sys 

print('What is your name?')
 
# Stores everything typed up until ENTER
name = sys.stdin.readline()
 
print('Hello', name)


# game time 

def add_two(a: int, b: int):
    return a+b

while True:
    print('first number please')
    a: int = int(sys.stdin.readline())
    print('second number please')
    b: int = int(sys.stdin.readline())
    result: int = add_two(a, b)
    print('result: '  f'{result}')
    print('press q to quit or any other key to continue')
    c: str = sys.stdin.readline().rstrip()
    if c == 'q':
        break
    else: 
        continue


# exercise time baby
#this program is fun but has many flaws
# first what if the user inputs something that is not a number?
# can you fix it?
# what if the user would like to input 3 or 4 numbers?
# can you do that?
# can you extend our little calculator to do divisions too?
# have fun