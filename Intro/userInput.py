# USER INPUT -------------
import sys 

print('What is your name?')
 
# Stores everything typed up until ENTER
# name = sys.stdin.readline()
 
# print('Hello', name)


# game time 

def add_two(a: int, b: int):
    return a + b 

def add_four(a: int, b: int, c: int, d: int):
    return a+b+c+d

def dividing(a: int, b: int):
    return a / b

def check_input() -> int:
    inputHappy: bool = False
    while inputHappy is not True:
        input = sys.stdin.readline().rstrip()
        if input.isdigit():

            userInput: int = int(input) #casting
            inputHappy = True
        else:
            print("give me a digit fucker")
    return userInput

while True:
    print("choose '+' for addition or '/' for division")
    operation: str = sys.stdin.readline().rstrip()

    print('first number please') 
    a: int = check_input()
            
    print('second number please')    
    b: int = check_input()

    if operation == '+':
        result: int = add_two(a , b)
    elif operation == '/' :
        result: int = int(dividing(a, b))
    else:
        #fill this
        pass

    # ask user if more numbers

    #make sure it still works with division
    moreNumbers: bool = True
    while moreNumbers:
        print("add another number? y/n")
        answer: str = sys.stdin.readline().rstrip()
        if answer == 'y':
            print('another number please')
            c: int = check_input()
            result = add_two(result, c)
        else: 
            moreNumbers = False


    print('result: '  f'{result}')


    print('press q to quit or any other key to continue')
    e: str = sys.stdin.readline().rstrip()
    if e == 'q':
        break
    else: 
        continue


# exercise time baby
# this program is fun but has many flaws
# first what if the user inputs something that is not a number? -DONE
# can you fix it?
# what if the user would like to input 3 or 4 numbers? -DONE
# can you do that?
# can you extend our little calculator to do divisions too? -NOT DONE
# can you split the duplicate code into nice functions -NOT DONE
# have fun