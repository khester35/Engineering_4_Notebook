# Make a game of hangman where one player inputs a word and the other player tries to guess it before the man has been completed 
# Kaymin Hester

import time

wrongArr = ["________	",
	    "|       |  ",
            "|       O  ",
            "|      /|\\",
            "|      / \\", # \ is an escape character, so you have to escape the escape character
            "|          ",
	    "|		"]

print ("Hello, Player 1! Hello, Player 2!")
print ("Player 1, set your word.")

word = input()
time.sleep(1)

print ("Start guessing, Player 2!")
time.sleep(0.5)

guesses = ' ' # creates a variable with an empty value

turns = len(wrongArr) # determines the number of turns and sets it equal to the length of the array
save = turns

while turns > 0:
    failed = 0 # a counter that starts with zero
    for char in word:
        if char in guesses: # see if the character is in the player's guess
            print (char) # print out the character

        else:
            print ("_") # if not found, print a dash
            failed += 1 # and increase the failed counter by 1

    if failed == 0:
        print ("You won")
        break

    print

    guess = input() # ask the user to guess a character
    guesses += guess # set the player's guess to guesses

    if guess not in word:
        turns -= 1
# save - turns = number you started w/ - number you have now
        for i in range(save - turns): # range produces a list of the values from zero to n - 1
       	    print (wrongArr[i]) #prints the i item in the array
        print ("You have", + turns, 'more guesses')

        if turns == 0:
            print ("You lost :(")

    print ("_______________________________")
