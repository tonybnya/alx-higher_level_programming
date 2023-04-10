#!/usr/bin/python3
# 0-hbtn_status.py
# @tonybnya
"""
This python script
"""
import urllib.request


def main():
    """ Main function """
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == '__main__':
    main()
