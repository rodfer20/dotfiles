#!/bin/sh
if [[ -z "$1" || -z "$2" ]]; then
    echo "Usage ./ssl_server <host> <port>"
    exit 1
fi
HOST="$1"
PORT=$2
openssl s_client -connect $HOST:$PORT
