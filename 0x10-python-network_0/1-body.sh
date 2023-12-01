#!/bin/bash


# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to fetch the URL and display the body for a 200 status code
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
    body=$(curl -s "$url")
    echo "Body of the response (Status Code 200):"
    echo "$body"
else
    echo "Error: Status Code $response. Unable to display the body."
fi
