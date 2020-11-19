# Two LED lights blink alternately
# Kaymin Hester

from gpiozero import LED
from time import sleep

led1 = LED(17) #the pin #
led2 = LED(22) #the second pin #

while True:
	led1.on()
	sleep(0.5)
	led1.off()
	sleep(0.5)
	led2.on()
	sleep(0.5)
	led2.off()
	sleep(0.5)

