import subprocess
import sys


def run_tests(test_path="."):
    print("\n" + "=" * 70)
    print("RUNNING TESTS")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_path, "-v"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print("\nERROR OUTPUT:")
        print(result.stderr)

    print("=" * 70)

    if result.returncode == 0:
        print("RESULT: ✅ ALL TESTS PASSED")
    else:
        print("RESULT: ❌ SOME TESTS FAILED")

    return result.returncode


if __name__ == "__main__":
    run_tests()