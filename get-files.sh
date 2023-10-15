#!/bin/bash

rm -rf dotfiles/*
rm -rf configs/*
mkdir -p dotfiles/.config
mkdir -p configs

# -------- home --------
cp ~/.gitconfig dotfiles
cp ~/.zshrc dotfiles

# -------- configs --------
cp -R ~/.config/alacritty dotfiles/.config/
cp -R ~/.config/btop dotfiles/.config/
cp -R ~/.config/cava dotfiles/.config/
cp -R ~/.config/conky dotfiles/.config/
cp -R ~/.config/flameshot dotfiles/.config/
cp -R ~/.config/gtk-2.0 dotfiles/.config/
cp -R ~/.config/gtk-3.0 dotfiles/.config/
cp -R ~/.config/neofetch dotfiles/.config/
cp -R ~/.config/nvim dotfiles/.config/
cp -R ~/.config/pavucontrol.ini dotfiles/.config/
cp -R ~/.config/picom dotfiles/.config/
cp -R ~/.config/qtile dotfiles/.config/
cp -R ~/.config/rofi dotfiles/.config/

cp /etc/pacman.conf configs/pacman.conf
