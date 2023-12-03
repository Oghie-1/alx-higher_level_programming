#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Arguments: arg1: repo name, arg2: repo owner
"""
import sys
import requests


if __name__ == "__main__":
    # Get the arguments, arg1: repo name, arg2: repo owner
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    
    try:
        # Make the API request
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad responses
        
        commits = r.json()

        # Print information about the 10 most recent commits
        for i, commit in enumerate(commits[:10], start=1):
            sha = commit['sha']
            author = commit['commit']['author']['name']
            message = commit['commit']['message']
            print(f"{i}. Commit SHA: {sha}\n   Author: {author}\n   Message: {message}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
