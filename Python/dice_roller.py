
# Automatic Dice Roller
# Written by Kaymin H.

# from random import randint
import random 

print ("Automatic Dice Roller")

repeat = True

while(repeat == True): # checks if repeat is equal to True
	print ("You rolled",random.randint(1,6))
	print ("Do you want to roll the dice again? (Enter/x) ")
	val = input("")
	# sets value equal to whatever you type in after the code runs
	if (val == "x"):
	# if the value is equal to one specific input, it stops repeating
		repeat = False
		print ("Thanks for playing!")
