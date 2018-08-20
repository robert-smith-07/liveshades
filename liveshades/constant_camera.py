import picamera
import os
import glob

#remove any remaining old clips
clips = glob.glob("/home/pi/clip*.h264")
for clip in clips:
    os.remove(clip)

#set up camera
with picamera.PiCamera() as camera:
    for filename in camera.record_sequence(
            'clip%02d.h264' % i for i in range(240)):
        print('Recording to %s' % filename)
        camera.wait_recording(30);
