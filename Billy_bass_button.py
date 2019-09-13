# This script is uses the program saying_sound_using_buttons.py adapted from
# Mike Barela's tutorial on Adafruit.com:  Speech Synthesis on the Raspberry Pi
# https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/introductionhttps://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/introduction
# Mike Barela's code is located at https://raw.githubusercontent.com/adafruit/Adafruit_Learning_System_Guides/master/Speech_Synthesis_on_the_Raspberry_Pi/saying_sounds_using_buttons.py
# Mike's tutorial references the Adafruit Tutorial "Playing sounds and
# using buttons with Raspberry Pi" by Michael Sklar
# The code is located at https://raw.githubusercontent.com/adafruit/Adafruit_Learning_System_Guides/master/Playing_Sounds_and_Using_Buttons_with_Raspberry_Pi/audio-button.py
# It has been modified to allow text-to-speech by a Billy Bass toy by using the events.txt file created by BillyBassScrapper.py, 
# a python script that pulls events data down from a meetup site.
# Festival text-to-speech package:  http://festvox.org/festival/
# From the RPi command line run: sudo apt-get install festival -y
# Maureen Haley, 9/12/19

import time
import os
import board
import digitalio

# set up button on RPi zero W GPIO pin 23
button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

#button2 = digitalio.DigitalInOut(board.D24)
#button2.direction = digitalio.Direction.INPUT
#button2.pull = digitalio.Pull.UP

#button3 = digitalio.DigitalInOut(board.D25)
#button3.direction = digitalio.Direction.INPUT
#button3.pull = digitalio.Pull.UP


print("press a button!")

while True:
    
    if not button1.value:
        # pipe text to festival
        os.system('echo "I, , , Today is " | festival --tts')
	# use date to get todays date and time and pipe to festival
        os.system('date "+%A %B %d %Y %I:%M %P" | festival --tts')
       # os.system('date "+%H%M" | festival --tts')
        os.system('echo "I, , , Upcoming Events at Decatur Makers from Meetup dot com,  include, ,  "| festival --tts')
       # read events.txt with festival
        os.system('festival --tts events.txt')

#    if not button2.value:
#        os.system('echo "I, , , Some rescue!" | festival --tts')

#    if not button3.value:
#        os.system('echo "I, , , I find your lack of faith disturbing." | festival --tts')

    time.sleep(0.1)
