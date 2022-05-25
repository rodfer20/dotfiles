#!/bin/sh
CWD="/home/trevalkov/images"
TIMESTAMP="$(date +%H:%M:%S_%d-%m-%Y).png"
import -window root "$CWD/$TIMESTAMP"
