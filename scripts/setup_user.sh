#!/bin/sh

useradd webserver 
passwd webserver
usermod -aG sudo webserver
usermod --shell /bin/bash webserver 
echo "[*] User information:"
cat /etc/passwd | grep webserver || echo "[x] Error setting user account"
echo "[*] Permissions informations:"
sudo -l -U webserver | grep "ALL" || echo "[x] Error setting user permissions"
