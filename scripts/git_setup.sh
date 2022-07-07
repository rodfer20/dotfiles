#!/bin/sh
DIR=~/Scripts
if [ ! -d "$DIR" ]; then
    mkdir ~/Scripts
fi
cp ~/trevalkov_configs/configs/git/git_push.sh ~/Scripts
echo 'alias push="~/Scripts/git_push.sh"' >> ~/.zshrc
echo "[*] Successfully setup git_push.sh script"
echo "[+] Run 'source ~/.zshrc' to update the changes"
