#!/bin/bash
#displays all http methods the server will accept for a given url
curl -sI "$1" | grep allow | cut -d " " -f2-
