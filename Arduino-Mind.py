from pyfirmata import Arduino
from time import sleep
import random
import pyttsx3

# initialize the engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# declare the port connected with Arduino UNO
board = Arduino("com6")


def dw(pin, mode):
    board.digital[pin].write(mode)


def dr(pin, mode):
    board.digital[pin].read(mode)


def assist(string):
    engine.say(string)
    engine.runAndWait()

assist("Hello there, I welcome you to this game, please enter your name")
name = input("Enter player name: ").title()
assist(f"Ok I will remember your name {name}, now enter any two positive numbers to play with")
_from, to = input("Enter range (from, to): ").split(" ")
_from, to = int(_from), int(to)
points = 0

assist(f"Ok {name}, now the game starts, all the best...")
while True:
    operator = ['+', '-', '*', '//', '%']
    num1 = random.randint(_from, to)
    num2 = random.randint(_from, to)
    op = random.choice(operator)

    exp = f"{num1} {op} {num2}"
    user = int(input(f"{exp} = "))
    try:
        output = eval(exp)
    except Exception:
        output = user

    if user == output:
        dw(2, 1)
        dw(3, 0)
        points += 1
        if points == 5:
            assist(f"Good {name}, you are playing well...")

        elif points == 20:
            assist(f"Wow great {name}, you are ultimate player of this game")

    elif user == -1:
        string = f"{name}, your gain is {points} XD, Thanks for Playing"
        print(string)
        assist(string)
        break

    else:
        dw(2, 0)
        dw(3, 1)
        string = f"Wrong {name}, your point is {points} XD"
        print(string)
        assist(string)
