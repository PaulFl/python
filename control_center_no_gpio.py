#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
import time
import serial
import requests
import datetime
from soco import SoCo
from PIL import Image, ImageTk
import urllib
from multiprocessing import Process, Queue

k1pin = 16
k2pin = 19
k3pin = 20
k4pin = 26

doorSwitchPin = 12
doorLedPin = 6

# ser = serial.Serial(port='/dev/tty0', timeout = 0)

sonos = SoCo("192.168.0.230")

img = None
musicPreviousTitle = ''

serLine = ''

time1 = ''

desktopState = True
mgState = True
ledState = True
doorLedState = True
doorState = True
v12State = True
canState = False
musicPlaying = False


def keydown(e):
    key = e.keycode
    if key == 65:
        sonosPlayPause()
    elif key == 114:
        sonos.next()
    elif key == 113:
        sonos.previous()
    elif key == 111:
        sonos.ramp_to_volume(sonos.volume + 1)
    elif key == 116:
        sonos.ramp_to_volume(sonos.volume - 1)
    elif key == 90:
        switchDesktop()
    elif key == 87:
        switchV12()
    elif key == 104:
        switchMg()
    elif key == 88:
        switchLed()
    elif key == 89:
        switchDoorLed()
    elif key == 86:
        window.attributes('-fullscreen', True)
    elif key == 82:
        window.attributes('-fullscreen', False)


def callgetSonosInfo():
    #    global musicPlaying
    #    global musicPreviousTitle
    queue = Queue()
    action_process = Process(target=getSonosInfo, args=(queue,))
    action_process.start()
    action_process.join(timeout=5)
    action_process.terminate()
    global musicPlaying
    if not queue.empty():
        musicPlaying = queue.get()
    #    if not queue.empty():
    #        dat = queue.get()
    #        if not dat:
    #            musicPreviousTitle = dat[0]
    #            musicArtwork.configure(image = dat[1])
    if not queue.empty():
        musicTitle.config(text=queue.get())
    if not queue.empty():
        musicPosition.config(text=queue.get())
    if not queue.empty():
        musicVolume.config(text=queue.get())
    if musicPlaying:
        musicPlayPause.config(text="Pause")
    else:
        musicPlayPause.config(text="Play")
    music.after(2000, callgetSonosInfo)


def getSonosInfo(queue):
    # global img
    # global musicPlaying
    # global musicPreviousTitle
    #    localMusicPreviousTitle = musicPreviousTitle
    musicPlaying = (sonos.get_current_transport_info()['current_transport_state'] == 'PLAYING')
    queue.put(musicPlaying)
    # if musicPlaying:
    trackInfo = sonos.get_current_track_info()
    title = trackInfo['title']
    #    if (title != localMusicPreviousTitle):
    #        localMusicPreviousTitle = title
    #        img = ImageTk.PhotoImage(Image.open(urllib.request.urlopen(trackInfo['album_art'])))
    #        queue.put((musicPreviousTitle, img))
    #    else:
    #        queue.put(False)
    # musicArtwork.configure(image = img)
    artist = trackInfo['artist']
    # musicTitle.config(text = title + " - " + artist)
    queue.put(title + " - " + artist)
    # musicPosition.config(text = trackInfo['position'] + ' - ' + trackInfo['duration'])
    queue.put(trackInfo['position'] + ' - ' + trackInfo['duration'])
    volume = sonos.volume
    queue.put("Vol: " + str(volume))
    # musicVolume.config(text = "Vol: "+str(volume))


#    if musicPlaying:
#        musicPlayPause.config(text = "Pause")
#    else:
#        musicPlayPause.config(text = "Play")
# musicArtwork.configure(image = None)

def sonosPlayPause():
    if musicPlaying:
        sonos.pause()
    else:
        sonos.play()


def updateWeather():
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=Baulne,fr&appid=aecef374984aecf5c205fb2d974115ac")
    weatherValue = r.json()['weather'][0]['main']
    weatherMain.config(text=weatherValue)
    temp = float(r.json()['main']['temp'])
    temp -= 273.15
    temp = round(temp, 1)
    temperature.config(text="Temp: " + str(temp) + "°C")
    pressureValue = int(r.json()['main']['pressure'])
    pressure.config(text="Press: " + str(pressureValue) + "hPa")
    windValue = float(r.json()['wind']['speed'])
    windValue *= 1.94384
    windValue = round(windValue, 1)
    wind.config(text="Wind: " + str(windValue) + "kts")
    sunRise = datetime.datetime.fromtimestamp(r.json()['sys']['sunrise']).strftime('%H:%M')
    sunSet = datetime.datetime.fromtimestamp(r.json()['sys']['sunset']).strftime('%H:%M')
    sun.config(text="Sun\n" + sunRise + "   " + sunSet)
    clockDisplay.after(1800 * 1000, updateWeather)


