import RPi.GPIO as GPIO
import time

LED = 8
Switch = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED, GPIO.OUT)

  try:
    while True:
      if GPIO.input(Switch) == GPIO.HIGH:
        print("LED ON!")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
      else:
        print("LED OFF!")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   

if __name__ == '__main__':
    main()
