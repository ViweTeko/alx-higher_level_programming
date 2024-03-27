#!/bin/bash
# This script sends a GET request to the URL, then displays body of response

curl -s "$1" -X GET -L
