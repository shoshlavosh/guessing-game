"""A number-guessing game."""

import random

#get player name
user = input("Hi! What's your name? > ")

#greet player
print(f"Hi, {user}, welcome to the guessing game.")

#choose a random number between 1 and 100
rand_num = random.randint(1, 100)

guess_count = 0

#repeat forever:
while True:
    #get guess
    guess = input("Guess a number between 1-100 > ")
    try:
        guess = int(guess)
    except ValueError:
        print("That's not a number")

    #validate guess is in range 1-100
    if guess in range(1,101):

        #if guess is incorrect:
        if guess != rand_num:
            #give hint
            if guess > rand_num:
                print("Guess a lower number")
            else:
                print("Guess a higher number")
            #increase number of guesses
            guess_count = guess_count + 1

        else:
            #congratulate player
            print("Correct! You win!")
            print(f"You guessed in {guess_count} guesses")
            break