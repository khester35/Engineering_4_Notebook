import time

import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# Initialize library.
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

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 120
top = 0 # top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Draw an ellipse.
# draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
# x += shape_width+padding

# Draw a rectangle.
# draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
# x += shape_width+padding
# Draw a triangle.
# draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], $
# x += shape_width+padding

# Draw an X.
# draw.line((x, bottom, x+shape_width, top), fill=255)
# draw.line((x, top, x+shape_width, bottom), fill=255)
# x += shape_width+padding

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same d$
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)

draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.image(image)
disp.display()

accel, mag = lsm303.read()
accel_x, accel_y, accel_z = accel
mag_x, mag_y, mag_z = mag

# draw.text((x, top), "Accel X={0}".format(accel_x), font=font, fill=255)

# Display image
# disp.image(image)
# disp.display()
# time.sleep(1)
# draw.rectangle((0,0,width,height), outline=0, fill=0)

# Display image.
# disp.image(image)
# disp.display()

perc = 0

draw.rectangle((x, top, x+shape_width, (height-2)*perc), outline=255, fill=0)

disp.image(image)
disp.display()

while True:
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag

	percx = accel_x/1138
	percy = accel_y/1138

#	draw.text((x, top), "Accel X={0}".format(max), font=font, fill=255)
	draw.rectangle((x, height, (x+shape_width)*percy, height-(height-2)*percx), outline=255, fill=255)

	disp.image(image)
	disp.display()

	time.sleep(0.1)

	draw.rectangle((0,0,width,height), outline=0, fill=0)

	disp.image(image)
	disp.display()

	time.sleep(0.0000001)

