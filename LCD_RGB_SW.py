import RPi.GPIO as GPIO
import I2C_driver as LCD
import time

Switch_G = 10
#Switch_B = 15
#Switch_R = 22
LED_G = 12
#LED_B = 16
#LED_R = 18
mylcd = LCD.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def main():
  GPIO.setup(Switch_G, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED_G, GPIO.OUT, initial=GPIO.LOW)
  #GPIO.setup(Switch_B, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  #GPIO.setup(LED_B, GPIO.OUT, initial=GPIO.LOW)
  #GPIO.setup(Switch_R, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  #GPIO.setup(LED_R, GPIO.OUT, initial=GPIO.LOW)

  try:
    while True:
      if GPIO.input(Switch_G) == GPIO.HIGH: #elif copy
        print("LED ON!")
        mylcd.lcd_display_string("Green LED ON!",1)
        GPIO.output(LED_G, GPIO.HIGH)
        time.sleep(0.5)
      elif GPIO.input(Switch_G) == GPIO.LOW::
        print("LED OFF!")
        mylcd.lcd_display_string("Green LED OFF!",1)
        GPIO.output(LED_G, GPIO.LOW)
        time.sleep(0.5)
                    
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
    main()