def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clockDate1.config(text=time.strftime("%d/%m/%y"))
        clockDate2.config(text=time.strftime("%a, %d %b"))
        clockDisplay.config(text=time2)
    clockDisplay.after(200, tick)


def updateDoor():
    global doorState
    state = True
    if doorState != state:
        if (not doorState and state):
            print('hey')
            top = tk.Toplevel()
            top.title('Door openned')
            tk.Message(top, text='BONJOUR !', pady=500, font=('Arial', 250)).pack()
            top.after(7000, top.destroy)
        switchDoor()
    doorPosition.after(300, updateDoor)


def processLine(line):
    if (len(line) > 2):
        if (line[0] == 'a'):
            line = line[1:]
            if (line.find('a') == -1):
                if (line[0] != '\n'):
                    id = int(line[0])
                    if (id == 1 or id == 2 or id == 3 or id == 4 or id == 9):
                        if (line[1:] != '\n'):
                            state = bool(int(line[1:]))
                            setDevice(id, state)
                    elif (id == 5 or id == 6 or id == 7 or id == 8):
                        if (line[1:] != '\n'):
                            value = int(line[1:])
                            setDeviceValue(id, value)


# def readSerial():
#     global serLine
#     if ser.inWaiting()>0:
#         line = ser.read(ser.inWaiting()).decode()
#         while line.find('\n') != -1:
#             i = line.find('\n')
#             serLine += line[:i-1]
#             processLine(serLine)
#             serLine = ''
#             line = line[i+1:]
#     clockDisplay.after(100, readSerial)

def setDeviceValue(id, value):
    if id == 5:
        ledRedSlider.set(value)
    elif id == 6:
        ledGreenSlider.set(value)
    elif id == 7:
        ledBlueSlider.set(value)
    elif id == 8:
        canStatusValue.config(text=str(abs(value)))
        canBarValue.set(abs(value))


def setDevice(id, state):
    if id == 1:
        global desktopState
        desktopState = state
        for widget in [desktop, desktopSwitch, desktopStatus, desktopLabel]:
            if desktopState:
                widget.config(bg='green')
            else:
                widget.config(bg='red')
        if desktopState:
            desktopSwitch.config(text='OFF', fg='black')
            desktopStatus.config(text='ON', fg='black')
            desktopLabel.config(fg='black')
        else:
            desktopSwitch.config(text='ON', fg='white')
            desktopStatus.config(text='OFF', fg='white')
            desktopLabel.config(fg='white')
    elif id == 2:
        global mgState
        mgState = state
        for widget in [mg, mgSwitch, mgStatus, mgLabel]:
            if mgState:
                widget.config(bg='green')
            else:
                widget.config(bg='red')
        if mgState:
            mgSwitch.config(text='OFF', fg='black')
            mgStatus.config(text='ON', fg='black')
            mgLabel.config(fg='black')
        else:
            mgSwitch.config(text='ON', fg='white')
            mgStatus.config(text='OFF', fg='white')
            mgLabel.config(fg='white')
    elif id == 3:
        global ledState
        ledState = state
        for widget in [led, ledSwitch, ledStatus, ledLabel]:
            if ledState:
                widget.config(bg='green')
            else:
                widget.config(bg='red')
        if ledState:
            ledSwitch.config(text='OFF', fg='black')
            ledStatus.config(text='ON', fg='black')
            ledLabel.config(fg='black')
        else:
            ledSwitch.config(text='ON', fg='white')
            ledStatus.config(text='OFF', fg='white')
            ledLabel.config(fg='white')
    elif id == 4:
        global v12State
        v12State = state
        for widget in [v12, v12Switch, v12Status, v12Label]:
            if v12State:
                widget.config(bg='green')
            else:
                widget.config(bg='red')
        if v12State:
            v12Switch.config(text='OFF', fg='black')
            v12Status.config(text='ON', fg='black')
            v12Label.config(fg='black')
        else:
            v12Switch.config(text='ON', fg='white')
            v12Status.config(text='OFF', fg='white')
            v12Label.config(fg='white')
    elif id == 9:
        global canState
        canState = state
        for widget in [canStatus, canStatusStatus, canStatusLabel, canStatusValue]:
            if ledState:
                widget.config(bg='green')
            else:
                widget.config(bg='red')
        if canState:
            canStatusStatus.config(text='TOUCHED', fg='black')
            canStatusValue.config(fg='black')
            canStatusLabel.config(fg='black')
        else:
            canStatusStatus.config(text='NOT TOUCHED', fg='white')
            canStatusValue.config(fg='white')
            canStatusLabel.config(fg='white')


