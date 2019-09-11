


import meetup.api
import json
import requests
import time
import codecs
import sys
import io
import datetime

currentTime = ((datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')) + '.000'
print(currentTime)
endDate = (datetime.datetime.now() + (datetime.timedelta(days=8))).strftime('%Y-%m-%dT') + '00:00:00.000'
print(endDate)

url ='https://api.meetup.com/Decatur-Makers/events?&sign=true&photo-host=public&no_later_than=' + endDate + '&no_earlier_than=' + currentTime + '&only=local_date,local_time,name'

response = requests.get(url)
response.raise_for_status()

data = response.json()


print(len(response.json()))
print(data)
f = open("events.txt", "w")
for i in range(0,len(response.json())):
 #  f.write(data[i]['local_date'])
#   f.write(data[i]['local_time'])
   f.write(data[i]['name'])
f.close()

f = open("events.txt", "r")
print(f.read())
#print len(response.json())
#print data
#print data[0]['local_date']
#print data[0]['local_time']
#print data[0]['name']


