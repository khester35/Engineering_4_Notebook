# LED light blink
# Kaymin Hester

from gpiozero import LED
from time import sleep

led = LED(17) #the pin #

while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)
