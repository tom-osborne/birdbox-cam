#!/usr/bin/env python3 
import subprocess
import time
import config

print("Started BirdBox Cam v0.1")

raspivid_cmd = 'raspivid -o - -t 0 -a 1036 -a "%Y-%m-%d %H:%M:%S" -n -fps 30 -b 4500000'
ffmpeg_cmd = f"ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/{config.STREAM_KEY}"
stream_cmd = raspivid_cmd + ' | ' + ffmpeg_cmd

stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE) 
