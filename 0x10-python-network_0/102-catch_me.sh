#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me response "You got me!"
curl -sL PUT -X -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
