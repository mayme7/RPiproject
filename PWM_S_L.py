import RPi.GPIO as GPIO
import I2C_driver as LCD
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Switch = 10
LED = 12
mylcd = LCD.lcd()

def main():
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

  PWM_LED= GPIO.PWM(LED, 50)
  PWM_LED.start(0)

  try:
    while True:
      #for duty in range(100):
        #PWM_LED.ChangeDutyCycle(duty)
        #print(PWM_LED)
        #time.sleep(0.5)
        
      if GPIO.input(Switch) == GPIO.HIGH:
        print("Switch Push")
        mylcd.lcd_display_string("Switch Push!",1)
        PWM_LED = PWM_LED + 50
        print(GPIO.PWM)
        time.sleep(0.5)
        
      else:
        print("Switch didn't push")
        mylcd.lcd_display_string("Switch didn't push!",1)
        print(GPIO.PWM)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
  main()
    
