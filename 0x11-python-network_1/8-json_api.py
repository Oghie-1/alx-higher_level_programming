#!/usr/bin/python3 
"""a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    
    payload = {'q': arg}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=payload)
    try:
        r.raise_for_status()
        json = r.json()
        
        if json:
            print("[{:d}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    
    except Exception:
        print("Not a valid JSON")
