AdaMPD
======

MPD clients for AdaFruit Character LCD Keypad and Raspberry Pi


2 python daemons:
 * ada-screen.py - displays the currently playing song and artist on LCD screen
 * ada-buttons.py - watch for buttons pressed and do some MPD actions

ada-screen.py:
 * you can set a Favorite playlist, to have the backlight of a different color if a favorite song is playing.
 * you can also set the default color

ada-buttons.py:
 * select: play/pause, right/left: next/previous song, up/down: volume
 * after some idle time not playing, you have to press buttons for some seconds to wake up the keypad, this is for cpu economy

Usage on Raspbian
------------------------

apt-get install git python-mpd

cd /root
git clone https://github.com/dooblem/adampd
cd adampd

# get adafruit lib
git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

# to test interactively:
./ada-screen.py
./ada-buttons.py

# to setup the init script
ln -s /root/adampd/adampd /etc/init.d/adampd
insserv adampd 
