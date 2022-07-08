#!/usr/bin/python3


from datetime import date
import sys
import os 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)
    device = sys.argv[1]

    _dirs = list() 
    with open("backup.txt", 'r') as fp:
        _dirs = fp.read().splitlines()
    dirs = " ".join([_dir for _dir in _dirs])
    
    sys.stdout.write("[*] Starting backup process...")
    date = date.today()
    
    sys.stdout.write("[*] Compressing into tarball ...")
    os.system(f"tar -cf backup-{date}.tar.gz {dirs}")
    
    sys.stdout.write("[*] Generating SHA1 sum ...")
    os.system("shasum -a 1 backup-{date}.tar.gz | cat > backup-{date}.sha1")
    
    sys.stdout.write(f"[*] Copying into device {device} ...")
    os.system("sudo cp -r backup-{date}.tar.gz {device}")
    os.system("sudo cp backup-{date}.shasum1 {device}")
    
    sys.stdout.write("[*] Done!")
    exit(0)
