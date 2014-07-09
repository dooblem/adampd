#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-

# A small MPD client to watch button events on AdaFruit CharLCD display
# for raspberry pi

import mpd,time,sys,os
sys.path.append(os.path.dirname(__file__)+'/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate')
import Adafruit_CharLCDPlate

lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()

client = mpd.MPDClient()
client.connect("localhost", 6600)

# adafruit lib is not interrupt-driven so we have to set a loop
# https://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi/usage#using-the-library-code
# drawback is that sleeping .2s consumes cpu
# so we place a idletime counter. if idle (no button pressed) for more than 60s :
#   if playing, keep .2s
#   if not playing anymore, set nap to 5s
# drawbacks: - we may wait a minute before the buttons to be active if set playing by another client
#            - you have to keep a button pressed some seconds to "wake up" the script

idletime = 3600

while True:
	press = False

	#print(repr(client.status()))
	if lcd.buttonPressed(lcd.SELECT):
		press = True
		print("select")
		if client.status()["state"] == "play":
			client.pause(1)
		else:
			client.pause(0)

	elif lcd.buttonPressed(lcd.LEFT):
		press = True
		print("left")
		client.previous()

	elif lcd.buttonPressed(lcd.RIGHT):
		press = True
		print("right")
		client.next()

	elif lcd.buttonPressed(lcd.UP):
		press = True
		print("up")

	elif lcd.buttonPressed(lcd.DOWN):
		press = True
		print("down")
	
	if press:
		nap = .2
		time.sleep(1)
		idletime = 0

	if idletime > 60:
		idletime = 0
		if client.status()["state"] == "play":
			print("naptime to .2s...")
			nap = .2
		else:
			print("naptime to 5s...")
			nap = 5

	idletime+= nap
	time.sleep(nap)
