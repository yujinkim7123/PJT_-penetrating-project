import board
import digitalio
import adafruit_ssd1306
import time
import RPi.GPIO as GPIO

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D24)
# Change these to the right size for your display!
WIDTH = 128
HEIGHT = 64
# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D8)
oled_dc = digitalio.DigitalInOut(board.D25)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

#Clear display.
oled.fill(0)
oled.show()


# Create PIL image
from PIL import Image,ImageDraw, ImageFont
from datetime import datetime

#image = Image.open('./catImage.ppm').convert('1')
## 1 is black and withe mode

check = 0

def swithch(channel):
	global check
	print(check)
	if check ==0:
		check = 1
	else:
		check = 0

	time.sleep(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(12, GPIO.RISING, callback=swithch, bouncetime=500)


while 1:

	if check == 0:
		now = datetime.now()
		nowday = str(now.hour) + ":" + str(now.minute)  
		image = Image.new('1', (128,64),0)
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('malgun.ttf', 12)
		draw.text((40,10), "현재시각:" , font=font, fill=1)
		draw.text((50,25), nowday, font=font, fill = 1) 
		time.sleep(0.1)
		oled.image(image)
		oled.show()

	else :
		now = datetime.now()
		nowday = str(now.month) + ":" + str(now.day)
		image = Image.new('1', (128,64),0)
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('malgun.ttf', 12)
		draw.text((40,10), "현재날짜:" , font=font, fill=1)
		draw.text((50,25), nowday, font=font, fill = 1)
		time.sleep(0.1)
		oled.image(image)
		oled.show()
	time.sleep(0.1)
#draw.line((0,0,128,64), fill=1)
#draw.line((0,image.size[1], image.size[0], 0), fill=1)
#draw.ellipse((30,30,50,50), fill=0)
#draw.rectangle((10,10,118,64), fill=1)

#box = (0,0,50,50)
#regin = image.crop(box)

#regin = regin.transpose(Image.ROTATE_180)
#image.paste(regin, box)

# Display image
oled.image(image)
oled.show()
