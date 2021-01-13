# USER INPUT -------------
import sys 

print('What is your name?')
 
# Stores everything typed up until ENTER
# name = sys.stdin.readline()
 
# print('Hello', name)


# game time 


def add_four(a: int, b: int, c: int, d: int):
    return a+b+c+d

def dividing(a:int, b:int):
    return b/a

while True:
    print('first number please') 
    inputHappy = False
    while inputHappy is not True:
        input = sys.stdin.readline().rstrip()
        if input.isdigit():

            a: int = int(input) #casting
            inputHappy = True
        else:
            print("give me a digit fucker")
            
    print('second number please')    
    inputHappy = False
    while inputHappy is not True:
        input = sys.stdin.readline().rstrip()
        if input.isdigit():

            b: int = int(input) #casting
            inputHappy = True
        else:
            print("give me a digit fucker")

    print('third number please') 
    inputHappy = False       
    while inputHappy is False:
        input = sys.stdin.readline().rstrip()
        if input.isdigit():

            c: int = int(input) #casting
            inputHappy = True
        else:
            print("give me a digit fucker")
    print('four number please')  
    inputHappy = False      
    while inputHappy is False:
        input = sys.stdin.readline().rstrip()
        if input.isdigit():

            d: int = int(input) #casting
            inputHappy = True
        else:
            print("give me a digit fucker")

    result: int = add_four(a, b, c, d)
    print('result: '  f'{result}')
    print('press q to quit or any other key to continue')
    e: str = sys.stdin.readline().rstrip()
    if e == 'q':
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
# can you split the duplicate code into nice functions
# have fun