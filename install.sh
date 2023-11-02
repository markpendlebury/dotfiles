#!/bin/zsh

# quick start symlinking configs
# I'll make this better in the future 


sudo apt update 
sudo apt install -y $applicationList rofi qtile picom


for d in .config/* ; do
    echo "ln -s $PWD/$d ~/.config/$d"
done