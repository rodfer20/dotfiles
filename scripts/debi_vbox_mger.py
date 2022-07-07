#!/usr/bin/python3


import os


USER = "trevalkov"
PORT = 4422
VM_NAME = "debi"


if __name__ == '__main__':
    while True:
        print("5. poweroff")
        print("4. pause")
        print("3. resume")
        print("2. start")
        print("1. ssh")
        print("0. quit")
        s = input(">>> ")
        try:
            c = int(s)
        except ValueError:
            exit(1)
        if c == 0:
            exit(0)
        elif c == 1:
            os.system(f"ssh -p {PORT} {USER}@localhost")
        elif c == 2:
            os.system(f"VBoxManage startvm '{VM_NAME}' --type headless")
        elif c == 3:
            os.system(f"VBoxManage controlvm '{VM_NAME}' resume --type headless")
        elif c == 4:
            os.system(f"VBoxManage controlvm '{VM_NAME}' pause --type headless")
        elif c == 5:
            os.system(f"VBoxManage controlvm '{VM_NAME}' poweroff --type headless")
