from gpiozero import OutputDevice
import time
relay = OutputDevice(18)

try:
    while True:
     relay.on()
     time.sleep(2)
     relay.off()
     time.sleep(2)
except :
    relay.close()
"""
from gpiozero import Button, OutputDevice
from signal import pause


button = Button (17, pull_up = False)
relay = OutputDevice (12)

def on ():
    relay.on()
    
def off ():
    relay.off ()
    
def toggle ():
    relay.toggle ()


button.when_pressed = toggle
button.when_released = off

try:
    pause()
except KeyboardInterrupt:
  
    button.close()
    relay.close()
rell.txt
Ouvrir avec

Affichage de rell.txt"""


















""""from gpiozero import Button, OutputDevice
from signal import pause


#button = Button (17, pull_up = False)
relay = OutputDevice (18)

def on ():
    relay.on()
    
def off ():
    relay.off ()
    
def toggle ():
    relay.toggle ()


#button.when_pressed = toggle
#button.when_released = off

try:
    pause()
except KeyboardInterrupt:
  
    #button.close()
    relay.close()"""