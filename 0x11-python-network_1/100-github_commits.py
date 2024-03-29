#!/usr/bin/python3
"""This script takes two args to solve challenge"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])

    a = requests.get(url)
    commits = a.json()
    try:
        for b in range(10):
            print("{}: {}".format(commits[b].get("sha"),
                                  commits[b].get("commmit").get("author").get(
                                      "name")))
    except IndexError:
        pass
