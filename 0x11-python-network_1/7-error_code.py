#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and displays the body of the response."""
import sys
import requests


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e))
