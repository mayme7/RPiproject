import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Switch = 10
LED = 12

def main():
  #GPIO.setup(LED, GPIO.OUT)
  GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

  PWM_LED= GPIO.PWM(LED, 50)
  PWM_LED.start(0)

  try:
    while 1:
      for duty in range(100):
        PWM_LED.ChangeDutyCycle(duty)
        print(PWM_LED)
        time.sleep(0.5)
        
      if GPIO.input(Switch) == GPIO.HIGH:
        print("Switch Push")
        PWM_LED = PWM_LED + 50
        print(PWM_LED)
        time.sleep(0.5)
        
      else:
        print("Switch didn't push")
        print(PWM_LED)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
  main()
    
