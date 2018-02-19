#!/usr/bin/python3

import tkinter as tk
import time
import serial

ser = serial.Serial(port='/dev/ttyUSB0', timeout = 0)

time1 = ''

desktopState = True
mgState = True
ledState = True
doorLedState = True
doorState = True
v12State = True

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clockDisplay.config(text=time2)
    clockDisplay.after(200, tick)

    
def readSerial():
    if (ser.inWaiting() > 3):
        line = ser.read(ser.inWaiting()).decode()
        id = int(line[0])
        state = bool(int(line[1]))
        setDevice(id, state)
    clockDisplay.after(100, readSerial)
    
def setDevice(id, state):
    if id == 1:
        global desktopState
        desktopState = state
        for widget in [desktop, desktopSwitch, desktopStatus, desktopLabel]:
            if desktopState:
                widget.config(bg = 'green')
            else:
                widget.config(bg = 'red')
        if desktopState:
            desktopSwitch.config(text = 'OFF')
            desktopStatus.config(text = 'ON', fg = 'black')
            desktopLabel.config(fg = 'black')
        else:
            desktopSwitch.config(text='ON')
            desktopStatus.config(text = 'OFF', fg = 'white')
            desktopLabel.config(fg = 'white')
    elif id == 2:
        global mgState
        mgState = state
        for widget in [mg, mgSwitch, mgStatus, mgLabel]:
            if mgState:
                widget.config(bg = 'green')
            else:
                widget.config(bg = 'red')
        if mgState:
            mgSwitch.config(text = 'OFF')
            mgStatus.config(text = 'ON', fg = 'black')
            mgLabel.config(fg = 'black')
        else:
            mgSwitch.config(text='ON')
            mgStatus.config(text = 'OFF', fg = 'white')
            mgLabel.config(fg = 'white')
    elif id == 3:
        global ledState
        ledState = state
        for widget in [led, ledSwitch, ledStatus, ledLabel]:
            if ledState:
                widget.config(bg = 'green')
            else:
                widget.config(bg = 'red')
        if ledState:
            ledSwitch.config(text='OFF')
            ledStatus.config(text = 'ON', fg = 'black')
            ledLabel.config(fg = 'black')
        else:
            ledSwitch.config(text='ON')
            ledStatus.config(text = 'OFF', fg = 'white')
            ledLabel.config(fg = 'white')
    elif id == 4:
        global v12State
        v12State = state
        for widget in [v12, v12Switch, v12Status, v12Label]:
            if v12State:
                widget.config(bg = 'green')
            else:
                widget.config(bg = 'red')
        if v12State:
            v12Switch.config(text='OFF')
            v12Status.config(text = 'ON', fg = 'black')
            v12Label.config(fg = 'black')
        else:
            v12Switch.config(text='ON')
            v12Status.config(text = 'OFF', fg = 'white')
            v12Label.config(fg = 'white')

def writeSerial(line):
    ser.write((line + '\n').encode('utf-8'))

def switchV12():
    global v12State
    v12State = not v12State
    for widget in [v12, v12Switch, v12Status, v12Label]:
        if v12State:
            widget.config(bg = 'green')
        else:
            widget.config(bg = 'red')
    if v12State:
        v12Switch.config(text='OFF')
        v12Status.config(text = 'ON', fg = 'black')
        v12Label.config(fg = 'black')
        writeSerial('41')
    else:
        v12Switch.config(text='ON')
        v12Status.config(text = 'OFF', fg = 'white')
        v12Label.config(fg = 'white')
        writeSerial('40')

def switchDesktop():
    global desktopState
    desktopState = not desktopState
    for widget in [desktop, desktopSwitch, desktopStatus, desktopLabel]:
        if desktopState:
            widget.config(bg = 'green')
        else:
            widget.config(bg = 'red')
    if desktopState:
        desktopSwitch.config(text='OFF')
        desktopStatus.config(text = 'ON', fg = 'black')
        desktopLabel.config(fg = 'black')
        writeSerial('11')
    else:
        desktopSwitch.config(text='ON')
        desktopStatus.config(text = 'OFF', fg = 'white')
        desktopLabel.config(fg = 'white')
        writeSerial('10')
    
