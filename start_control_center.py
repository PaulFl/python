from os import system
from time import sleep

system('export DISPLAY=:0.0')
system('export LC_CTYPE="en_US.UTF-8"')

if 256 == system('pidof Xorg'):
    system('startx&')
    sleep(10)

system('/home/paul/Documents/start_control_center.sh&')
