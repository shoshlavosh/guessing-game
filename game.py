"""A guessing game"""

import random

answer = random.randint(1,100)

#greet user
print("Hello and welcome to the numbers guessing game."
 "Your job is to guess a number, picked at random, between 1 and 100.")

guess = " "

while guess:

    guess = int(input("Guess a number: "))

    if guess == answer: 
        print("You win!")
        break

    elif guess < 1 or guess > 100:
        print("Please pick a number between 1 and 100.")

    elif guess < answer:
        print("Too low, try again!")

    elif guess > answer:
        print("Too high, try again!")


