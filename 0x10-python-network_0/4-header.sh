#!/bin/bash
# Sends a GET request to a URL with a specific header


# Usage: ./4-header.sh <URL>

url="$1"

# Send a GET request with the X-School-User-Id header set to 98
curl -s -H "X-School-User-Id: 98" "$url"
