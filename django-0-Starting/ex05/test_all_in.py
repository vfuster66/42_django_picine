#!/usr/bin/python3

import subprocess

def run_test(input_str, expected_output=None):
    """Run test with input string and compare with expected output."""
    result = subprocess.run(['python3', 'all_in.py', input_str], 
                          capture_output=True, text=True)
    actual_output = result.stdout.strip()
    
    if expected_output is None:
        print(f"\nTest: {input_str}")
        print(f"Output: {actual_output}")
    else:
        success = actual_output == expected_output
        print(f"\nTest: {input_str}")
        print(f"Expected: {expected_output}")
        print(f"Got: {actual_output}")
        print(f"Status: {'✅ Pass' if success else '❌ Fail'}")

def run_all_tests():
    print("=== Testing all_in.py ===")

    # Test 1: Basic state lookup
    run_test('Oregon', 'Salem is the capital of Oregon')
    
    # Test 2: Basic capital lookup
    run_test('Salem', 'Salem is the capital of Oregon')
    
    # Test 3: Case insensitive
    run_test('OREGON', 'Salem is the capital of OREGON')
    
    # Test 4: Unknown entry
    run_test('Paris', 'Paris is neither a capital city nor a state')
    
    # Test 5: Multiple entries
    run_test('Oregon, Salem',
            'Salem is the capital of Oregon\nSalem is the capital of Oregon')
    
    # Test 6: With spaces
    run_test(' Oregon , Salem ',
            'Salem is the capital of Oregon\nSalem is the capital of Oregon')
    
    # Test 7: Empty input (should print nothing)
    run_test('')
    
    # Test 8: Double comma (should print nothing)
    run_test('Oregon,,Salem')
    
    # Test 9: Mixed valid and invalid
    run_test('Oregon, Paris, Salem',
            'Salem is the capital of Oregon\nParis is neither a capital city nor a state\nSalem is the capital of Oregon')

if __name__ == '__main__':
    run_all_tests()