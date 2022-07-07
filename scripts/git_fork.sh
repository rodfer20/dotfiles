#!/bin/sh

read -r -p "[+] Branch name: " branch && \
    git checkout -b $branch && \
    git add . && \
    read -r -p "[+] Commit description: " desc && \
    git commit -m "$desc" && \
    git push --set-upstream origin $branch && \
    echo "[*] Successfully pushed changes"

