# smbus library
import smbus
import RPi.GPIO as GPIO
import I2C_driver as LCD
import luma.led_matrix as examples
import time
import re
import time
import argparse
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

bus = smbus.SMBus(1)

# IC address
address = 0x53

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

mylcd = LCD.lcd()

# ADXL345 init
def init_ADXL345():
    print('ADXL345 init function')
    bus.write_byte_data(address, 0x2D, 0x08)

# data measure
def measure_acc(adr):
    acc0 = bus.read_byte_data(address, adr)

    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0

    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    acc = acc * 3.9 / 1000

    return acc

# dot matrix
def demo(n, block_orientation, rotate, inreverse):
    print(bus)
    init_ADXL345()
    
    while 1:
        num = input()
        if num == '1':
            print("1")
            mylcd.lcd_display_string("LCD OUTPUT1", 1)
            mylcd.lcd_display_string("LCD OUTPUT2", 2)
            mylcd.lcd_clear() 
            
        elif num == '2':  # 01234 5
            print("2")
            x_acc = measure_acc(x_adr)
            y_acc = measure_acc(y_adr)
            z_acc = measure_acc(z_adr)

            print('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
            mylcd.lcd_clear()    
            
        elif num == '3':  # LCD Dot Matrix
            print("3")
            mylcd.lcd_display_string("LCD OUTPUT1", 1)
            mylcd.lcd_display_string("LCD OUTPUT2", 2)    
            
            # create matrix device
            serial = spi(port=0, device=0, gpio=noop())
            device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                             rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
            print("Created device")

            # start demo
            msg = "dot matrix OUTPUT!"
            print(msg)
            show_message(device, msg, fill="white", font=proportional(CP437_FONT))
            time.sleep(1)

            show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0)
            time.sleep(1)

            show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.1)

            # words= ['0','1','2','3','4','5','6','7','8','9']
            words = ['O', 'X']
            virtual = viewport(device, width=device.width, height=len(words) * 8)
            with canvas(virtual) as draw:
                for i, word in enumerate(words):
                    text(draw, (0, i * 8), word, fill="white", font=proportional(CP437_FONT))
                    time.sleep(0.1)

            for i in range(virtual.height - device.height):
                virtual.set_position((0, i))
                time.sleep(0.1)

            show_message(device, msg, fill="white")

            time.sleep(0.5)

            print('Canvas')
            for i in words:
                print(i, type(i))
                with canvas(device) as draw:
                    # text(draw, (0, 0), "A", fill="white")
                    text(draw, (0, 0), i, fill="white")

                time.sleep(0.1)

                for _ in range(5):
                    for intensity in range(16):
                        device.contrast(intensity * 16)
                        time.sleep(0.5)

            device.contrast(0x80)
            time.sleep(1)

            show_message(device, msg, fill="white", font=SINCLAIR_FONT)

            time.sleep(1)
            show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))

            time.sleep(1)
            show_message(device, msg, fill="white", font=proportional(TINY_FONT))

            time.sleep(1)
            show_message(device, msg)

            time.sleep(1)
            for x in range(256):
                with canvas(device) as draw:
                    text(draw, (0, 0), chr(x), fill="white")
                    time.sleep(0.1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90],
                        help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3],
                        help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()
