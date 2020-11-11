# Find and output roots of a quadratic equation when given a, b, & c
# Kaymin Hester

from numpy import sqrt

while 1: # infinite loop but w/ escape hatch
	try: # if it works, proceed
		a = int(input()) # user inputs a number
		break # return in functions, break in loops
	except ValueError: # tells program how to proceed if there is an error (user puts in bad input, etc.)
		print("Enter a number")
		continue

while 1:
	try:
		b = int(input())
		break
	except ValueError:
		print ("Enter a number")
		continue

while 1:
	try:
		c = int(input())
		break
	except ValueError:
		print("Enter a number")
		continue

# quadratic equation

d = (b**2) - (4*a*c) # calculate the discriminant
x1 = (-b - sqrt(d))/(2*a) # calculate the rest of the quadratic formula
x2 = (-b + sqrt(d))/(2*a)
arr = [x1, x2] # array

if a == 0: # if a = 0, the quadratic equation is not a quadratic equation + the code breaks
	print ("Error")

else:
	if d<0: # if the discriminant is negative, it can't be factored
		print ("No real roots")
	else:
		print ("The roots are: ", arr)
