import RPi.GPIO as gpio
from time import sleep

backlight = True

gpio.setmode(gpio.BCM)

k1pin = 16
k2pin = 19
k3pin = 20
k4pin = 26

gpio.setup(k1pin, gpio.OUT)
gpio.output(k1pin, 0)
sleep(0.3)
gpio.output(k1pin, 1)
sleep(0.3)
gpio.output(k1pin, 0)
sleep(0.3)
gpio.output(k1pin, 1)
sleep(0.3)
gpio.output(k1pin, 0)
sleep(0.3)
gpio.setup(k1pin, gpio.IN)

if backlight:
    gpio.setup(k2pin, gpio.OUT)
    gpio.output(k2pin, 0)
    sleep(6)
    gpio.setup(k2pin, gpio.IN)
else:
    gpio.setup(k3pin, gpio.OUT)
    gpio.output(k3pin, 0)
    sleep(6)
    gpio.setup(k3pin, gpio.IN)
