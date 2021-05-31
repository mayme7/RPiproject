import RPi.GPIO as GPIO
import time

LED = 12
Switch = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

  while True:
    if GPIO.input(Switch) == GPIO.HIGH:
      print("Button was pushed!")
      GPIO.output(LED, GPIO.HIGH)
      time.sleep(0.5)
    else:
      print("Button was not pushed!")
      GPIO.output(LED, GPIO.LOW)
      time.sleep(0.5)

if __name__ == '__main__':
    main()
