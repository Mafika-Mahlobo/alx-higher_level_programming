#!/bin/bash
#Sends https request to server and return size of response
curl -s -o /temp -w "%{size_download}\n" "$1"
