from random import *
n = randint(0, 100)
x = input("Guess a number between 0 and 100: ")

while isinstance(x, int) == False:
    try:
        x = int(x)
    except:
        x = input("That is not a number, man! Guess again: ")

while x != n:
    if x < 0:
        print("WOMP WOMP: Invalid number!")
    elif x > 100:
        print("WOMP WOMP: Invalid number!")
    elif x > n:
        print("Too high")
    elif x < n:
        print("Too low!")
    x = input("Try again: ")
    while isinstance(x, int) == False:
        try:
            x = int(x)
        except:
            x = input("That is not a number, man! Guess again: ")

print("YES! You got it!")
