#!/bin/bash

user="philipp"

# -------- install software --------
# install yay
sudo pacman -S --noconfirm git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si --noconfirm
cd ..
rm -rf yay

# install needed packages
sudo pacman -S --noconfirm alacritty dmenu btop tree neofetch man-db vim zsh curl git firefox discord
yay --noprovides --answerdiff None --answerclean None --mflags "--noconfirm" -S picom ly

# -------- git --------
# copy git config
cp files/configs/home/.gitconfig ~


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
sudo pacman --noconfirm -Rns lightdm lightdm-gtk-greeter
sudo rm /etc/systemd/system/display-manager.service

# enable new dm
sudo systemctl enable ly.service


# -------- shell --------
# set zsh as shell
sudo chsh -s /bin/zsh $user

# install oh my zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# install fonts for p10k
cp -R files/fonts ~/.local/share

# install p10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# copy zsh config files
cp files/configs/home/.zshrc ~
cp files/configs/home/.zshrc.pre-oh-my-zsh ~
cp files/configs/home/.p10k.zsh ~

echo ""
echo ""
echo "--------done--------"
echo "if the shell looks strange, maybe run 'p10k reconfigure' after the reboot"

read -p "Press enter to exit and reboot now"
sudo shutdown -r now


