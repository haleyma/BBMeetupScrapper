#  Python script to contact meetup.com api and pull down events data for Decatur Makers
#  URL params obtained from meetup.com api:  https://www.meetup.com/meetup_api/
#  datetime manipulation, file writing code developed with the help of 
#  Automate the boring stuff with Python by Al Sweigart
#  https://automatetheboringstuff.com/
#  This code writes the info to events.txt which is read by Billy_bass_button.py
#  Festival text-to-speech then reads the events.txt file
#  http://festvox.org/festival/
#  Maureen Haley , 9/12/19



import meetup.api
import json
import requests
import time
import codecs
import sys
import io
import datetime

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


