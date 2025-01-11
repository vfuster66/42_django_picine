import subprocess

def test_state():
    test_cases = [
        ("Salem", "Oregon"),
        ("Montgomery", "Alabama"),
        ("Trenton", "New Jersey"),
        ("Denver", "Colorado"),
        ("Paris", "Unknown capital city"),
    ]

    for capital, expected_output in test_cases:
        result = subprocess.run(["python3", "state.py", capital], capture_output=True, text=True)
        output = result.stdout.strip()
        print(f"Test input: {capital}")
        print(f"Expected output: {expected_output}")
        print(f"Actual output: {output}")
        assert output == expected_output, f"Test failed for {capital}: expected '{expected_output}', got '{output}'"
        print("Test passed.\n")

    print("All tests passed.")

if __name__ == "__main__":
    test_state()
