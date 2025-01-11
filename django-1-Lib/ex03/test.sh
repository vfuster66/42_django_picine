#!/bin/bash

echo "=== Testing roads_to_philosophy.py ==="

# Test 1: Example from the subject (42 number)
echo -e "\nTest 1: 42 (number)"
python3 roads_to_philosophy.py "42_(number)"

# Test 2: Known dead end
echo -e "\nTest 2: Testing a potential dead end"
python3 roads_to_philosophy.py "Dead_end"

# Test 3: Starting with Philosophy
echo -e "\nTest 3: Starting with Philosophy"
python3 roads_to_philosophy.py "Philosophy"

# Test 4: Article with multiple links
echo -e "\nTest 4: Testing 'Python_(programming_language)'"
python3 roads_to_philosophy.py "Python_(programming_language)"

# Test 5: Article with a redirect
echo -e "\nTest 5: Testing a redirect (Programming)"
python3 roads_to_philosophy.py "Programming"

# Test 6: Invalid article
echo -e "\nTest 6: Testing invalid article"
python3 roads_to_philosophy.py "ThisArticleDoesNotExist12345"

# Test 7: Another redirect (USA -> United States)
echo -e "\nTest 7: Testing a redirect (USA)"
python3 roads_to_philosophy.py "USA"

# Test 8: Another redirect (UK -> United Kingdom)
echo -e "\nTest 8: Testing a redirect (UK)"
python3 roads_to_philosophy.py "UK"

# Test 9: Redirect with special characters (COVID-19 -> Coronavirus_disease_2019)
echo -e "\nTest 9: Testing a redirect with special characters (COVID-19)"
python3 roads_to_philosophy.py "COVID-19"

# Test 10: Article starting with Philosophy
echo -e "\nTest 10: Testing another starting article (Mathematics)"
python3 roads_to_philosophy.py "Mathematics"

echo -e "\n=== Tests completed ==="
