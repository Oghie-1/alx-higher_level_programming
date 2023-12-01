#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to fetch the URL and measure the size of the response body
response=$(curl -sI "$url")

# Check if the URL is accessible
if [ $? -ne 0 ]; then
    echo "Error: Unable to access the URL."
    exit 1
fi

# Extract the Content-Length header
size=$(echo "$response" | grep -i content-length | awk '{print $2}' | tr -d '\r')

# Display the size
if [ -n "$size" ]; then
    echo "Size of the response body: ${size} bytes"
else
    echo "Error: Content-Length header not found in the response."
fi
