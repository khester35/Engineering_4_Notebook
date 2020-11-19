# My Engineering 4 Notebook

This is a collection of my assignments from Engineering 4. 

### Hello Python

#### Objective

In this assignment, I wrote a program that rolls a random number between 1 and 6. The program runs again if the user presses Enter and quits if the user presses "x" and Enter. 

#### Methodology/Lesson
This assignment is a pretty basic one; therefore, it was easy to find online. The [code](https://www.pythonforbeginners.com/code-snippets-source-code/game-rolling-the-dice) I found worked pretty seamlessly; the dice would roll and in order to get it to roll again, you had to type "Y". 
```
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
```

However, the instructions on our assignment were very specific and that's where I ran into a hurdle. It was easy to end the game if you did not type a certain input, but it was much harder to end the game if you did type a certain input. Basically, I had no trouble setting it to repeat if you typed any input—a specific letter, a number, etc.— and end if you didn't. However, the Enter key was the one exception. If I didn't set it to repeat after a specific input, it would never stop, even if I typed in the X. I tried a million things but what ultimately ended up working was swapping the approach. Instead of stating that it would repeat under a specific condition, I had to state that it would stop repeating under a specific condition. 

```
repeat = True

while(repeat == True): 

	if (val == "x"):
		repeat = False
		print ("Thanks for playing!")
```

It seems easy, and honestly, it probably shouldn't have taken me as much time as it did. However, I figured it out (with the help of Google and a friend) and it taught me that sometimes, the solution is right under your nose. This assignment reminded me that I have to consider every aspect of the code instead of just changing the same two or three lines. 

### Python Program 01 - Calculator

#### Objective

In this assignment, I wrote a program that gives you the sum, difference, quotient, and modulo of two numbers. The asks for the user to input two numbers and runs them through one function five times. 

#### Methodology/Lesson

I actually wrote the code for the calculator straight out before I did anything else. I found a [page](https://www.sanfoundry.com/python-program-take-numbers-print-quotient-remainder/) that gave me the code and it was extremely easy. I did, however, struggle a little bit with the function. Defining it wasn't all that bad once I finally understood what I was doing but it took a long time and a lot of Google to figure it out. I found [a good explanation](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links) of what exactly functions were, what purposes they served, and how to define them. I defined each number (1-5) as addition, subtraction, etc. 

```
  if (type == 1): # addition
     return(num1+num2)
```

However, it gave me an error saying "can only concatenate str (not "int") to str". After a little bit of digging, I found a [forum](https://stackoverflow.com/questions/51252580/how-to-resolve-typeerror-can-only-concatenate-str-not-int-to-str) that helped me out. I ended up changing my code to fix the issue and this is what I got. 

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

### Python Program 02 - Quadratic Solver

#### Objective

In this assignment, I had to make a quadratic equation solver. The user inputs a, b, and c in the context of the quadratic equation (ax^2 + bx + c) and the solver spits out the roots. 

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

However, this was kind of clunky. So, I used an array. I moved x1 and x2 to where I'd calculated the discriminant and put them into an array. 

``` 
d = (b**2) - (4*a*c)
x1 = (-b - sqrt(d))/(2*a)
x2 = (-b + sqrt(d))/(2*a)
arr = [x1, x2]

```

I kept the if/else as is and replaced the x1 and x2 with the array like so: 

```
else: 
	for values in arr:
		print ("The roots are: ", arr)
```
This worked but it printed each value twice. This was kind of frustrating, but I couldn't tell what I'd done wrong. However, the fix was kind of simple: I commented out "for values in arr:" and it worked perfectly! I ended up with this: 

```
else: 
	print ("The roots are: ", arr)
```

### Vertical Sentence

#### Objective

I made a program that asks the user for a sentence, then rewrites it vertically by word and by letter. 

#### Methodology/Lesson

First, I learned how to split up the sentence by word. [This forum](https://stackoverflow.com/questions/40027728/i-want-to-split-a-sentence-into-words-and-get-it-to-display-vertically/40027744) had a lot of good advice about splitting by word, so that aspect of the code was pretty straightforward. 

```
sentence = input("Enter a sentence: ".lower())

sentence = sentence.split()
for word in sentence:
	print (word)
```

First, I tried switching out "word" for "letter" like this:

```
sentence = input("Enter a sentence: ".lower())

sentence = sentence.split()
for letter in sentence:
	print (letter)
```

It still printed out by word. So, I googled what .split() actually meant. I found [this explanation](https://www.geeksforgeeks.org/python-string-split/), which doesn't go into too much depth but is definitely helpful. Therefore, I took out the sentence = sentence.split() entirely and got this, which worked!

```
for letter in sentence:
	print (letter)
```

Because I couldn't put sentence = sentence.split() after 

```
for word in sentence:
```

I just ran the line

```
for letter in sentence:
```

first and printed a space to separate the two. Then, I put

```
sentence = sentence.split()
for word in sentence:
	print (word)
```

and ended up with this!

```
sentence = input("Enter a sentence: ".lower())

for letter in sentence:
	print (letter)

print (" ")

sentence = sentence.split()
for word in sentence:
	print (word)
```

### Python Program 03 - Hangman Game

#### Objective

In this assignment, I made a two-player hangman game. When player 1 inputs the word, player 2 tries to guess it. If player 2 guesses wrong, it prints the hangman. If they guess it right, it prints the letter and dashes in place of the remaining letters. 

### Methodology/Lessons

Before I did anything, I started playing with [arrays](https://www.w3schools.com/python/python_arrays.asp). I did this because the assignment has a lot of different components and I wanted to break them down into digestible pieces. Then, I started out with the [the simplest game I could find](https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman). Going about it this way really helps me to understand the basics of the assignment and if I run into a problem, it's much easier to figure out if it's due to a gap in knowledge or just a lack of experience. I chose to make the game that outputs a generic phrase instead of a complicated array when you're wrong. 

When that started to work, I moved on to the array. I found the [characters](http://www.berkeleyinternet.com/perl/node30.html) to make the actual man. I put them in an array and put each one on a different line. 

```
wrongArr = ["________	",
	    "|       |  ",
            "|       O  ",
            "|      /|\\",
            "|      / \\", 
            "|          ",
	    "|		"]
```

I also learned that \ is an escape character. We used it in a previous assignment to represent tab (\t); the \ made it so the code wouldn't just output the letter t and would read it as tab. I set the number of turns allowed equal to the length of the array, which means that if the player doesn't guess all of the letters before the array prints all the way through, they lose. I also set a variable called save equal to turns. 

``` 
turns = len(wrongArr)
save = turns 
```

Setting the turns equal to the length of the array is basically the same as counting the number of inputs in the array and setting the number of turns equal to that. The difference comes if/when I need to change anything about the array. This keeps me from having to change the number of turns too. Setting the new variable equal to turns helps me out later. 

When I printed the array in response to an incorrect guess, I was having trouble printing each input at a time. If I just printed the array like so: 

```
print (wrongArr)
```

It would print the array straight out. Then, I found out what the range function was. Range basically sets a list of the values from zero to to whatever value you input. If I write

```
for i in range(3):
	print (wrongArr[i])
```

It will print out the first three values of the array. This is where save comes in handy. If I subtract the amount of turns the player has left from the save, which is equal to the initial amount of turns, which is equal to the length of the array, I get a number that rises as the number of turns lowers.

```
for i in range(save - turns):
	print (wrongArr[i])
```

The game starts by asking the first player to input a word. This is the word that the second player will be trying to guess. The code replaces all of the letters with dashes at first so the second player knows how many letters are in the word. When the second player puts in a guess, the code tries to figure out if it is in the word or not. If it is, it shows that letter wherever applicable and continues to replace the other letters with dashes. If they guess wrong, the failed counter goes up and the array prints out as many outputs as is applicable. 

```
while turns > 0:
    failed = 0 
    for char in word:
        if char in guesses: 
            print (char)
	    
        else:
            print ("_")
            failed += 1 
```

The following excerpt will clarify what exactly a guess is: an input from the player. 

```
    guess = input() # ask the user to guess a character
    guesses += guess # set the player's guess to guesses
```

If the player runs out of turns (a.k.a the hangman runs through), it ends. If they get it before they do, they win!

```
if turns == 0:
            print ("You lost :(")
```
```
if failed == 0:
	print ("You won")
        break
```

### LED Blink

#### Objective

In this assignment, I connected my Raspberry Pi to a breadboard using a t-cobbler and made two LED lights blink. 

### Methodology/Lessons

The code for the assignment was relatively simple; however, it was a little different than what I was used to. I found a great [GPIO pinout](https://pinout.xyz/) that explained what each pin was and how to wire things to them. I also found out that if you just type 

```
pinout
```

into your terminal, the Pi will give you one. Just like on an Arduino or the boards we used last year, there are pins for general use, VCC, Ground, PWM and more. The GPIO pins don't match up perfectly to the chronological number of the pin it's on (e.g. GPIO 17 is on the 11th pin); however, this diagram really explains it well. I found out from this [site](https://www.tunnelsup.com/raspberry-pi-zero-blink-an-led-using-gpio-pins/) that if you used GPIO 17 for your pin, that's the number you'd put in the code. Here's what mine looked like. 

```
led1 = LED(17)
led2 = LED(22)
```

Before that, I had to introduce GPIO and sleep. This is what that looked like. 

```
from gpiozero import LED
from time import sleep
```

I used a while True loop and from there, I set one to blink on while the other blinked off and vice versa.

```
while True:
	led1.on()
	sleep(0.5)
	led1.off()
	sleep(0.5)
	led2.on()
	sleep(0.5)
	led2.off()
	sleep(0.5)
```

The t-cobbler was really interesting; I'd never seen anything like it before. It connected to the pins on the Raspberry Pi and had an attachment on the end with corresponding pins that you attach to the breadboard, straddling the middle line. The pins on the attachment and on the Pi were connected by wires on the t-cobbler. The first time I made the LED light up, it was a little difficult to wire because I had to connect the LED to the breadboard which went straight to the Pi. This meant that I had to use male/female wires and meticulously count each pin to make sure that I didn't hook something up wrong. The t-cobbler attachment clearly labels each pin and you can connect the wires directly to the breadboard, which is a lot easier than trying to count to the 11th or 32nd pin on the Pi. 

I then hooked up a power boost to a battery, then to the Pi. This enabled me to run code on the Pi without hooking it up the computer. However, first, I had to find the IP address. I used 

```
ifconfig
```
while the Pi was still plugged in. However, it didn't give me an IP address that I could see, so I tried

```
hostname -I
```

instead. This was a little better and it gave me a pretty clear IP address but when I tried to use it on Putty, it didn't work. Dr. Shields helped me fix the problem by enabling SSH capabilities on the Pi and it worked from there! I clicked the SSH button in the Putty setup instead of the Serial and put in the IP address. I left it as the default port number and it worked perfectly! At this point, I had two Putty windows open: the one that was connected to the IP address and the one that I used to get the IP address, the one that the Pi was physically plugged into. After I hooked the Pi onto the booster and the battery, I unplugged it from the computer and ran the code on the other window. The LED lit up with no problem. 
