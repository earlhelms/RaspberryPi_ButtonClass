# RaspberryPi_ButtonClass
A python app providing a class wrapper around button event tracking with a raspberry pi
Earl Helms May 2016

What it does:
1 - Abstracts away the underlying GPIO calls to detect button state
2 - Generates a single event for each button state change. The events are the return value of the function
3 - If you need multiple buttons, create multiple instances of the class with different GPIO values

Files:
PiButton.py - This is the class, you don't need to edit this, just grab a copy and put it in the same folder
TryButton.py - An example app that uses the class and prints to the screen on button press or release


