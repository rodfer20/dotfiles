#!/usr/bin/python3


import os
import sys
import time
import subprocess


if __name__ == '__main__':
    if os.geteuid != 0:
        print("[+] Script must have root previligies ")
        cmd = "sudo echo '1337' >> /dev/null"
        os.system(cmd)
    try:
        print("[+] Checking connection ... ")
        cmd = "ping gnu.org -c 5".split(" ")
        output = subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if output == 2:
            print("[+] Restarting connection ... ")
            cmd = "sudo systemctl restart iwd".split(" ")
            subprocess.call(cmd)
            time.sleep(3)
            cmd = "sudo systemctl restart dhcpcd".split(" ")
            subprocess.call(cmd)
            time.sleep(2)
            try:
                print("[+] Verifying connection ... ")
                cmd = "ping gnu.org -c 5".split(" ")
                output = subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                if output == 2:
                    sys.stderr.write("[!] Failed to setup connection\n")
                    exit(1)
            except:
                print("[!] Verification failed ")
                sys.stderr.write("[!] Failed to setup connection\n")
                exit(1)
    except:
        print("[+] Restarting connection ... ")
        cmd = "sudo systemctl restart iwd".split(" ")
        subprocess.call(cmd)
        time.sleep(2)
        cmd = "sudo systemctl restart dhcpcd".split(" ")
        subprocess.call(cmd)
        time.sleep(3)
        try:
            print("[+] Verifying connection ... ")
            cmd = "ping gnu.org -c 5".split(" ")
            _ = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            print("[!] Verification failed ")
            sys.stderr.write("[!] Failed to setup connection\n")
            exit(1)
    print("[*] Connection estabilished ")
    exit(0)
    
