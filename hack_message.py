#!/usr/bin/env python

import urllib2,re,pygeoip,json
import os
import twilio
from twilio.rest import TwilioRestClient
import pygame
import pygame.camera

TWILIO_ACCOUNT_SID="YOUR_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="YOUR_AUTH_TOKEN"

new=open("/home/yash/auth",'r')
for i in new:
	length1=len(i)
new.close()

new_file=open("/home/yash/auth",'w')
f=open("/var/log/auth.log",'r')
text=f.read()
failed=re.findall(r'failed|FAILED',text)
new_file.write(str(failed))
new_file.close()

new2=open("/home/yash/auth",'r')
for i in new2:
	length2=len(i)
new2.close()

if length2>length1:
	ip_url=urllib2.urlopen("http://whatismyip.org").read()
	ip_search=re.search(r'\d+.\d+.\d+.\d+',ip_url)
	ip=ip_search.group()

	url="http://www.freegeoip.net/json/"+ip
	location=urllib2.urlopen(url).read()
	data=json.loads(location)
	hack_message="City: "+data['city']+\
	", Country: "+data['country_name']+\
	", IP: "+data['ip']+\
	", Latitude: "+str(data['latitude'])+\
	", longitude: "+str(data['longitude'])+\
	", zipcode: "+str(data['zip_code'])
	
	pygame.camera.init()
	pygame.camera.list_cameras()
	cam = pygame.camera.Camera("/dev/video0", (640, 480))
	cam.start()
	img = cam.get_image()
	pygame.image.save(img, "/home/yash/logs/pygame.jpg")
	cam.stop()

	client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
	message=client.messages.create(
	body="Someone is trying to break into your laptop. The details are: "+hack_message, 
	to="YOUR_CONTACT_NUMBER", 
	from_="YOUR_TWILIO_PHONE_NUMBER")
	
try:
    logs=open('logs/file.txt', 'a')
except IOError as e:
    # dir & file don't exist; create them
    os.mkdir('logs')
    logs=open('logs/file.txt', 'a')
except Exception as e:
    print e
else:
    pass

# log it
logs.write("Message with sid {} sent at {}".format(message.sid,strftime("%a, %d %b %Y %H:%M:%S") + "\n"))
logs.close()
