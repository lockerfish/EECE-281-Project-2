#!/usr/bin/python

import time
import RPi.GPIO as GPIO # Import GPIO library
import picamera
from subprocess import call
from datetime import datetime
from imgurpython import ImgurClient

newImagesAlbum = 'V6d9g'

client_id = '7d93686adde0c8d'
client_secret = '9bbd8aa21c99a00ec2f5319ea2271f614f29fb33'
access_token = '98fc8cd909ba029bd210cf0a7c76c5609f51278a'
refresh_token = 'f02874b84943949c43c927cf30f8eebbe299494b'
client = ImgurClient(client_id, client_secret, access_token, refresh_token)
config = {
        'album': newImagesAlbum, # album ID or None
        'name': 'Test',
        'title': 'Test',
        'description': 'Whizzards are cool'
}

GPIO.setmode(GPIO.BCM) # T-cobbler setup in BCM mode
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Setup GPIO Pin 5 OUT
camera = picamera.PiCamera() # create instance of camera class

while (True): #GPIO.output(5,True) ## Turn on GPIO pin 5
        if (GPIO.input(5) == 1):
		i = datetime.now()               #take time and date for filename  
		now = i.strftime('%Y%m%d-%H%M%S')
		photo_name = "images/" + now + '.jpg'
		camera.capture(photo_name)
		image = client.upload_from_path(photo_name, config=config, anon=False)

# if not using infinite loop, call camera.close() at end of usage to conserve resources

	
