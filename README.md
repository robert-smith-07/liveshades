# liveshades

This project uses a Raspberry Pi with a camera module to become an always on, small camera. 

Meant to be used attached to glasses, but can fit in a pocket as well.

At the press of a button last few minutes of video are recorded. 

The button is soldered to Pins 12 (GPIO 18) and 6 on a Raspberry Pi 3. 

This pin location can be changed in button.py

Because this uses the picamera library most Pi cameras should work.

TODO: 

Push the auto start daemon for the script

Pi Zero compatability 

Audio muxing from USB microphone 

Auto share over Wifi, even by cell phone tethering

Starting camera with voice, accelerometer to be more covert

