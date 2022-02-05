#!/usr/bin/env python3 
import subprocess 
import picamera 
import time 

print("Started BirdBox Cam v0.1")

# ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i hw:1,0 -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32k -map 0:0 -map 1:0 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/7ytq-b3uh-xrr5-0hmu-6x61
# raspivid -o - -t 0 -vf -hf -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128000 -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/7ytq-b3uh-xrr5-0hmu-6x61
YOUTUBE="rtmp://a.rtmp.youtube.com/live2/" 
KEY="7ytq-b3uh-xrr5-0hmu-6x61"
stream_cmd = 'raspivid -o - -t 0 -vf -hf -fps 30 -b 6000000 | ffmpeg -f h264 -r 25 -i - -itsoffset 5.5 -fflags nobuffer -f alsa -ac 1 -i /dev/zero -vcodec copy -acodec aac -ac 1 -ar 8000 -ab 32000 -map 0:0 -map 1:0 -strict experimental -f flv ' + YOUTUBE + KEY 
stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE) 
# # camera = picamera.PiCamera(resolution=(640, 480), framerate=25) 
# try: 
#   now = time.strftime("%Y-%m-%d-%H:%M:%S") 
#   camera.framerate = 25 
#   camera.vflip = True 
#   camera.hflip = True 
#   camera.start_recording(stream.stdin, format='h264', bitrate = 2000000) 
#   while True: 
#      camera.wait_recording(1) 
# except KeyboardInterrupt: 
#      camera.stop_recording() 
# finally: 
#   camera.close() 
#   stream.stdin.close() 
#   stream.wait() 
#   print("Camera safely shut down") 