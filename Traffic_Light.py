import RPi.GPIO as GPIO
import time

Switch = 10
LED_G = 12
LED_B = 16
LED_R = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

  try:
    while 1:
        print("Green LED ON!")
        GPIO.output(LED_G, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(LED_G, GPIO.LOW)
        time.sleep(0.5)
        print("Blue LED ON!")
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
        print("Red LED ON!")
        GPIO.output(LED_R, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_R, GPIO.LOW)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
    main()
