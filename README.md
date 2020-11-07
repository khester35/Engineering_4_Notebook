# My Engineering 4 Notebook

This is a collection of my assignments from Engineering 4. 

### Hello Python

This assignment is a pretty basic one; therefore, it was easy to find online. The code I found worked pretty seamlessly; the dice would roll and in order to get it to roll again, you had to type "Y". If you didn't type "Y", the game would end. However, the instructions on our assignment were very specific and that's where I ran into a hurdle. It was easy to end the game if you did not type a certain input, but it was much harder to end the game if you did type a certain input. Basically, I had no trouble setting it to repeat if you typed any input—a specific letter, a number, etc.— and end if you didn't. However, the Enter key was the one exception. If I didn't set it to repeat after a specific input, it would never stop, even if I typed in the X. I tried a million things but what ultimately ended up working was swapping the approach. Instead of stating that it would repeat under a specific condition, I had to state that it would stop repeating under a specific condition. It seems easy, and honestly, it probably shouldn't have taken me as much time as it did. However, I figured it out (with the help of Google and a friend) and it taught me that sometimes, the solution is right under your nose. This assignment reminded me that I have to consider every aspect of the code instead of just changing the same two or three lines. 

### Python Program 01 - Calculator

I actually wrote the code for the calculator straight out before I did anything else. I found a [page](https://www.sanfoundry.com/python-program-take-numbers-print-quotient-remainder/) that gave me the code and it was extremely easy. I did, however, struggle a little bit with the function. Defining it wasn't all that bad once I finally understood what I was doing but it took a long time and a lot of Google to figure it out. I found [a good explanation](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links) of what exactly functions were, what purposes they served, and how to define them. I defined each number (1-5) as addition, subtraction, etc. 

```
  if (type == 1): # addition
     return(num1+num2)
```

However, it gave me an error saying "can only concatenate str (not "int") to str". After a little bit of digging, I found a [forum](https://stackoverflow.com/questions/51252580/how-to-resolve-typeerror-can-only-concatenate-str-not-int-to-str) that helped me out. I ended up changing my code to fix the issue and this is what  Igot. 

```
  if (type == 1): # addition
     return(str(num1+num2))
```

Then, I had to round the quotient to two digits. If you use the round() function, it rounds it to the nearest whole number. I read a little bit about the round() function and how it works, then found the truncate() function. It gives you more control over what place you round to, as described [here](https://realpython.com/python-rounding/). To use this function, I had to define it similarly to what I had to do with doMath. 

```
def truncate(type, decimals=2) # defining the function that rounds to two decimal places
  multiplier = 10 ** decimals # 10^decimals
  return int(type * multiplier)/multiplier
```

I put the quotient in the truncate function like so: 

```
  elif (type == 4): # quotient
    return(str(truncate(num1/num2)))
```

And it worked perfectly!

### Quadratic Calculator

#### Objective

In this assignment, we had to make a quadratic equation solver. The user inputs a, b, and c in the context of the quadratic equation (ax^2 + bx + c) and the solver spits out the roots. 

#### Methodology/Lessons

My solver evolved a lot over the course of this assignment! At first, I used [this site](https://www.programiz.com/python-programming/examples/quadratic-roots) and [this site](https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/) when writing my program. These two programs both import the cmath module, which allows you to work with complex numbers, and used the quadratic formula to find the roots. 

```
import cmath

a = int(input())
b = int(input())
c = int(input())

d = (b**2) - (4*a*c)

x1 = (-b - cmath.sqrt(d))/(2*a)
x2 = (-b + cmath.sqrt(d))/(2*a)

print(x1)
print(x2)
```

This makes it so the program will print imaginary roots for numbers that don’t exist. Another flaw with the program was that if a user typed 0 when prompted to type a or typed any character that didn't fit the requirements for a, b, or c, the code would give me an error. This makes sense because if a = 0, then the coefficient of the first term = 0 and it’s no longer a quadratic function/the coefficient can't be a letter or special character or else it's invalid. However, I wanted the code to account for situations like these. Therefore, I used [this code](https://trinket.io/python/a2d73e78a4) instead, which solved all of these issues. I also found a really neat [explanation](https://medium.com/swlh/build-your-own-quadratic-equation-solver-in-python-4f70e48d2ca4) that broke down each part of the code and why the user chose to write what they did. This really helped me when commenting what was going on in each line. Instead of importing cmath, I imported the square root function from the numpy module, which meant that it was no longer capable of computing the square root of negative numbers. I also used while 1: loops when asking for the user’s input for a, b, and c.

```
while 1:
	try:
		b = int(input())
		break
	except ValueError:
		print ("Enter a number")
		continue
```

If it worked, I used break to exit the loop and continue through the code—when I was still working with my first two resources, I tried to use return() to end something and it gave me an error. It told me that “return was outside the function”. I found an explanation and realized that return() only works within functions. When using a loop, break will work much better. If the user input wasn’t valid (wasn’t an integer), it asked the user to try again with a valid character and if once they did, it would start the loop from the beginning and break, running through the rest of the code. Next, I used an if statement to make the code print Error if the user typed 0 = a. 

```
if a == 0: 
  print ("Error")
```

Then, I used else (as long as a did not = 0) and another if statement to tell the code to print “No real roots” if the discriminant (the part inside the square root) was negative. 

```
else:
	if d<0: 
		print ("No real roots")
```

The corresponding else (still inside the other else) told it to run through computing if all of the necessary conditions were met. 

```
else:
		x1 = (-b - sqrt(d))/(2*a)
		x2 = (-b + sqrt(d))/(2*a)

		print ("The roots are:")
		print ("x1 = "+str(x1))
		print ("x2 = "+str(x2))
```
