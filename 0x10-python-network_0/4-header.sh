#!/bin/bash
# This script passes variable in header of request
curl -sH "X-School-User-Id: 98" "$1"
