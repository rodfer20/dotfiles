import sys
import requests


def get_url():
    if len(sys.argv) != 2:
        return "[x] Error parsing arguments: <url> not passed to call"
    return argv[1]


def get_call(url):
    err = False
    res = requests.get(url)
    if res.status_code != 200:
        err = True
        return f"[x] Response status code: res.status_code", err
    return res, err
