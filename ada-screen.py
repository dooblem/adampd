#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-

# A small MPD client to display the current song on AdaFruit CharLCD display
# for raspberry pi
# you should install the python-mpd debian package
# and git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

import mpd,time,sys,os
sys.path.append(os.path.dirname(__file__)+'/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate')
import Adafruit_CharLCDPlate

print("creating adalcd object...")
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()

# Some settings
# backlight colors
#col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
#       lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
NORMAL_COLOR = lcd.TEAL
#FAVORITE_PLAYLIST = "Favoris"
FAVORITE_PLAYLIST = ""
FAVORITE_COLOR = lcd.VIOLET

print("connecting to mpd...")
client = mpd.MPDClient()
client.connect("localhost", 6600)

time.sleep(1)

def cleanforlcd(s):
	s = s.replace("é","e")
	s = s.replace("è","e")
	s = s.replace("ê","e")
	s = s.replace("ë","e")
	s = s.replace("à","a")
	return s.decode("utf8").encode("ascii", errors='replace')

while True:
	status = client.status()

	if status["state"] == "play":
		song = client.currentsong()
		print(repr(song))

		# get artist and title, fallback on path items
		if "artist" in song:
			line1 = song["artist"]
		else:
			line1 = song["file"].split("/")[0]
		if "title" in song:
			line2 = song["title"]
		else:
			line2 = song["file"].split("/")[-1]

		lcd.clear()
		lcd.message(cleanforlcd(line1+"\n"+line2))

		if FAVORITE_PLAYLIST != "" and song["file"] in client.listplaylist(FAVORITE_PLAYLIST):
			print("fav color")
			lcd.backlight(FAVORITE_COLOR)
		else:
			print("normal color")
			lcd.backlight(NORMAL_COLOR)
	else:
		print("off")
		lcd.backlight(lcd.OFF)
		lcd.clear()

	print("idling for event...")
	subsys = client.idle()
