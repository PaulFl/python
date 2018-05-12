import serial
import time

ser = serial.Serial(port = "/dev/arduino", timeout = 0)
serLine =  ''

def interpretLine(line):
    if(line[0] != '\n'):
        id = int(line[0])
        if(line[1:]!='\n'):
            value=int(line[1:])
            print("id="+str(id))
            print("value="+str(value))

while True:
    if ser.inWaiting()>0:
        line = ser.read(ser.inWaiting()).decode()
        while line.find('\n') != -1:
            i = line.find('\n')
            serLine += line[:i-1]
            interpretLine(serLine)
            serLine = ''
            line = line[i+1:]
    time.sleep(0.2)