# def writeSerial(line):
#     ser.write((line + '\n').encode('utf-8'))

def switchV12():
    global v12State
    v12State = not v12State
    for widget in [v12, v12Switch, v12Status, v12Label]:
        if v12State:
            widget.config(bg='green')
        else:
            widget.config(bg='red')
    if v12State:
        v12Switch.config(text='OFF', fg='black')
        v12Status.config(text='ON', fg='black')
        v12Label.config(fg='black')
        # writeSerial('41')
    else:
        v12Switch.config(text='ON', fg='white')
        v12Status.config(text='OFF', fg='white')
        v12Label.config(fg='white')
        # writeSerial('40')


def switchDesktop():
    global desktopState
    desktopState = not desktopState
    for widget in [desktop, desktopSwitch, desktopStatus, desktopLabel]:
        if desktopState:
            widget.config(bg='green')
        else:
            widget.config(bg='red')
    if desktopState:
        desktopSwitch.config(text='OFF', fg='black')
        desktopStatus.config(text='ON', fg='black')
        desktopLabel.config(fg='black')
        # writeSerial('11')
    else:
        desktopSwitch.config(text='ON', fg="white")
        desktopStatus.config(text='OFF', fg='white')
        desktopLabel.config(fg='white')
        # writeSerial('10')


def switchDoor():
    global doorState
    global doorLedState
    doorState = not doorState
    for widget in [doorPosition, doorPositionLabel, doorPositionStatus]:
        if doorState:
            widget.config(bg='green')
        else:
            widget.config(bg='red')
    if doorState:
        doorPositionStatus.config(text='OPEN', fg='black')
        doorPositionLabel.config(fg='black')
    else:
        doorPositionStatus.config(text='CLOSED', fg='white')
        doorPositionLabel.config(fg='white')
    doorLedState = doorState
    switchDoorLed()


def switchMg():
    global mgState
    mgState = not mgState
    for widget in [mg, mgSwitch, mgStatus, mgLabel]:
        if mgState:
            widget.config(bg='green')
        else:
            widget.config(bg='red')
    if mgState:
        mgSwitch.config(text='OFF', fg='black')
        mgStatus.config(text='ON', fg='black')
        mgLabel.config(fg='black')
        # writeSerial('21')
    else:
        mgSwitch.config(text='ON', fg='white')
        mgStatus.config(text='OFF', fg='white')
        mgLabel.config(fg='white')
        # writeSerial('20')


def switchLed():
    global ledState
    ledState = not ledState
    for widget in [led, ledSwitch, ledStatus, ledLabel]:
        if ledState:
            widget.config(bg='green')
        else:
            widget.config(bg='red')
    if ledState:
        ledSwitch.config(text='OFF', fg='black')
        ledStatus.config(text='ON', fg='black')
        ledLabel.config(fg='black')
        # writeSerial('31')
    else:
        ledSwitch.config(text='ON', fg='white')
        ledStatus.config(text='OFF', fg='white')
        ledLabel.config(fg='white')
        # writeSerial('30')


def switchDoorLed():
    global doorLedState
    doorLedState = not doorLedState
    for widget in (doorLed, doorLedSwitch, doorLedStatus, doorLedLabel):
        if doorLedState:
            widget.config(bg='green')
        else:
            widget.config(bg='red')
    if doorLedState:
        doorLedSwitch.config(text='OFF', fg='black')
        doorLedStatus.config(text='ON', fg='black')
        doorLedLabel.config(fg='black')
    else:
        doorLedSwitch.config(text='ON', fg='white')
        doorLedStatus.config(text='OFF', fg='white')
        doorLedLabel.config(fg='white')


