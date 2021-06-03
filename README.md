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

### GPIO Pins - Bash

#### Objective

In this assignment, I wrote a Bash script that made 2 LED lights blink 10 times. 

### Methodology/Lessons

I must admit: this assignment was harder than expected. I started out with 

```
gpio mode 0 out
gpio write 0 1
```
in the terminal. This sets 0 (pin 17) as an output and makes it High, so it'll light up. However, I couldn't figure out how to assign a value to my second LED, which was on pin 22. [This site](https://www.teknotut.com/en/first-raspberry-pi-project-blink-led/#Blink_Project) helped clear it up. In the terminal, I typed 

```
gpio -g mode 17 out 
gpio -g mode 22 out 
```

This set pins 17 and 22 as outputs. Then, I wrote 

```
gpio -1 write 11 1
gpio -1 write 15 1
```
which turned them both to High. Note that on the GPIO pinout, pin 17 is 11 and pin 22 is 15. Then, still in the terminal, I typed 

```
which gpio
```
This gave me

```
/usr/bin/gpio
```
I opened an .sh file and wrote a loop that made the LED on pin 17 blink. 

```
#!/bin/bash

while :
do
        /usr/bin/gpio -1 toggle 11
        sleep 1
done
```
I learned that toggle switches it to an opposite condition. So, because I set it to High, it switches to Low, therefore blinking the light on and off. In order to make it blink a set amount of times (in this assignment, I did it 10 times), I used [this site](https://stackoverflow.com/questions/11176284/time-condition-loop-in-shell), which exits the loop after a specific amount of time. Because the blinks are so closely correlated with the time (on for 1 second, off for 1 second), I let the LED blink for 20 seconds and it blinks 10 times. I also added in the second LED. 

```
end=$((SECONDS+20)) # SECONDS = # of seconds elapsed so far in a script

while [ $SECONDS -lt $end ];
do
	/usr/bin/gpio -1 toggle 11 # toggle = switch to opposite condition
	/usr/bin/gpio -1 toggle 15 # ex. if set to Low, will switch to High
	sleep 1
done
```

### GPIO Pins - I2C

#### Objective

In this assignment, I made an OLED screen display X, Y, and Z acceleration values that were measured by my accelerometer. 

#### Methodology/Lesson

I quite literally put blood, sweat, and tears into this assignment. I started off with some practice on the OLED; I spent some time on some Adafruit code I copiped from their github, but it was old and didn't work very well. So, I copied the shapes.py document (this [terminal cheatsheet](https://learn.adafruit.com/an-illustrated-shell-command-primer/moving-and-copying-files-mv-and-cp) really came in handy) and took out the shapes, just messing around with the text. I decided to comment out the lines I didn't need instead of deleting them, just so I'd have them if I ever needed to go back and take a look at them. First, I familiarized myself with the syntax for printing text on the OLED. 

```
draw.text((x, top),   'Hello, ',   font=font, fill=255)
draw.text((x, top+20),   'World',   font=font, fill=255)
```
This prints Hello, World on the OLED. The first word is at the top of the screen (as indicated by top) and the second is about a third of the way down (as indicated by top+20). I think that the max value is 64 pixels. That turned out to be something I struggled with later on, so this practice turned out to be really useful because I could rule out potential causes of my problem. When I started the assignment, I began by scanning simpletest.py and pasting all of the important parts into my copied document. 

```
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24

lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)
```
This is what it looked like. Then, I learned about different display commands that are important to use when working with the OLED. 

```
# Initialize library
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
```
All of the comments are pretty self explanatory and I just kept them from when I copied the shapes.py code, so I really appreciated how detailed they were. It took me a while to figure this out, but I learned that when you're trying to wipe a screen, you can't just write

```
disp.clear()
```
because it doesn't actually create a black screen. It just wipes your image and when you call for any new image to come back, the old one will come back too. I finally figured out that in order to actually clear a screen so when you call the new image, that's the only one that shows up, you have to write:

```
draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.image(image)
disp.display()
```
When you do that, it creates a black screen, prints that image, then your new image will print on top of that. It's a little confusing at first, but it made a lot of sense when I put it into practical use! Next, I wrote:

```
draw.text((x, top+10),   'Printing accelerometer',   font=font, fill=255)
draw.text((x, top+20),   'r & magnetometer X, Y', font=font, fill=255)
draw.text((x, top+30),   'Z axis values', font=font, fill=255)
disp.image(image)
disp.display()

time.sleep(3)
```
This splits up a sentence into three different lines because I noticed that when I print them all in one, it just runs off the screen. After it prints that, it pauses for three seconds and then it clears with the same lines I introduced before. At first, I had it print in a while loop, but it started printing inputs on top of inputs, so I took it out and put the while loop after. Trying to get the accelerometer values to print was the most difficult part. When I printed 

```
  draw.text((x, top), "Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}".format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z), font=font, fill=255)
```
it worked fine. However, when I tried to split it up so they would print vertically, I ran into a problem. When I printed
```  
	draw.text((x, top), "Accel X={0}".format(accel_x), font=font, fill=255)
        draw.text((x, top+10), "Accel Y={1}".format(accel_y), font=font, fill=255)
```
I got an error telling me that the value I'd called for didn't exist. I finally realized that I was calling the values inside format() instead of inside the accel that I'd defined above the while loop in the lines

```
accel, mag = lsm303.read()
accel_x, accel_y, accel_z = accel
mag_x, mag_y, mag_z = mag
```
So, I wrote them all out like this:

```
  draw.text((x, top), "Accel X={0}".format(accel_x), font=font, fill=255)
        draw.text((x, top+10), "Accel Y={0}".format(accel_y), font=font, fill=255)
        draw.text((x, top+20), "Accel Z={0}".format(accel_z), font=font, fill=255)
        draw.text((x, top+30), "Mag X={0}".format(mag_x), font=font, fill=255)
        draw.text((x, top+40), "Mag Y={0}".format(mag_y), font=font, fill=255)
        draw.text((x, top+50), "Mag Z={0}".format(mag_z), font=font, fill=255)
```
and it worked perfectly!

### Hello Flask

#### Objective

In this assignment, I set up my Raspberry Pi as a web server.

#### Methodology/Lesson

This was pretty thoroughly explained in the Canvas assignment, but here's a picture of what the page looked like when I finished and tested it!

![Web Server](https://github.com/khester35/Engineering_4_Notebook/blob/master/Images/Hello%20World.PNG)

### Headless 

#### Objective

In this assignment we were to display the data from the accelerometer graphically and attach it to the battery, enabling it to operate away from the computer. 

#### Methodology/Lesson

My OLED screen shows the height of a box changing alongside the X value of the accelerometer's acceleration and the width changing with the Y. 

```
percx = accel_x/1138
percy = accel_y/1138

draw.rectangle((x, height, (x+shape_width)*percy, height-(height-2)*percx), outline=255, fill=255)
```

percx = accel_x/1138 divides the X value by the maximum value it can reach. This creates the percentage of x, which becomes the percentage of the rectangle that is shown. It works similarly with the Y values. I found the maximum value by having the OLED count up as the accelerometer values count up. When it stopped counting despite me still moving it up and around, I used that value as the maximum value. 

I wipe the screen every time the value changes so when the graph moves around, it's not images on top of images on top of images. 

```
draw.rectangle((x, height, (x+shape_width)*percy, height-(height-2)*percx), outline=255, fill=255)

disp.image(image)
disp.display()

time.sleep(0.1)

draw.rectangle((0,0,width,height), outline=0, fill=0)

disp.image(image)
disp.display()

time.sleep(0.0000001)
```
I then connected it to the battery, ran the code, and took a walk with the hardware in tow! It worked perfectly.

### GPIO - Flask 

#### Objective

In this assignment, we were to turn an LED light on over the Internet!

#### Methodology/Lesson

This assignment was fairly easy up to a certain point, given that the instructions provided code. However, I got a long error saying that my permissions were denied. First, I tried to change the code that previously read 

```
app.run(host="0.0.0.0", port=80)
```
to read 

```
app.run(host="10.0.0.248", port=22)
```
to match my IP address and my port #. I got the same response, so I looked up the error. It told me that my permissions weren't allowing me to access the file, so I tried a few commands in the terminal including 

```
chown app.py
```
and 

```
chmod 755 app.py
```
which went through easily, but didn't result in a different error. Next, I tried 

```
sudo python3 app.py
```
which told me that it was already in use. I tried a few other commands which didn't work, but what ultimately led to success was 

```
app.run(host="0.0.0.0", port=8080)
```
and 

```
sudo python3 app.py
```
Then, I went to my browser and searched 10.0.0.248:8080. After a quick tweak to my wiring, it worked!

### Pi Camera 

#### Objective

In this assignment, we were to make a camera take pictures in two ways: first, we had to print "running" while the camera was taking the picture and "done" when it was finished Second, we had to write a program that, when run, took five photos with five different effects. 

#### Methodology/Lesson

This lesson was definitely fun, but thanks to the [resources](https://picamera.readthedocs.io/en/release-1.10/recipes1.html) provided in the assignment, it wasn't too hard. The only issue I ran into was with the second assignment. I was a little confused on how to get each effect to apply to each different photo, but I figured that an array would work best. I used this: 

```
effects = ["negative", "solarize", "sketch", "oilpaint", "blur"]
```

to clarify which effects I wanted to use. Then, I used this: 

```
for i in range(len(effects)):
        camera.image_effect = effects[i]
```

to clarify where I wanted to apply them. I decided to write len(effects) instead of the number of inputs in the array because I didn't want to restrict it to five; I know that the assignment would have been fulfilled if I'd simply written the relevant number of effects in the array, but I wanted to make sure that it wouldn't malfunction if I decided to change the number of effects I used. In order to make it neat and pretty, I had it print "running" while it was running and used this: 

```
nme = input("enter file name:\n")
```

and later, this: 

```
 camera.capture(nme + effects[i] + ".jpg")
        print("done")
        print("file saved as: "+nme + effects[i] + ".jpg\n")
```

so it would name each file something unique and state the saved file at the end! 
