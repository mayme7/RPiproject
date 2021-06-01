import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

LED1 = 10
LED2 = 12

def main():
    GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
    
    try:
        while 1:
            GPIO.output(LED1, GPIO.HIGH)
            GPIO.output(LED2, GPIO.LOW)
            time.sleep(1)

            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.HIGH)
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    
    finally:
        GPIO.cleanup()

if __name__=='__main__':
    main()
