#!/usr/bin/python3
""" This script sends request to URL and displays value of response header"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    a = requests.get(url)
    print(a.headers.get("X-Request-Id"))
