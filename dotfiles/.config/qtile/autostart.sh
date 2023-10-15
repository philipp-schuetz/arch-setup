#!/bin/sh

picom -b &

conky -c "$HOME"/.config/conky/mocha.conf
