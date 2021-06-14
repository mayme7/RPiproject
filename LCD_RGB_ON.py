import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *

LED_G = 12
LED_B = 16
LED_R = 18
mylcd = LCD.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(LED_B, GPIO.OUT, initial=GPIO.LOW)
  GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)

  try:
    while 1:
        print("Green LED ON!")
        mylcd.lcd_display_string("Green LED ON!",1)
        GPIO.output(LED_G, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(LED_G, GPIO.LOW)
        time.sleep(0.5)
        print("Blue LED ON!")
        mylcd.lcd_display_string("Blue LED ON!",1)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
        print("Red LED ON!")
        mylcd.lcd_display_string("Red LED ON!",1)
        GPIO.output(LED_R, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_R, GPIO.LOW)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
