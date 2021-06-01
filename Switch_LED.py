import RPi.GPIO as GPIO
import time

Switch = 15
LED = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def main():
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED, GPIO.OUT)

  try:
    while True:
      if GPIO.input(Switch) == GPIO.HIGH:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
      else:
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
    main()
