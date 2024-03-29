#!/usr/bin/python3
""" This script sends request to URL and displays error code"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    a = requests.get(url)
    if a.status_code >= 400:
        print("Error code: {}".format(a.status_code))
    else:
        print(a.text)
