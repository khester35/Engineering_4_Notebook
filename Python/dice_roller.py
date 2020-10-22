
# Automatic Dice Roller
# Written by Kaymin H.

# from random import randint
import random

print ("Automatic Dice Roller")

repeat = True

while(repeat == True):
	print ("You rolled",random.randint(1,6))
	print ("Do you want to roll the dice again? (Enter/x) ")
	val = input("")
	if (val == "x"):
		repeat = False
		print ("Thanks for playing!")
