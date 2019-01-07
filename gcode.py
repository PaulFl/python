import serial
import time

ser = serial.Serial('/dev/tty0', baudrate=115200)

#time.sleep(2)

ser.write(b'G28 X\n')

ser.close()