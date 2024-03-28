#!/usr/bin/python3
""" This script takes in url an email, sends a POST request"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    req = Request(url, data)
    with urlopen(req) as it:
        print(it.read().decode("utf-8"))
