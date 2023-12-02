#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = request.Request(url)
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.URLError as e:
        print("Error code: {}".format(e))
    except Exception as e:
        print("Unexpected error: {}".format(e))
