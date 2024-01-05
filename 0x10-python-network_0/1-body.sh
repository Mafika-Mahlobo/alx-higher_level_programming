#!/bin/bash
#takes url, sends GET request and display the body
body=$(curl -s -w "%{http_code}" "$1")
http_status=$(echo "$body" | tail -n1)
if [ "$http_status" -eq 200 ]; then
	echo "$body"
fi
