#!/usr/bin/python3
"""This script takes your Github credentials and displays id"""
if __name__ == "__main__":
    from sys import argv
    import requests

    url = "https://api.github.com/user"

    user = argv[1]
    password = argv[2]
    data_result = requests.get(url, auth=(user, password))
    try:
        json_data = data_result.join()
        print(json_data;"id"])
    except Exception:
        print("None")
