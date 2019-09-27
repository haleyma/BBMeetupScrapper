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
import meetup.api
import json
import requests
import time
import codecs
import sys
import io
import datetime
import threading

#  Python script to contact meetup.com api and pull down events data for Decatur Makers
#  URL params obtained from meetup.com api:  https://www.meetup.com/meetup_api/
#  datetime manipulation, file writing code developed with the help of 
#  Automate the boring stuff with Python by Al Sweigart
#  https://automatetheboringstuff.com/
#  This code writes the info to events.txt which is read by Billy_bass_button.py
#  Festival text-to-speech then reads the events.txt file
#  http://festvox.org/festival/
#  Maureen Haley , 9/12/19

def billyBassScrapper():
    # current days datetime object converted to string in the iso 8601 format required by meeptup api
    currentTime = ((datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')) + '.000'
    print(currentTime)
    #  timedelta used to get string for day one week in the future
    endDate = (datetime.datetime.now() + (datetime.timedelta(days=8))).strftime('%Y-%m-%dT') + '00:00:00.000'
    print(endDate)

    #  only= params to get key:value pairs for date, time, event name
    url ='https://api.meetup.com/Decatur-Makers/events?&sign=true&photo-host=public&no_later_than=' + endDate + '&no_earlier_than=' + currentTime + '&only=local_date,local_time,name'

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()


    print(len(response.json()))
    print(data)

    #  write values for each event to the events.txt file
    #  format the date/time so that it will sound good spoken by the Festival package
    #  use "w" to overwrite previous info in events.txt
    f = open("events.txt", "w")
    thisDay = datetime.datetime.now().strftime('%A, %B %d')
    f.write('\n' + 'Today is ' + thisDay)
    f.write('\n')
    f.write('\n' + 'Upcoming events for Decatur Makers from Meetup dot com include:')
    f.write('\n')
    for i in range(0,len(response.json())):
        ld = data[i]['local_date'] 
        lt = data[i]['local_time']
        eD = ld + ' ' + lt
        print(eD)
        eventDate = datetime.datetime.strptime(eD, '%Y-%m-%d %H:%M')
        eventString = eventDate.strftime('%A %B %d %I:%M %p')
        f.write('\n' + ', ,' + eventString)
        # f.write('\n' + data[i]['local_time'])
        f.write('\n' + data[i]['name'] + ',')
        f.write('\n')
    f.close()

    #  print the events.txt file to the terminal just to check how it looks
    f = open("events.txt", "r")
    print(f.read())
    #print len(response.json())
    #print data
    #print data[0]['local_date']
    #print data[0]['local_time']
    #print data[0]['name']
    time.sleep(3600)  # run every hour - 3600 seconds
    
threadObj = threading.Thread(target=billyBassScrapper)
threadObj.start()


# set up button on RPi zero W GPIO pin 23
button1 = digitalio.DigitalInOut(board.D23)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D24)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

#button3 = digitalio.DigitalInOut(board.D25)
#button3.direction = digitalio.Direction.INPUT
#button3.pull = digitalio.Pull.UP


print("press a button!")

while True:
    
    if not button1.value:
        # pipe text to festival
       # os.system('echo "I, , , Today is " | festival --tts')
	# use date to get todays date and time and pipe to festival
       # os.system('date "+%A %B %d %Y %I:%M %P" | festival --tts')
       # os.system('date "+%H%M" | festival --tts')
       # os.system('echo "I, , , Upcoming Events at Decatur Makers from Meetup dot com,  include, ,  "| festival --tts')
       # read events.txt with festival
        os.system('festival --tts events.txt')

    if not button2.value:
        os.system('date "+%I:%M %p" | festival --tts')

#    if not button3.value:
#        os.system('echo "I, , , I find your lack of faith disturbing." | festival --tts')

    time.sleep(0.1)
