import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 16

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(LED, GPIO.HIGH)
time.sleep(1)
