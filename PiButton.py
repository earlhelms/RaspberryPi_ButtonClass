#Class for getting button state with raspberry pi
#The class handles informing the app one time for each button state change 
#Earl Helms May 2016 May 2016 - earl@earlhelms.com visit me at EarlHelms.com or Github/EarlHelms
#
#USAGE >>>
# Create an instance passing a GpioPort
# Call GetButtonEvent() periodically and check the return value

import RPi.GPIO as GpioObject #Raspberry pi GPIO library
import time

class PiButton:

    _Unknown = 100
    _Gpio = _Unknown 
    _LastButtonStatus = _Unknown
    _ButtonDown = 1
    _ButtonUp = 2
    _ButtonNoChange = 3
    _CurrentButtonStatus = _Unknown

    def __init__(self, GpioPort=0):
        GpioObject.setmode(GpioObject.BCM)
        if(GpioPort != 0):
            self.SetGpioPort(GpioPort)

    # Set the Gpio port that is on the raspberry pi for this button
    def SetGpioPort(self,GpioPort=""):
        IsPortNumber = False 
        if(type(GpioPort)==str):
            #Validate that the string passed is a digit
            IsPortNumber = GpioPort.isdigit()
            if(IsPortNumber):
                self._Gpio = int(GpioPort)
        elif(type(GpioPort)==int):
            IsPortNumber = True
            self._Gpio = GpioPort
        if(IsPortNumber):
            GpioObject.setup(self._Gpio, GpioObject.IN, pull_up_down=GpioObject.PUD_UP)
        else:
            ErrorString = "The GpioPort parameter passed \"{0}\" is not a number".format(GpioPort)
            raise ValueError(ErrorString)

    # Gets the current state of the button
    def GetStatus(self):
        if(self._Gpio == self._Unknown):
            raise RuntimeError("You must first call SetGpioPort before calling the GetStatus function")
        RetVal = self._Unknown 
        ButtonState = GpioObject.input(self._Gpio)
        if(ButtonState):
            self._CurrentButtonStatus = self._ButtonDown
            RetVal = self._ButtonDown            
        elif(ButtonState == False):
            self._CurrentButtonStatus = self._ButtonUp
            RetVal = self._ButtonUp
        return RetVal 
        
    # Returns a value indicating if a button event took place
    # the button event is only returned one time for each event
    # The events are _ButtonDown, _ButtonUp or _ButtonNoChange
    # _ButtonDown indicates that the button was pressed
    # _ButtonUp indicates that the button changed from pressed to not pressed
    # _ButtonNoChange indicates that the status of the button has not changed since the last check
    #  if you pass a False argumnent you will have to manually call GetStatus() to update the status  
    def GetEventCode(self,GetTheStatus = True):
        RetVal = self._ButtonNoChange
        if(GetTheStatus):
            self.GetStatus()
        if(self._LastButtonStatus != self._Unknown):
            if(self._CurrentButtonStatus == self._ButtonUp and self._LastButtonStatus != self._ButtonUp):
                #The button status changed to pressed
                RetVal = self._ButtonUp
            elif(self._CurrentButtonStatus == self._ButtonDown and self._LastButtonStatus != self._ButtonDown):
                #The button status changed to not pressed
                RetVal = self._ButtonDown
        self._LastButtonStatus = self._CurrentButtonStatus
        return RetVal
        

    
 
    
