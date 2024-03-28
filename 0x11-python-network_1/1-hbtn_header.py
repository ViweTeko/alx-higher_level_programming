#!/usr/bin/python3
""" This script sends request to URL and displays value of X-Request-Id"""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    with urlopen(req) as it:
        print(dict(it.headers).get("X-Request-Id"))
