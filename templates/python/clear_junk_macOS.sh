#!/usr/bin/python3

from os import listdir, chdir, environ, remove
from os.path import isdir


def clear(path: str):
    blacklist = ["Applications", "Library", ".Trash"]
    microsoft = f"{path}/workspace.code-workspace"
    apple = f"{path}/.DS_Store"
     
    ls = listdir(path)
    for dir_path in ls:
        if f"{path}/{dir_path}" == microsoft or f"{path}/{dir_path}" == apple:
            print(f"Deleted file {path}/{dir_path}")
            remove(f"{path}/{dir_path}")
    for dir_path in ls:
        if isdir(f"{path}/{dir_path}") and dir_path not in blacklist:    
            clear(f"{path}/{dir_path}")

if __name__ == "__main__":
    home = environ["HOME"]
    clear(home) 
    
