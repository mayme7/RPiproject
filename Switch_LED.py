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
        GPIO.output(LED, GPIO.HIGH)
        print("LED ON!")
        time.sleep(0.5)
      else:
        GPIO.output(LED, GPIO.LOW)
        print("LED OFF!")
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   

if __name__ == '__main__':
    main()
