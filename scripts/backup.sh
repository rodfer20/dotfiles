#!/bin/sh

if [ -z "$MNT_PATH" ]; then
    if [ -z "$1" ]; then
        echo "[!] MNT_PATH not set and required e.g. /mnt/backup-device"
        exit
    fi
    MNT_PATH=$1
fi
cd "$HOME" && \
    echo "[*] Starting backup process ..."
    DATE="$(date +%d-%m-%Y)" &&\
    echo "[*] Compressing into tarball ..." &&\
    tar -cf "backup-$DATE.tar.gz" dotfiles docs proggies proxies templates lists workspace music vms scripts &&\
    echo "[*] Generating shasum1 ..." &&\
    shasum -a 1 "backup-$DATE.tar.gz" | cat > "backup-$DATE.sha1" &&\
    echo "[*] Coppying into device $1 ..." &&\
	sudo cp -r "backup-$DATE.tar.gz" "$MNT_PATH" &&\
    sudo cp "backup-$DATE.sha1" "$MNT_PATH"
