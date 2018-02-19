import serial

ser = serial.Serial('/dev/ttyUSB0', timeout = 0)

while True:
	if (ser.inWaiting() > 3):
		line = ser.read(ser.inWaiting()).decode()
		id = int(line[0])
		print(id)
		state = bool(int(line[1]))
		print(state)
		print(line)

ser.close()
