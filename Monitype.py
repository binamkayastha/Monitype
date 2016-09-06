from evdev import InputDevice
from select import select
from numbers import Number
import sys
import pygame
import re

def isModifier(key): #passed in parameter is keycode
    key = key[0:len(key)-1]  #get rid of ',' at end of key
    key = int(key)
    #L/R,on/off Shift, Ctrl,   Alt,     Win, Esc, Caps
    if(key in [42, 54, 29, 97, 56, 100, 125, 0, 4, 1, 58]):
        return True
    else:
        return False

#Starts here

#Input from keyboard event. This is why this program needs root permissions
#dev = InputDevice("/dev/input/by-path/platform-i8042-serio-0-event-kbd")
dev = InputDevice("/dev/input/event0")

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
        #Next two lines take neccessary info from the event. To see more info from event, print event.
        code = str(event).split(" ")[4]
        keydown = str(event).split("val")[1] #Value 01 if KeyDown.
        if ((not isModifier(code)) and code != '00,' and keydown == " 01"):
            print("letter pressed")
