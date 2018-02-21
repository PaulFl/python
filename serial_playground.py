import serial
import time

ser = serial.Serial(port = "/dev/arduino", timeout = 0)
serLine =  ''

def interpretLine(line):
    print("id="+str(line[0]))
    print("value="+str(line[1:]))

while True:
    if ser.inWaiting()>0:
        line = ser.read(ser.inWaiting()).decode()
        while line.find('\n') != -1:
            i = line.find('\n')
            serLine += line[:i]
            interpretLine(line)
            serLine = ''
            line = line[i+1:]
    time.sleep(0.2)
