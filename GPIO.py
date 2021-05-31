import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

LED = 12
Switch = 10

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

def main():
  
  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  while True: 
    # GPIO.input(Switch)와 GPIO.HIGH를 AND 연산으로 변경 가능
    if GPIO.input(Switch) == GPIO.HIGH:
      print("Button was pushed!")
      time.sleep(0.5)
    else:
      print("Button was not pushed!") 
      time.sleep(0.5)

if __name__ == '__main__':
    main()
