import RPi.GPIO as GPIO
import glob
import time
import os
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#remove old clips file
try:
    os.remove('clips.txt')
except OSError:
    pass


while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        
        # read the directory and find the most recent clips
        clips = sorted(glob.glob("*.h264"))
        print(clips)


        current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        #get the last 6 clips / 3 minutes
        last_clips = clips[-6:]
        print(last_clips)
        clip_txt_name = 'clips_' + current_time + '.txt'

        f = open(clip_txt_name, "a")
        for clip in last_clips:
            f.write("file '%s'\n"%(clip))
        f.close()
        time.sleep(2)
            
        # write these to a file to prepare for ffmpg concat
        os.system('ffmpeg -f concat -safe 0 -i %s -c copy %s.h264'%(clip_txt_name, current_time))

        # debounce button
        time.sleep(3)
