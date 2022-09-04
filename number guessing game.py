# Algorithm
#==========
# input both upper and lower bounds from user
# generate a rondom number
# calculate max guesses using our equation => log2((upper - lower) + 1)
# display the max guesses to the user
# initialize the count
# while count <= maxGuesses:
# input the user guess
# if guess is higher than random number:
# calulate the guesses left
# display it to user
# tell him he guessed higher and try agian
# do the opposite if the guess is lower than random number
# if guess == random number
# display a winning message to user
# then break the loop
# increment the count
# after the loop ends it means user lost
# check if count > max guesses:
# display a losing message to the user


import random
import math

# input lower and upper bounds from user
lower = int(input('Enter lower bound: '))
upper = int(input('Enter higher bound '))

# generating a random number within
# the lower and upper bounds
randomNum = random.randint(lower, upper)
# calculate the max amount of guesses
maxGuesses = round(math.log(((upper - lower) + 1),2))
print('you have only', maxGuesses, 'chances to guess the right number')
# initialize the count
count = 1
while count <= maxGuesses:
    # input the user guess
    guess = int(input('Guess a number within the range you picked: '))
    # testing the guess
    if guess > randomNum:
        # calculate the amount of guesses left
        guesseLeft= maxGuesses - count
        if guesseLeft > 0:
            print('You guessed a higher number, Try again')
            print('You have ', guesseLeft, 'guesses left')

    elif guess < randomNum:
        # calculate the amount of guesses left
        guesseLeft= maxGuesses - count
        if guesseLeft > 0:
            print('You guessed a lower number, Try again')
            print('You have ', guesseLeft, 'guesses left')
    else:
        print('Congrats!!!, you guessed the right number in', count, 'guesses')
        break
    # increment the count
    count += 1
if count > maxGuesses:
    print('The number is', randomNum)
    print('You lost, better luck next time')