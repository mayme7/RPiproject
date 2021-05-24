import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 12



def main():
    GPIO.setup(LED, GPIO.OUT)

    PWM_LED= GPIO.PWM(LED, 50)
    PWM_LED.start(0)

    while 1:
        for duty in range(100):
            PWM_LED.ChangeDutyCycle(duty)
            time.sleep(0.5)

if __name__ == '__main__':
    main()
