#!/usr/bin/bash


#displays all http methods the server will accept for a given url

#send an OPTIONS request to the URL and displays the allow header

curl -sI "$1" | grep "Allow:"
