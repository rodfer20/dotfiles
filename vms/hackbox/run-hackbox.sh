#!/bin/sh
sudo docker run \
    --rm \
    -it \
    -v ~/vms/hackbox/opt/:/host/ \
    hackbox