window = tk.Tk()
window.title("Control Center")

canBarValue = tk.IntVar()
pwindow = tk.PanedWindow(window, orient='horizontal')

lights = tk.Frame(window)
pwindow.add(lights, stretch="always")

sensors = tk.Frame(window)
pwindow.add(sensors, stretch='always')

clock = tk.Frame(window)
pwindow.add(clock)

lightsLabel = tk.Label(lights, text='Outputs', font=('Arial', 50))
lightsLabel.pack(fill='both', expand=False)

sensorsLabel = tk.Label(sensors, text='Sensors', font=('Arial', 50))
sensorsLabel.pack(fill='both', expand=False)

clockLabel = tk.Label(clock, text='Control', font=('Arial', 50))
clockLabel.pack(fill='both', expand=False)

v12 = tk.Frame(lights, bg='green')
v12.pack(fill='both', expand=True)

v12Label = tk.Label(v12, text="12V Output", bg='green', font=('Arial', 25))
v12Label.pack(fill='both', expand=True)

v12Status = tk.Label(v12, text='ON', bg='green', font=('Arial', 25))
v12Status.pack(fill='both', expand=True)

v12Switch = tk.Button(v12, text='OFF', bg='green', command=switchV12, font=('Arial', 25))
v12Switch.pack(fill='both', expand=True)

desktop = tk.Frame(lights, bg='green')
desktop.pack(fill='both', expand=True)

desktopLabel = tk.Label(desktop, text="Desktop", bg='green', font=('Arial', 25))
desktopLabel.pack(fill='both', expand=True)

desktopStatus = tk.Label(desktop, text='ON', bg='green', font=('Arial', 25))
desktopStatus.pack(fill='both', expand=True)

desktopSwitch = tk.Button(desktop, text='OFF', bg='green', command=switchDesktop, font=('Arial', 25))
desktopSwitch.pack(fill='both', expand=True)

mg = tk.Frame(lights, bg='green')
mg.pack(fill='both', expand=True)

mgLabel = tk.Label(mg, text="Magnifying glass", bg='green', font=('Arial', 25))
mgLabel.pack(fill='both', expand=True)

mgStatus = tk.Label(mg, text='ON', bg='green', font=('Arial', 25))
mgStatus.pack(fill='both', expand=True)

mgSwitch = tk.Button(mg, text='OFF', bg='green', command=switchMg, font=('Arial', 25))
mgSwitch.pack(fill='both', expand=True)

led = tk.Frame(lights, bg='green')
led.pack(fill='both', expand=True)

ledLabel = tk.Label(led, text="LEDs", bg='green', font=('Arial', 25))
ledLabel.pack(fill='both', expand=True)

ledStatus = tk.Label(led, text='ON', bg='green', font=('Arial', 25))
ledStatus.pack(fill='both', expand=True)

ledSliders = tk.Frame(led, bg='green')
ledSliders.pack(fill='both', expand=True)

redValue = tk.DoubleVar()
ledRedSlider = tk.Scale(ledSliders, variable=redValue, bg='red', font=('Arial', 25))
ledRedSlider.config(from_=255, to=0)
ledRedSlider.pack(side='left', fill='both', expand=True)

greenValue = tk.DoubleVar()
ledGreenSlider = tk.Scale(ledSliders, variable=greenValue, bg='green', font=('Arial', 25))
ledGreenSlider.config(from_=255, to=0)
ledGreenSlider.pack(side='left', fill='both', expand=True)

blueValue = tk.DoubleVar()
ledBlueSlider = tk.Scale(ledSliders, variable=blueValue, bg='blue', font=('Arial', 25))
ledBlueSlider.config(from_=255, to=0)
ledBlueSlider.pack(side='left', fill='both', expand=True)

ledSwitch = tk.Button(led, text='OFF', bg='green', command=switchLed, font=('Arial', 25))
ledSwitch.pack(fill='both', expand=True)

doorLed = tk.Frame(lights, bg="green")
doorLed.pack(fill='both', expand=True)

doorLedLabel = tk.Label(doorLed, text="Door LED", bg='green', font=('Arial', 25))
doorLedLabel.pack(fill='both', expand=True)

doorLedStatus = tk.Label(doorLed, text='ON', bg='green', font=('Arial', 25))
doorLedStatus.pack(fill='both', expand=True)

