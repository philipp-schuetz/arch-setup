#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: no username provided"
  exit 1
fi

user=$1

echo "setting up arch for $user"

# copy system configs
cp configs/pacman.conf /etc/pacman.conf

# install yay
pacman -S git yay

# install packages from package list
while read -r package; do
  if [ -n "$package" ]; then
    yay -S "$package"
  fi
done < "packages.txt"

# copy dotfiles
cp -R dotfiles/* ~/

# enable ly
sudo systemctl enable ly.service


# user configuration
usermod -aG video,audio $user
sudo chsh -s /bin/zsh $user
