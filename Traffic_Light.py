import RPi.GPIO as GPIO
import time

Switch = 10
LED_G = 12
LED_B = 16
LED_R = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

  try:
    while True:
      if GPIO.input(Switch) == GPIO.HIGH:
        print("LED ON!")
        GPIO.output(LED_G, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(LED_G, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_R, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_R, GPIO.LOW)
        time.sleep(0.5)

      else:
        print("LED OFF!")
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        GPIO.output(LED_R, GPIO.LOW)
        time.sleep(0.5)
        
  finally:
    GPIO.cleanup()
   
if __name__ == '__main__':
    main()
