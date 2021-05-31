import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 10

def main():
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
    try:
        while 1:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)

            GPIO.output(LED, GPIO.LOW)
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    
    finally:
        GPIO.cleanup()

if __name__=='__main__':
    main()
