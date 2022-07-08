#!/usr/bin/python3
import os


USER = "kali"
HOST = "127.0.0.1"
PORT = 6622
KEY_LOCAL = "~/Virtualbox/Kali/.ssh/id_rsa"
VM_NAME = "Kali"


if __name__ == '__main__':
    while True:
        print("="*16)
        print(f"[BOX] :: {VM_NAME} {HOST}:{PORT}")
        print(f"[ID] :: {USER} {KEY_LOCAL}")
        print("="*16)
        print("5. poweroff")
        print("4. pause")
        print("3. resume")
        print("2. start")
        print("1. ssh")
        print("0. quit")
        print("="*16)
        s = input(">>> ")
        try:
            c = int(s)
        except ValueError:
            exit(1)
        if c == 0:
            exit(0)
        elif c == 1:
            os.system(f"ssh -p {PORT} -i {KEY_LOCAL} {USER}@{HOST}")
        elif c == 2:
            os.system(f"VBoxManage startvm '{VM_NAME}' --type headless")
        elif c == 3:
            os.system(f"VBoxManage controlvm '{VM_NAME}' resume --type headless")
        elif c == 4:
            os.system(f"VBoxManage controlvm '{VM_NAME}' pause --type headless")
        elif c == 5:
            os.system(f"VBoxManage controlvm '{VM_NAME}' poweroff --type headless")
