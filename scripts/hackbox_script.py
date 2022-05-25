#!/usr/bin/python3

import os, sys, time


if __name__ == '__main__':
    try:
        cmd = "~/vms/hackbox/run-hackbox.sh"
        if os.system(cmd) == 2:
            cmd = "~/vms/hackbox/build-hackbox.sh"
            os.system(cmd)
            cmd = "~/vms/hackbox/run-hackbox.sh"
            os.system(cmd)
    except Exception as e:
        sys.stderr.write(f"[!] Caught exception: {e}\n")
        exit(1)
    exit(0)
