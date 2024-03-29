#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as it:
        html = it.read()

        print("Body Response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8", "replace")))