doorLedSwitch = tk.Button(doorLed, text='OFF', bg='green', command=switchDoorLed, font=('Arial', 25))
doorLedSwitch.pack(fill='both', expand=True)

clockDate2 = tk.Label(clock, font=('Arial', 45), fg='white', bg='black')
clockDate2.pack(fill='both', expand=True)

weatherMain = tk.Label(clock, font=('Arial', 35), fg='white', bg='black')
weatherMain.pack(fill='both', expand=True)

temperature = tk.Label(clock, font=('Arial', 35), fg='white', bg='black')
temperature.pack(fill='both', expand=True)

pressure = tk.Label(clock, font=('Arial', 35), fg='white', bg='black')
pressure.pack(fill='both', expand=True)

wind = tk.Label(clock, font=('Arial', 35), fg='white', bg='black')
wind.pack(fill='both', expand=True)

sun = tk.Label(clock, font=('Arial', 35), fg='white', bg='black')
sun.pack(fill='both', expand=True)

clockDate1 = tk.Label(clock, font=('Arial', 72), fg='white', bg='black')
clockDate1.pack(fill='both', expand=True)

clockDisplay = tk.Label(clock, font=('Arial', 72), fg='white', bg='black')
clockDisplay.pack(fill='both', expand=True)

doorPosition = tk.Frame(sensors, bg='green')
doorPosition.pack(fill='both', expand=True)

doorPositionLabel = tk.Label(doorPosition, text="Door status", bg='green', font=('Arial', 25))
doorPositionLabel.pack(fill='both', expand=True)

doorPositionStatus = tk.Label(doorPosition, text='OPEN', bg='green', font=('Arial', 25))
doorPositionStatus.pack(fill='both', expand=True)

canStatus = tk.Frame(sensors, bg='red')
canStatus.pack(fill='both', expand=True)

canStatusLabel = tk.Label(canStatus, text="Can status", bg='red', fg='white', font=('Arial', 25))
canStatusLabel.pack(fill='both', expand=True)

canStatusBar = ttk.Progressbar(canStatus, variable=canBarValue, maximum=30000, orient='vertical')
canStatusBar.pack()

canStatusValue = tk.Label(canStatus, text='NULL', bg='red', fg='white', font=('Arial', 25))
canStatusValue.pack(fill='both', expand=True)

canStatusStatus = tk.Label(canStatus, text='NOT TOUCHED', bg='red', fg='white', font=('Arial', 25))
canStatusStatus.pack(fill='both', expand=True)

music = tk.Frame(sensors, bg='black')
music.pack(fill='both', expand=True)

musicLabel = tk.Label(music, text="Music", bg='black', fg="white", font=('Arial', 25))
musicLabel.pack(fill='both', expand=True)

musicTitle = tk.Label(music, text="Title", bg='black', fg="white", font=('Arial', 20), wraplengt=220)
musicTitle.pack(fill='both', expand=True)

# musicArtwork = tk.Label(music)
# musicArtwork.pack(fill = 'both', expand = True)

musicPosition = tk.Label(music, text="-", bg='black', fg="white", font=('Arial', 20))
musicPosition.pack(fill='both', expand=True)

musicVolume = tk.Label(music, text="Vol: ", bg='black', fg='white', font=('Arial', 20))
musicVolume.pack(fill='both', expand=True)

musicControls = tk.Frame(music, bg='black')
musicControls.pack(fill='both', expand=True)

musicPrevious = tk.Button(musicControls, text="<<", bg="black", fg="white", font=('Arial', 25), command=sonos.previous)
musicPrevious.pack(side='left', fill='both', expand=True)

musicPlayPause = tk.Button(musicControls, text="Play", bg='black', fg="white", font=('Arial', 25),
                           command=sonosPlayPause)
musicPlayPause.pack(side='left', fill='both', expand=True)

musicNext = tk.Button(musicControls, text=">>", bg="black", fg="white", font=('Arial', 25), command=sonos.next)
musicNext.pack(side="left", fill="both", expand=True)

pwindow.pack(fill='both', expand=True)

window.bind('<KeyPress>', keydown)

switchDesktop()
switchMg()
switchV12()
# readSerial()
tick()
updateDoor()
clockDisplay.after(1000, updateWeather)
music.after(2000, callgetSonosInfo)

window.mainloop()