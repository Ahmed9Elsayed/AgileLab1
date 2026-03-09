import inspect
import test_sum_digits


# ─────────────────────────────────────────
#           AUTO-DISCOVER & RUN
# ─────────────────────────────────────────

passed = 0
failed = 0

print("=" * 55)
print("         RUNNING TEST SUITE: sum_of_digits")
print("=" * 55)
print()

# Get all functions from test_sum_digits.py that start with "test_"
test_functions = [
    (name, func)
    for name, func in inspect.getmembers(test_sum_digits, inspect.isfunction)
    if name.startswith("test_")
]

for name, func in test_functions:
    try:
        func()          # call the test function
        print(f"  [PASSED]  {name}")
        passed += 1
    except AssertionError:
        print(f"  [FAILED]  {name}")
        failed += 1
    except Exception as e:
        print(f"  [ERROR]   {name} --> {e}")
        failed += 1

# ─────────────────────────────────────────
#              SUMMARY
# ─────────────────────────────────────────

total = passed + failed
print()
print("=" * 55)
print(f"  Total  : {total}")
print(f"  Passed : {passed}")
print(f"  Failed : {failed}")
print("=" * 55)