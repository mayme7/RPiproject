# smbus library
import smbus
import RPi.GPIO as GPIO
import I2C_driver as LCD

from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)
device.contrast(5)
virtual = viewport(device, width=32, height=16)

show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

bus = smbus.SMBus(1)

# IC address
address = 0x53

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

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

def main():
    print(bus)
    init_ADXL345()
    mylcd = LCD.lcd()
    while 1:
        num = input()
        if num == '1':
            x_acc = measure_acc(x_adr)
            y_acc = measure_acc(y_adr)
            z_acc = measure_acc(z_adr)
            
            print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
            mylcd.lcd_clear()
            
        elif num == '2':
            mylcd.lcd_display_string("Input2",1)
            mylcd.lcd_display_string("Input2",2)
            
        
        elif num == '3':
            with canvas(virtual) as draw:
            #text(draw, (0, 1), "Idris", fill="white", font=proportional(CP437_FONT))
            text(draw, (0, 1), datetime.now().strftime('%I:%M'), fill="white", font=proportional(CP437_FONT))
        
        
if __name__ == '__main__':
    main()
    
