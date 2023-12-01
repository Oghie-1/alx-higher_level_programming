#!/bin/bash
# Send a POST request with specific variables in the body
curl -sL "$1" -X POST -d "email=hr@holbertonschool.com&subjetc=I will always be here for PLD"
