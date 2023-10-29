#!/bin/bash

# set keyboard layout:
setxkbmap -layout us 

# start picom
picom -b --config ~/.config/picom/picom.conf &

#  load nvidia settings
nvidia-settings --load-config-only &