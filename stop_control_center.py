from os import system
from time import sleep

system('export DISPLAY=:0.0')
system('export LC_CTYPE="en_US.UTF-8"')

system('pkill -f control_center.py')
system('pkill -f uxterm')
system('pkill -f chromium-browser')
system('pkill -f start_control_center.sh')
