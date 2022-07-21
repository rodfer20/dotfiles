#!/bin/sh
if [ -z "$1"]; then
    echo "Usage ./ssl_server <key.pem> <cert.pem> <port>"
    exit 1
fi
PORT=$1
KEY="$2"
CERT="$3"
if [ -z "$2" ]; then
    KEY="key.pem"
fi
if [ -z "$3" ]; then
    CERT="cert.pem"
fi
openssl s_server -key $KEY -cert $CERT -accept $PORT
