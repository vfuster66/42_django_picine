import subprocess

def test_capital_city():
    test_cases = [
        ("Oregon", "Salem"),
        ("Alabama", "Montgomery"),
        ("New Jersey", "Trenton"),
        ("Colorado", "Denver"),
        ("Ile-De-France", "Unknown state"),
    ]

    for state, expected_output in test_cases:
        result = subprocess.run(["python3", "capital_city.py", state], capture_output=True, text=True)
        output = result.stdout.strip()
        print(f"Test input: {state}")
        print(f"Expected output: {expected_output}")
        print(f"Actual output: {output}")
        assert output == expected_output, f"Test failed for {state}: expected '{expected_output}', got '{output}'"
        print("Test passed.\n")

    print("All tests passed.")

if __name__ == "__main__":
    test_capital_city()
