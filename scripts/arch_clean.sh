#!/bin/sh

yes | sudo pacman -Syyu
sudo pacman -Rscn $(yay -Qtdq)
# updatedb
sudo pkgfile -u
sudo pacman -Fyy
sudo pacman-db-upgrade
yes | sudo pacman -Scc
sudo sync
