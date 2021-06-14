import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100) # pin 14 at 100 Hz
value = 0
pwm.start(value) # Start at 0

increment = 2 #smooth is the fade
sleeptime = .03 # fast is the fade

try:
 while True: 
  value += increment
 
  if value > 100:
   value = 0
  pwm.ChangeDutyCycle(value)
  sleep(sleeptime)

except KeyboardInterrupt:
 pwm.stop()
 GPIO.cleanup()
