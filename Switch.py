import RPi.GPIO as GPIO
import time

Switch = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  while True:
    if GPIO.input(Switch) == GPIO.HIGH:
      print("Button was pushed!")
      time.sleep(0.5)
    else:
      print("Button was not pushed!")
      time.sleep(0.5)

if __name__ == '__main__':
    main()
