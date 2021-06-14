import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED = 12

GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100) # pin 14 at 100 Hz
value = 0
pwm.start(value) # Start at 0

increment = 2 #smooth is the fade
#sleeptime = 0.3 # fast is the fade

try:
 while True: 
  value += increment
 
  if value > 100:
   value = 0
  pwm.ChangeDutyCycle(value)
  time.sleep(0.3)

except KeyboardInterrupt:
 pwm.stop()
 GPIO.cleanup()

if __name__ == '__main__':
  main()
