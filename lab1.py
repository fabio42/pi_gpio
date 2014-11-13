import RPi.GPIO as GPIO ## Import GPIO library
import sys
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

GPIO.output(7,False) ## Turn on GPIO pin 7
raw_input("Where is the light ???????...")

GPIO.output(7,True) ## Turn on GPIO pin 7
raw_input("It's better when it's all black !...")
GPIO.output(7,False) ## Turn on GPIO pin 7

GPIO.cleanup()
