#!/usr/bin/python3
"""This script takes your Github credentials and displays id"""
if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"

    user = argv[1]
    password = argv[2]
    auth = HTTPBasicAuth(user, password)
    data_result = requests.get(url, auth=auth)
    print(data_result.json().get("id"))
