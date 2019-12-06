from cpu_temp import get_cpu_temperature
from os import system
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

temp_regulation = False

switchPin = 17
switchPin2 = 24
switchPin3 = 23

gpio.setup(switchPin, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(switchPin2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(switchPin3, gpio.IN, pull_up_down=gpio.PUD_UP)

system('export DISPLAY=:0.0')
system('export LC_CTYPE="en_US.UTF-8"')
#system('sudo /home/paul/Documents/ethernet_leds l0 f1')

switchState = gpio.input(switchPin)
switchState2 = gpio.input(switchPin2)
switchState3 = gpio.input(switchPin3)

if switchState3:
    temp_regulation = True

def switchCallback(channel):
    sleep(0.5)
    global switchState
    if gpio.input(switchPin) != switchState:
        switchState = not switchState
        if switchState:
            #system('sudo /home/paul/Documents/ethernet_leds l1 f1')
            if 256 == system('pidof Xorg'):
                system('startx&')
                sleep(10)
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f start_control_center.sh')
            system('pkill -f chromium-browser')
            system('/home/paul/Documents/start_control_center.sh&')
        else:
            #system('sudo /home/paul/Documents/ethernet_leds l0 f1')
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f chromium-browser')
            system('pkill -f start_control_center.sh')
            system('pkill -f start_control_center_octoprint.sh')
            
def switchCallback2(channel):
    sleep(0.5)
    global switchState2
    if gpio.input(switchPin2) != switchState2:
        switchState2 = not switchState2
        if switchState2:
            #system('sudo /home/paul/Documents/ethernet_leds l1 f1')
            if 256 == system('pidof Xorg'):
                system('startx&')
                sleep(10)
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f start_control_center.sh')
            system('pkill -f chromium-browser')
            system('/home/paul/Documents/start_control_center_octoprint.sh&')
        else:
            #system('sudo /home/paul/Documents/ethernet_leds l0 f1')
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f chromium-browser')
            system('pkill -f start_control_center.sh')
            system('pkill -f start_control_center_octoprint.sh')
            
def switchCallback3(channel):
    global temp_regulation
    sleep(0.5)
    global switchState3
    if gpio.input(switchPin3) != switchState3:
        switchState3 = not switchState3
        if switchState3:
            temp_regulation = True
            temp = get_cpu_temperature()
            if temp > 65:
                system('echo 41 > /dev/arduino')
        else:
            temp_regulation = False
            system('echo 40 > /dev/arduino')

        

gpio.add_event_detect(switchPin, gpio.BOTH, callback=switchCallback, bouncetime=300)
gpio.add_event_detect(switchPin2, gpio.BOTH, callback=switchCallback2, bouncetime=300)
gpio.add_event_detect(switchPin3, gpio.BOTH, callback=switchCallback3, bouncetime=300)

while True:
    sleep(20)
    if temp_regulation:
        temp = get_cpu_temperature()
        if temp > 65:
            system('echo 41 > /dev/arduino')
        elif temp < 55:
            system('echo 40 > /dev/arduino')

gpio.cleanup()