def switchMg():
    global mgState
    mgState = not mgState
    for widget in [mg, mgSwitch, mgStatus, mgLabel]:
        if mgState:
            widget.config(bg = 'green')
        else:
            widget.config(bg = 'red')
    if mgState:
        mgSwitch.config(text='OFF')
        mgStatus.config(text = 'ON', fg = 'black')
        mgLabel.config(fg = 'black')
        writeSerial('21')
    else:
        mgSwitch.config(text='ON')
        mgStatus.config(text = 'OFF', fg = 'white')
        mgLabel.config(fg = 'white')
        writeSerial('20')

def switchLed():
    global ledState
    ledState = not ledState
    for widget in [led, ledSwitch, ledStatus, ledLabel]:
        if ledState:
            widget.config(bg = 'green')
        else:
            widget.config(bg = 'red')
    if ledState:
        ledSwitch.config(text='OFF')
        ledStatus.config(text = 'ON', fg = 'black')
        ledLabel.config(fg = 'black')
        writeSerial('31')
    else:
        ledSwitch.config(text='ON')
        ledStatus.config(text = 'OFF', fg = 'white')
        ledLabel.config(fg = 'white')
        writeSerial('30')

def switchDoorLed():
    global doorLedState
    doorLedState = not doorLedState
    for widget in (doorLed, doorLedSwitch, doorLedStatus, doorLedLabel):
        if doorLedState:
            widget.config(bg = 'green')
        else:
            widget.config(bg = 'red')
    if doorLedState:
        doorLedSwitch.config(text = 'OFF')
        doorLedStatus.config(text = 'ON', fg = 'black')
        doorLedLabel.config(fg = 'black')
    else:
        doorLedSwitch.config(text = 'ON')
        doorLedStatus.config(text = 'OFF', fg = 'white')
        doorLedLabel.config(fg = 'white')

window = tk.Tk()
window.title("Control Center")

pwindow = tk.PanedWindow(window, orient='horizontal')

lights = tk.Frame(window)
pwindow.add(lights,stretch="always")

sensors = tk.Frame(window)
pwindow.add(sensors, stretch = 'always')

clock = tk.Frame(window)
pwindow.add(clock)

lightsLabel = tk.Label(lights, text = 'Outputs', font=('Arial', 50))
lightsLabel.pack(fill='both', expand = False)

sensorsLabel = tk.Label(sensors, text = 'Sensors', font=('Arial', 50))
sensorsLabel.pack(fill = 'both', expand = False)

clockLabel = tk.Label(clock, text = 'Clock', font=('Arial', 50))
clockLabel.pack(fill = 'both', expand = False)

v12 = tk.Frame(lights, bg = 'green')
v12.pack(fill='both', expand = True)

v12Label = tk.Label(v12, text = "12V Output", bg = 'green')
v12Label.pack(fill='both', expand = True)

v12Status = tk.Label(v12, text = 'ON', bg = 'green')
v12Status.pack(fill='both', expand = True)

v12Switch = tk.Button(v12, text = 'OFF', bg = 'green', command=switchV12)
v12Switch.pack(fill='both', expand = True)


desktop = tk.Frame(lights, bg = 'green')
desktop.pack(fill='both', expand = True)

desktopLabel = tk.Label(desktop, text = "Desktop", bg = 'green')
desktopLabel.pack(fill='both', expand = True)

desktopStatus = tk.Label(desktop, text = 'ON', bg = 'green')
desktopStatus.pack(fill='both', expand = True)

desktopSwitch = tk.Button(desktop, text = 'OFF', bg = 'green', command=switchDesktop)
desktopSwitch.pack(fill='both', expand = True)

