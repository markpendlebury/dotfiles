#!/bin/zsh

# quick start symlinking configs
# I'll make this better in the future 

for d in .config/* ; do
    echo "ln -s $PWD/$d ~/.config/$d"
done