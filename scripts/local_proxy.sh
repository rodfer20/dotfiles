#!/bin/sh

if [ -z "$1" ]; then
    echo "[!] Toggle proxy on/off is required"
    exit 1
fi

    export http_proxy=http://10.10.10.10:1194/
    export https_proxy=$http_proxy
    export ftp_proxy=$http_proxy
    export rsync_proxy=$http_proxy
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
    exit 0
fi

if [[ "$1" -eq "-o" ]]; then
    if [ -z "$2"]; then
        echo "[*] Proxy on"
    fi
    
    if [[ "$2" -eq "-i" ]]; then
        echo "[*] Interception proxy on"
    fi

    export http_proxy=http://127.0.0.1:8080/
    export https_proxy=$http_proxy
    export ftp_proxy=$http_proxy
    export rsync_proxy=$http_proxy
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
    exit 0
fi
