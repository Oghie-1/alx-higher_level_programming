#!/bin/bash
# Check if URL argument is provided
curl -sI "$1" | grep -i content-length | cut -d " " -f2
