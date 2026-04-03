#!/bin/bash
# This script takes a URL, sends a GET request, and displays the size of the response body in bytes
curl -s "$1" | wc -c