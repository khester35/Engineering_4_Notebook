# Write a program that returns the sum, difference, product, quotient, and modulo. 
# Kaymin Hester

a = int(input())
b = int(input())

def truncate(type, decimals=2): # defining the function that rounds to two decimal places
	multiplier = 10 ** decimals # 10^decimals
	return int(type * multiplier)/multiplier 

def doMath(num1, num2, type): # defining the function

	if (type == 1): # addition
		return(str(num1+num2))

	elif (type == 2): # subtraction
		return(str(num1-num2))

	elif (type == 3): # product
		return(str(num1 * num2))

	elif (type == 4): #quotient
		return(str(truncate(num1/num2)))

	elif (type == 5): # modulo
		return(str(num1 % num2))

	else:
		return(None)

print ("Sum:\t\t" + doMath(a,b,1)) # \t = tab
print ("Difference:\t" + doMath(a,b,2))
print ("Product:\t" + doMath(a,b,3))
print ("Quotient:\t" + doMath(a,b,4))
print ("Modulo:\t\t" + doMath(a,b,5))
