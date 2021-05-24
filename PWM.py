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
        Duty= input()
        duty= int(Duty)
        PWM_LED.ChangeDutyCycle(duty)

if __name__ == '__main__':
    main()
