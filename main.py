import inspect
import test_sum_digits


# Counters to track how many tests passed or failed
passed = 0
failed = 0


print("=" * 55)
print("         RUNNING TEST SUITE: sum_of_digits")
print("=" * 55)
print()


# Collect all functions from test_sum_digits module
test_functions = [
    (name, func)
    for name, func in inspect.getmembers(test_sum_digits, inspect.isfunction)
    if name.startswith("test_")
]


# Run each test function
for name, func in test_functions:
    try:
        # Execute the test
        func()

        # If no assertion fails, the test passed
        print(f"  [PASSED]  {name}")
        passed += 1

    except AssertionError:
        # If an assertion inside the test fails
        print(f"  [FAILED]  {name}")
        failed += 1

    except Exception as e:
        # Catch any unexpected errors during the test
        print(f"  [ERROR]   {name} --> {e}")
        failed += 1


# Calculate total number of tests executed
total = passed + failed


# Print summary of results
print()
print("=" * 55)
print(f"  Total  : {total}")
print(f"  Passed : {passed}")
print(f"  Failed : {failed}")
print("=" * 55)