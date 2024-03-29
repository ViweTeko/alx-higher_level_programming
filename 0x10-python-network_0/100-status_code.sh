#!/bin/bash
# This script sends request to URL (as args) and displays status code
curl -sI -w '%{response_code}' "$1" -o /dev/null
