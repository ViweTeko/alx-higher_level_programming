#!/bin/bash
#Bash script takes in URL and sends request back to it
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
