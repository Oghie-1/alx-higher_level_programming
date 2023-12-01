#!/bin/bash
# Send a GET request with the X-School-User-Id header set to 98
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
