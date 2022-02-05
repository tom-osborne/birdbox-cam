#!/usr/bin/env python3 
import subprocess
import time 

print("Started BirdBox Cam v0.1")


raspivid_cmd = 'raspivid -o - -t 0 -a 1024 -a "%Y-%m-%d %X" -vf -hf -fps 30 -b 6000000'
ffmpeg_cmd = 'ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -use_wallclock_as_timestamps 1 -acodec aac -ab 128000 -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/7ytq-b3uh-xrr5-0hmu-6x61'
stream_cmd = raspivid_cmd + ' | ' + ffmpeg_cmd

# stream_cmd_video = "v4l2-ctl -d /dev/zero --set-ctrl=exposure_dynamic_framerate=1 --set-ctrl=scene_mode=8 -v width=1296,height=960,pixelformat=YU12 | "
# stream_cmd_ffmpeg = "ffmpeg -f rawvideo -pix_fmt yuv420p -video_size 1296x960 -use_wallclock_as_timestamps 1 -i /dev/zero -bsf h264_metadata=tick_rate=60 -vf 'pad=h=(in_h+5+32), drawtext=x=(w-tw-8):y=(h-28):fontcolor=white:fontsize=28:text=%{localtime}, drawtext=x=8:y=(h-28):fontcolor=white:fontsize=28:textfile=/tmp/cam_hostname, drawtext=x=32:y=(h-28):fontcolor=white:fontsize=28:textfile=/tmp/cam_msg:reload=1' -vsync 1 -r 30 -c:v h264_v4l2m2m -b:v 5M -an -f flv rtmp://a.rtmp.youtube.com/live2/7ytq-b3uh-xrr5-0hmu-6x61"
# stream_cmd = stream_cmd_video + stream_cmd_ffmpeg

stream_pipe = subprocess.Popen(stream_cmd, shell=True, stdin=subprocess.PIPE) 
