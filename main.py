'''
## Guessing Game 

In this assignment you will create a guessing game using user input, random, and conditional statements. 

You, the computer, will choose a random number between 1 and 10, then prompt the user to guess the number. Using the user's guess and comparing it to the computer's number, give the user feedback such as "Too high" or "Too low" or "You got it" 

*Ex* 

> Guess the number I'm thinking of: 9
  Sorry too high!


Review:

while loop
>> Repeats body statement until the condition becomes false.

Format:

while (Condition):
  Body Statement

else:
  Body Statement

# Expected outputs: 1x Python, 2x bye, 3x Evergreen, 4x 2021

student = 10

while (student > 0):
  if (student >= 11):
    print ("hello")
  elif (student >= 10):
    print ("Python")
  elif (student > 7):
    print ("bye")
  elif (student >= 5):
    print ("Everegreen")
  else:
    print (2021)

  student -= 1



import random

print ("Level 1 : 1 - 10\nLevel 2 : 1 - 100\nLevel 3 : 1 - 1000 ")
level = 10 ** int(input("Enter a level: Level "))


ranNum = random.randint(1, level)
playNum = int(input("Enter a number (1 - " + str(level) + "): "))

while (ranNum != playNum):

  # ranNum is greater than playNum
  if (ranNum > playNum):
    print ("Your number is too low.")

  # ranNum is less than playNum
  elif (playNum > ranNum):
    print ("Your number is too high.")

  # Ask player Number again
  playNum = int(input("Enter a number (1 - 10): "))

# Equal:
else:
  print ("You got it!")



for loop
Repeat a set of statements a certain number of times.


Formula

for LCV in Sequence:
  Body Statement


Loop Control Variable (LCV)
An ordinary int variable that is initialized, tested, and changed as the loop executes.


Sequence
An iteration statement

a. range(#)
b. list, tuple, or dictionary


# Example

for n in range(15):     # [0, 1, 2, 3, 4]
  print (n)


range() function

1 argument; range(#) -> range(stop)
2 arguments; range(#, #) -> range(start, stop)
3 arguments; range(#, #, #) -> range(start, stop, step)

# Ex
range(4)  # 0,1,2,3
range(3, 8)   # 3, 4, 5, 6, 7
range(1, 13, 3)   # 1, 4, 7, 10

'''