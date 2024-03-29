#!/usr/bin/python3
""" This script takes in url, sends request to it and displays body response"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]

    req = Request(url)
    try:
        with urlopen(req) as it:
            print(it.read().decode("ascii"))
    except HTTPError as er:
            print("Error code: {}".format(er.code))
