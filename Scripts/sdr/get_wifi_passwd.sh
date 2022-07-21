#!/bin/sh
WIFI_NAME="$1"
if [ -z "$WIFI_NAME" ]; then
    exit 1
fi
security find-generic-password -ga "$WIFI_NAME" | grep “password:”
