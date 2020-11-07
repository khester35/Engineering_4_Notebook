# Find and output roots of a quadratic equation when given a, b, & c
# Kaymin Hester

import cmath

a = int(input())
b = int(input())
c = int(input())

# quadratic equation

d = (b**2) - (4*a*c) # calculate the discriminant

while True:
	if (a == 0): # if a = 0, the quadratic equation is not a quadratic equation + the code breaks
		print ("Error")
		break  # return only works inside a function; break works inside a loop

	else:
		ans1 = (-b - cmath.sqrt(d))/(2*a)
		ans2 = (-b + cmath.sqrt(d))/(2*a)

		print ("The roots are:")
		print (ans1)
		print (ans2)

		break
