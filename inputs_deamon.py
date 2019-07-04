from os import system
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)


switchPin = 17
switchPin2 = 23
switchPin3 = 24

gpio.setup(switchPin, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(switchPin2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(switchPin3, gpio.IN, pull_up_down=gpio.PUD_UP)

system('export DISPLAY=:0.0')
system('export LC_CTYPE="en_US.UTF-8"')
system('sudo /home/paul/Documents/ethernet_leds l0 f1')

switchState = gpio.input(switchPin)
switchState2 = gpio.input(switchPin2)
switchState3 = gpio.input(switchPin3)

def switchCallback(channel):
    sleep(0.5)
    global switchState
    if gpio.input(switchPin) != switchState:
        switchState = not switchState
        if switchState:
            system('sudo /home/paul/Documents/ethernet_leds l1 f1')
            if 256 == system('pidof Xorg'):
                system('startx&')
                sleep(10)
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f start_control_center.sh')
            system('pkill -f chromium-browser')
            system('/home/paul/Documents/start_control_center.sh&')
        else:
            system('sudo /home/paul/Documents/ethernet_leds l0 f1')
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
            system('sudo /home/paul/Documents/ethernet_leds l1 f1')
            if 256 == system('pidof Xorg'):
                system('startx&')
                sleep(10)
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f start_control_center.sh')
            system('pkill -f chromium-browser')
            system('/home/paul/Documents/start_control_center_octoprint.sh&')
        else:
            system('sudo /home/paul/Documents/ethernet_leds l0 f1')
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f chromium-browser')
            system('pkill -f start_control_center.sh')
            system('pkill -f start_control_center_octoprint.sh')
            
def switchCallback3(channel):
    sleep(0.5)
    global switchState3
    if gpio.input(switchPin3) != switchState3:
        switchState3 = not switchState3
        if switchState3:
            system('sudo /home/paul/Documents/ethernet_leds l1 f1')
            if 256 == system('pidof Xorg'):
                system('startx&')
                sleep(10)
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f start_control_center.sh')
            system('pkill -f chromium-browser')
            system('/home/paul/Documents/start_control_center_octoprint.sh&')
        else:
            system('sudo /home/paul/Documents/ethernet_leds l0 f1')
            system('pkill -f control_center.py')
            system('pkill -f uxterm')
            system('pkill -f chromium-browser')
            system('pkill -f start_control_center.sh')
            system('pkill -f start_control_center_octoprint.sh')
        

gpio.add_event_detect(switchPin, gpio.BOTH, callback=switchCallback, bouncetime=300)
gpio.add_event_detect(switchPin2, gpio.BOTH, callback=switchCallback2, bouncetime=300)
gpio.add_event_detect(switchPin3, gpio.BOTH, callback=switchCallback3, bouncetime=300)

while True:
    sleep(10000)

gpio.cleanup()
