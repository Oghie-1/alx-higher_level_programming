#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on a personal access token.
Usage: ./10-my_github.py <GitHub personal access token>
"""
import sys
import requests


if __name__ == "__main__":
    token = sys.argv[1]
    headers = {"Authorization": "token " + token}
    r = requests.get("https://api.github.com/user", headers=headers)

    if r.status_code == 200:
        print(r.json().get("id"))
    else:
        print("Error:", r.text)
