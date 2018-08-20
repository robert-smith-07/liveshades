import glob
import threading
import os

def remove_clips():
    clips = glob.glob('/home/pi/clip*.h264')
    if len(clips) >= 10:
        first_clips = clips[:-10]
        for clip in first_clips:
            os.remove(clip)

threading.Timer(60.0, remove_clips).start()

