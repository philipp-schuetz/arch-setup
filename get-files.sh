#!/bin/bash

# -------- home --------
cp ~/.gitconfig files/configs/home
cp ~/.p10k.zsh files/configs/home
cp ~/.zshrc files/configs/home
cp ~/.zshrc.pre-oh-my-zsh files/configs/home

# -------- configs --------
cp -R ~/.config/alacritty files/configs/config
cp -R ~/.config/gtk-3.0 files/configs/config
cp -R ~/.config/picom files/configs/config
cp -R ~/.config/qtile files/configs/config