#!/bin/bash
# This script sends JSON POST request
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
