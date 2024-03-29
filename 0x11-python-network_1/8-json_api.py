#!/usr/bin/python3
""" This script takes in a letter and sends POST request to localhost"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}
    a = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        it = a.json()
        if it == {}:
            print("No result")
        else:
            print("[{}] {}".format(it.get("id"), it.get("name")))
    except ValueError:
        print("Not a valid JSON")
