import RPi.GPIO as GPIO
import I2C_driver as LCD
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Switch = 10
LED = 12
mylcd = LCD.lcd()

GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


def main(light, p):
    p.ChangeDutyCycle(light)

try:
    p1 = GPIO.PWM(LED, 100)
    p1.start(0)

    while 1:
        if GPIO.input(Switch) == GPIO.HIGH:
            print("Switch Push")
            mylcd.lcd_display_string("Switch Push!", 1)
            time.sleep(0.5)

            for i in range(10):
                GPIO.output(LED, True)
                p1.ChangeDutyCycle(i * 10)
                main(i * 10, p1)
                time.sleep(0.5)

            print("%.2f" % (p1))
            time.sleep(0.5)
            mylcd.lcd_clear()

        else:
            print("Switch didn't push")
            mylcd.lcd_display_string("Switch didn't push!", 1)
            time.sleep(0.5)

            for j in range(10, -1, -1):
                p1.start(100)
                GPIO.output(LED, True)
                p1.ChangeDutyCycle(j * 10)
                main(j * 10, p1)
                time.sleep(0.5)

            print("%.2f" % (p1))
            time.sleep(0.5)
            mylcd.lcd_clear()

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

if __name__ == '__main__':
    main(light, p)

