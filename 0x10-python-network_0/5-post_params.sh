#!/bin/bash
# Sends a POST request to a URL with specific variables in the body


# Usage: ./5-post_params.sh <URL>

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with specific variables in the body
curl -s -X POST -d "email=$email&subject=$subject" "$url"
