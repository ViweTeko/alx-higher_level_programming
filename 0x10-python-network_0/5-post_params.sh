#!/bin/bash
# This script sends POST request from URL
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
