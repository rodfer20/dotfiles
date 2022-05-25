#!/usr/bin/python3


import time
import sys


def get_bytes(t, iface='wlan0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read();
        return int(data)


if __name__ == '__main__':
    (tx_prev, rx_prev) = (0, 0)
    try:
        while(True):
            flag = False
            output = ''
            tx = get_bytes('tx')
            rx = get_bytes('rx')
            if tx_prev > 0:
                tx_speed = tx - tx_prev
                output += f'[TX: {tx_speed} bps]'
            else:
                output += '[TX: 0 bps]'
            if rx_prev > 0:
                rx_speed = rx - rx_prev
                output += f' [RX: {rx_speed} bps]'
            else:
                output += ' [RX: 0 bps] '
            time.sleep(1)
            tx_prev = tx
            rx_prev = rx
            print(output)
    except KeyboardInterrupt:
        sys.stdout.flush()
        exit(0)
