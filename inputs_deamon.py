from os import system
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)


switchPin = 4

gpio.setup(switchPin, gpio.IN, pull_up_down=gpio.PUD_UP)

system('export DISPLAY=:0.0')
system('export LC_CTYPE="en_US.UTF-8"')
system('sudo /home/paul/Documents/ethernet_leds l0 f1')

def switchCallback(channel):
    sleep(0.5)
    switchState = gpio.input(switchPin)
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
        

gpio.add_event_detect(switchPin, gpio.BOTH, callback=switchCallback, bouncetime=300)

while True:
    sleep(10000)

gpio.cleanup()
