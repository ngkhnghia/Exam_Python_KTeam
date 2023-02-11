import time
import RPi.GPIO as GPIO

interruptPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(interruptPin, GPIO.IN)

def interruptCallback(interruptPin):
	print('Interrupt.')

try:
	GPIO.add_event_detect(interruptPin, GPIO.RISING, callback=interruptCallback)

	while 1:
		time.sleep(10000)

except KeyboardInterrupt:
	print('Quit')
	GPIO.cleanup()