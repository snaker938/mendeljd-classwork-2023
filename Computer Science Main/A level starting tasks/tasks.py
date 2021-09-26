import math
from os import system, name
from random import *
from math import *

def clear():
    if name == 'nt':
        _ = system('cls')

# ---------------------------------------

# Names:

# print("What is your first name?")
# first_name = str(input())
# print("What is your second name?")
# surname = str(input())

# print(f"{first_name} {surname}")



# Password:

# password = list(input("What is your password?"))
# if len(password) > 6:
#     print("Password is valid")
# else:
#     print("Password is not valid")



# Options:

# number = int(input("Pick an option between 1 and 3"))
# while number > 3 or number < 1:
#     print("Not a valid number")
#     number = int(input())
# print(f"You have selected option {number}")



# Division:

# integer = int(input("Choose an integer "))
# divisor = int(input("Choose a  divisor "))

# first = integer // divisor
# second = integer % divisor

# print(f"{first} remainder {second}")




# Hundreds, tens and units:

# number = int(input("Choose a number between 100 and 999 "))

# hundreds = number // 100
# tens = (number % 100) // 10
# units = (number - ((100 * hundreds) + (10 * tens)))

# print(f"{hundreds} hundreds, {tens} tens and {units} units.")




# Number sequence:

# for i in range(1, 11):
#     print(i)




# Time Tables:

# number = int(input("Choose a number between 1 and 10 "))

# for i in range(1, 11):
#     print(number * i)





# Comparison of Two:

# first = int(input())
# second = int(input())

# if first > second:
#     print(first, second)
# else:
#     print(second, first)




# Comparison of Three:

# numbers = []
# for i in range(0, 3):
#     numbers.append(int(input()))

# print("")

# numbers.sort()
# for i in range(0, 3):
#     print(numbers[i])




# Words, Words, Words:
# count = 0

# sentence = str(input())
# for i in sentence:
#     if(i.isspace()):
#         count=count+1

# print(count + 1)



# # Seconds Anyone?:

# time = input()

# splitTime = time.split(":")


# totalSeconds = (int(splitTime[0]) * 60 * 60) + (int(splitTime[1]) * 60) + int(splitTime[2])
# print(totalSeconds)




# Factors:

# number = int(input())
# clear()

# factors = []

# for i in range(1, number + 1):
#     if number % i == 0:
#         factors.append(i)

# for i in range(0, len(factors)):
#     print(factors[i])





# Caesar Cypher 

# string = str(input())
# string.lower()
# stringArray = []
# newStringAray = []
# letters = ["a", "b", "c", "d", "e", "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for a in string:
#     stringArray.append(a)

# for i in range(0, len(stringArray)):
#     if stringArray[i] == "z":
#         newLetter = "a"
#         newStringAray.append(newLetter)
#     else:
#         indexNew = letters.index(stringArray[i]) + 1
#         newLetter = letters[indexNew]
#         newStringAray.append(newLetter)


# print(newStringAray)





# Reverse:

# string = str(input())

# stringReversed = (list(reversed(string)))

# print("".join(stringReversed))






# Rock, paper, scissors:



# def play():
#     clear()
#     move = str(input("Enter your move: R, P or S: "))
#     move = move.upper()

#     while (move != "R") and (move != "S") and (move != "P"):
#         clear()
#         move = str(input("Enter your move: R, P or S: "))
#         move = move.upper()
        

#     move = move.lower()
#     randomNumber = randint(0, 2)
#     computerMoves = ["r", "p", "s"]
#     computerMove = computerMoves[randomNumber]

#     if move == "p":
#         if computerMove == "s":
#             print("You lost")
#         elif computerMove == "r":
#             print("You won!")
#         else:
#             print("You drew!")

#     if move == "r":
#         if computerMove == "p":
#             print("You lost")
#         elif computerMove == "s":
#             print("You won!")
#         else:
#             print("You drew!")

#     if move == "s":
#         if computerMove == "r":
#             print("You lost")
#         elif computerMove == "p":
#             print("You won!")
#         else:
#             print("You drew!")

#     print("")
#     answer = str(input("Do you want to play again? ('Y' or 'N'): "))
#     answer = answer.upper()
#     if answer == "Y":
#         play()
#     else:
#         exit
# play()

