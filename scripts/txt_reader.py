#!/usr/bin/python3

import os, sys, subprocess


def setup():
    configs = dict()

    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: ./txt_reader.py <resource_path>\n")
        exit(1)

    configs["resource_path"] = sys.argv[1]
    return configs


def parse_resource(resource_path):
    resources = dict() # dict(len_category * category: list(category_resources)
    categories = list() # list(len_category * category)
    links = list() # list(len_categories * list(links))

    with open(resource_path, 'r') as fp:
        for line in fp.read().splitlines():
            print(line)
            try:
                category, link = line.split(" -- ")
            except Exception:
                category = line
                link = ""
            categories.append(category)
            links.append(link)

    if len(categories) != len(links):
        sys.stderr.write("[!] Wrong parsing style: 'category -- link'\n")
        exit(1)

    i = 0
    for category in categories:
        resources[category] = links[i]
        i += 1
    return resources


def reader_cli(resources, handle=0):
    print('\033c')
    i = 0
    for category, link in resources.items():
        print(f"{i+1}: {category}: {link}")
        i += 1
    
    c = input(">>> ")
    if c == "q" or c == "quit":
        print("[*] Gracefully quitting ... ")
        exit(0)
    
    elif c == "r":
        print('\033c')
        reader_cli(resources, handle)
    elif c == "b":
        print(c) 
        reader_cli(resources, 0)
    
    elif c == "j":
        print("down")
    
    elif c == "k":
        print("up")
    
    else:
        try:
            c = int(c)
        except:
            print("menu")
            print("[!] Invalid command")
            time.sleep(2)
            return reader_cli(resources, handle)
    
        link = list(resources.values())[c-1]
    return link, handle


def open_resource(link):
    try:
        browser = os.environ["BROWSER"]
    except KeyError:
        browser = "firefox"
    finally:
        cmd = f"{browser} {link}"
        try:
            subprocess.call(cmd.split(" "), stderr=subprocess.DEVNULL)
        except Exception as e:
            sys.stderr.write(f"[!] Error: {e}\n")
    return 0


def bootstrap():
    configs = setup()
    resource_path = configs["resource_path"]
    
    resources = parse_resource(resource_path)
    handle = 0
    while True:
        link, handle = reader_cli(resources, handle)
        open_resource(link)
    
    exit(0)


if __name__ == "__main__":
    bootstrap()

