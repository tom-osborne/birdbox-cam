#!/usr/bin/env python3 
import subprocess

print("Started BirdBox Cam v0.1")

raspivid_cmd = 'raspivid -o - -t 0 -a 1036 -a "%Y-%m-%d" -vf -hf -fps 30 -b 6000000'
ffmpeg_cmd = "ffmpeg -re  -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128000 -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/7ytq-b3uh-xrr5-0hmu-6x61"
stream_cmd = raspivid_cmd + ' | ' + ffmpeg_cmd

stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE) 