mg = tk.Frame(lights, bg = 'green')
mg.pack(fill='both', expand = True)
mgLabel = tk.Label(mg, text = "Magnifying glass", bg = 'green')
mgLabel.pack(fill='both', expand = True)

mgStatus = tk.Label(mg, text = 'ON', bg = 'green')
mgStatus.pack(fill='both', expand = True)

mgSwitch = tk.Button(mg, text = 'OFF', bg = 'green', command=switchMg)
mgSwitch.pack(fill='both', expand = True)

led = tk.Frame(lights, bg = 'green')
led.pack(fill='both', expand = True)

ledLabel = tk.Label(led, text = "LEDs", bg = 'green')
ledLabel.pack(fill='both', expand = True)

ledStatus = tk.Label(led, text = 'ON', bg = 'green')
ledStatus.pack(fill='both', expand = True)

ledSliders = tk.Frame(led, bg = 'green')
ledSliders.pack(fill = 'both', expand = True)

redValue = tk.DoubleVar()
ledRedSlider = tk.Scale(ledSliders, variable = redValue, bg = 'red')
ledRedSlider.config(from_ = 255, to = 0)
ledRedSlider.pack(side = 'left', fill = 'both', expand = True)

greenValue = tk.DoubleVar()
ledGreenSlider = tk.Scale(ledSliders, variable = greenValue, bg = 'green')
ledGreenSlider.config(from_ = 255, to = 0)
ledGreenSlider.pack(side = 'left', fill = 'both', expand = True)

blueValue = tk.DoubleVar()
ledBlueSlider = tk.Scale(ledSliders, variable = blueValue, bg = 'blue')
ledBlueSlider.config(from_ = 255, to = 0)
ledBlueSlider.pack(side = 'left', fill = 'both', expand = True)


ledSwitch = tk.Button(led, text = 'OFF', bg = 'green', command=switchLed)
ledSwitch.pack(fill='both', expand = True)

doorLed = tk.Frame(lights, bg = "green")
doorLed.pack(fill = 'both', expand = True)

doorLedLabel = tk.Label(doorLed, text = "Door LED", bg = 'green')
doorLedLabel.pack(fill = 'both', expand = True)

doorLedStatus = tk.Label(doorLed, text = 'ON', bg = 'green')
doorLedStatus.pack(fill = 'both', expand = True)

doorLedSwitch = tk.Button(doorLed, text = 'OFF', bg = 'green', command=switchDoorLed)
doorLedSwitch.pack(fill = 'both', expand = True)


clockDisplay = tk.Label(clock, font=('Arial', 60), fg = 'white', bg = 'black')
clockDisplay.pack(fill='both', expand= True)

doorPosition = tk.Frame(sensors, bg = 'green')
doorPosition.pack(fill = 'both', expand = True)

doorPositionLabel = tk.Label(doorPosition, text = "Door status", bg = 'green')
doorPositionLabel.pack(fill = 'both', expand = True)

doorPositionStatus = tk.Label(doorPosition, text = 'OPEN', bg = 'green')
doorPositionStatus.pack(fill = 'both', expand = True)

canStatus = tk.Frame(sensors, bg = 'red')
canStatus.pack(fill = 'both', expand = True)

canStatusLabel = tk.Label(canStatus, text = "Can status", bg = 'red', fg = 'white')
canStatusLabel.pack(fill = 'both', expand = True)

canStatusValue = tk.Label(canStatus, text = 'NULL', bg = 'red', fg = 'white')
canStatusValue.pack(fill = 'both', expand = True)

canStatusStatus = tk.Label(canStatus, text = 'NOT TOUCHED', bg = 'red', fg = 'white')
canStatusStatus.pack(fill = 'both', expand = True)



pwindow.pack(fill='both', expand = True)

switchDesktop()
switchMg()
readSerial()
tick()

window.mainloop()
