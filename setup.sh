#!/bin/bash

# -------- install software --------
# install yay
sudo pacman -S git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay

# install needed packages
sudo pacman -S alacritty nitrogen dmenu btop tree neofetch man-db vim zsh curl git
yay -S picom ly

# -------- git --------
# copy git config
cp files/configs/home/.gitconfig ~

# -------- wallpaper --------
# copy background image
cp -R files/configs/config/wallpaper ~/.config

# set background image
nitrogen --set-zoom-fill ~/.config/wallpaper/flower.jpg


# -------- alacritty --------
# copy config
cp -R files/configs/config/alacritty ~/.config


# -------- gtk --------
# copy config
cp -R files/configs/config/gtk-3.0 ~/.config


# -------- picom --------
# copy config
cp -R files/configs/config/picom ~/.config


# -------- qtile --------
# copy config
cp -R files/configs/config/qtile ~/.config


# -------- display manager --------
# remove dm installed with archinstall (systemctl disable also works)
sudo pacman -Rns lightdm lightdm-gtk-greeter
sudo rm /etc/systemd/system/display-manager.service

# enable new dm
sudo systemctl enable ly.service


# -------- shell --------
# set zsh as shell
sudo chsh -s /bin/zsh
# usermod -s /bin/zsh

# install oh my zsh
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# install fonts for p10k
cp -R files/fonts ~/.local/share

# install p10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# copy zsh config files
cp files/configs/home/.zshrc ~
cp files/configs/home/.zshrc.pre-oh-my-zsh ~
cp files/configs/home/.p10k.zsh ~

exec zsh

echo "--------done--------"
echo "if the shell looks strange, maybe run 'p10k reconfigure'"
