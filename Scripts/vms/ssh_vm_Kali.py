#!/usr/bin/python3

import os
import sys
import time
import random

# Settings
USER = "kali"
HOST = "127.0.0.1"
PORT = 6622
KEY_LOCAL = "~/Virtualbox/Kali/.ssh/id_rsa"
VM_NAME = "Kali"

# Errors
SSH_CON_REFUSED = 65280

# Configs
#PWD = "/".join([n for n in __file__.split('/')[:-1]])+"/"
#with open(f"{PWD}/{__file[:-3]}.cfg", 'rw') as fp:
#    cfg_in = fp.read().splitlines()
#VM_LIVE = cfg_in[1].split("=")[2][1:]

def gen_random_ascii_string(n: int):
    chars = list(map(chr, range(97, 123)))
    digits = list(map(chr, range(48, 58)))
    s = chars + digits
    s_size = len(s)-1
    ss = ""
    for i in range(n):
        ss = ss + s[random.randint(0,s_size)]
    return ss

def start_vm():
    return os.system(f"VBoxManage startvm '{VM_NAME}' --type headless")

def ssh_vm():
    return os.system(f"ssh -p {PORT} -i {KEY_LOCAL} {USER}@{HOST}")

def resume_vm():
    return os.system(f"VBoxManage controlvm '{VM_NAME}' resume --type headless")

def pause_vm():
    return os.system(f"VBoxManage controlvm '{VM_NAME}' pause --type headless")
           
def poweroff_vm():
    return os.system(f"VBoxManage controlvm '{VM_NAME}' poweroff --type headless")

def take_snapshot(snapshotName="", snapshotDescription=""):#: str, caseLive: str):
    if not snapshotName:
        snapshotName = gen_random_ascii_string(32)
    return os.system(f"VBoxManage snapshot '{VM_NAME}' take {snapshotName} --description='{snapshotDescription}'")# {caseLive}")

def display_menu():
    print("="*16)
    print(f"[BOX] :: {VM_NAME} {HOST}:{PORT}")
    print(f"[ID] :: {USER} {KEY_LOCAL}")
    print("="*16)
    print("6. snapshot")
    print("5. poweroff")
    print("4. pause")
    print("3. resume")
    print("2. start")
    print("1. ssh")
    print("0. quit")
    print("="*16)
    return 0


def get_user_input():
    s = input(">>> ")
    try:
        c = int(s[0])
    except ValueError:
        return -1
    return c


def run_menu(c: int):
    global VM_LIVE, SSH_CON_REFUSED
    if c < 0:
        exit(1)
    elif c == 0:
        exit(0)
    elif c == 1:
        e = ssh_vm()
        if e == SSH_CON_REFUSED:
            start_vm()
            while e == SSH_CON_REFUSED:
                time.sleep(2)
                e = ssh_vm()
    elif c == 2:
        start_vm
    elif c == 3:
        resume_vm()
    elif c == 4:
        pause_vm()
    elif c == 5:
        poweroff_vm()
    elif c == 6:
        #if VM_LIVE:
        #    caseLive = "--live"
        #else:
        #    caseLive = ""
        snapshotName = input("Snapshot Name: ")
        snapshotDescription = input("Snapshot Description: ")
        take_snapshot(snapshotName, snapshotDescription)

    else:
        exit(1)

if __name__ == '__main__':
    while True:
        display_menu()
        c = get_user_input()
        run_menu(c)
    exit(0)
