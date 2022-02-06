#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script
sleep 5

# raspivid -o - -t 0 -vf -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm
cd home/pi/birdbox-cam/
sudo python main.py
cd /