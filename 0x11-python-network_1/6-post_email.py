#!/usr/bin/python3
""" This script takes a POST request to passed URL with email"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    req_data = requests.post(url, {"email": email})
    print(req_data.text)
