#!/bin/bash

# Test script for request_wikipedia.py

echo "=== Testing request_wikipedia.py ==="

# Test 1: Valid search term
echo -e "\nTest 1: Valid search term 'chocolatine'"
python3 request_wikipedia.py "chocolatine"
if [ -f "chocolatine.wiki" ]; then
    echo "File created successfully ✅"
    cat chocolatine.wiki
else
    echo "File creation failed ❌"
fi

# Test 2: Invalid search term
echo -e "\nTest 2: Invalid search term 'xyzabc123'"
python3 request_wikipedia.py "xyzabc123"

# Test 3: No search term
echo -e "\nTest 3: No search term"
python3 request_wikipedia.py

# Test 4: Term with spaces
echo -e "\nTest 4: Term with spaces 'World War II'"
python3 request_wikipedia.py "World War II"
if [ -f "World_War_II.wiki" ]; then
    echo "File created successfully ✅"
else
    echo "File creation failed ❌"
fi

echo -e "\n=== Tests completed ==="