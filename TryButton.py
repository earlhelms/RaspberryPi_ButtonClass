# TryButton, a demo of using the PiButton class to
# handle getting button events from raspberry pi GPIO ports
# This example uses a Pi 3 GPIO port 18 connected to an on/off push button
# When the button is pressed you will get a message
# When the button is released you will get a message
# The key here is, only one event will occur for each button press or 
# release even though it loops once every 200 milliseconds  
# The class handles suppressing repetitive events
# If you want multiple buttons, create multiple instances of the class 
# passing a different GPIO value for each
#
# Created by Earl Helms May 2016 - earl@earlhelms.com visit me at EarlHelms.com or Github/EarlHelms

from PiButton import PiButton
import time

TheButton = PiButton(18)
while True:
    time.sleep(0.2)
    EventCode = TheButton.GetEventCode()
    if(EventCode == TheButton._ButtonDown):
        # Button down code goes here...
        print("ButtonDown")
    elif(EventCode == TheButton._ButtonUp):
        # Button up code goes here...
        print("ButtonUp")
