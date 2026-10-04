from ollama import chat
from pathlib import Path
import subprocess
import re


MODEL = "qwen2.5-coder:7b"


def get_source_file(repository):
    python_files = list(Path(repository).glob("*.py"))

    for file in python_files:
        if not file.name.startswith("test_"):
            return file

    return None


def generate_fix(file_path, code, test_output):

    prompt = f"""
You are an expert autonomous software debugging agent.

Fix the bug in this Python source file.

SOURCE FILE:
{file_path}

SOURCE CODE:
{code}

TEST FAILURE:
{test_output}

Rules:
- Find the actual root cause.
- Make the smallest safe fix.
- Do not change unrelated code.
- Preserve all existing correct behavior.
- Return ONLY the complete corrected Python source code.
- Do not include explanations.
- Do not use markdown code fences.
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()


def clean_code(response):

    # Remove markdown code fences if Qwen adds them.
    response = re.sub(r"^```python\s*", "", response)
    response = re.sub(r"^```\s*", "", response)
    response = re.sub(r"\s*```$", "", response)

    return response.strip()


def run_tests(repository):

    result = subprocess.run(
        ["python", "-m", "pytest", repository, "-v"],
        text=True,
        capture_output=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result.returncode == 0


def main():

    repository = input("Enter repository path: ").strip()

    repository_path = Path(repository)

    if not repository_path.exists():
        print("Repository not found.")
        return

    source_file = get_source_file(repository)

    if source_file is None:
        print("No source Python file found.")
        return

    print("\nSource file found:")
    print(source_file)

    code = source_file.read_text(encoding="utf-8")

    print("\nRunning tests before fix...")

    test_result = subprocess.run(
        ["python", "-m", "pytest", repository, "-v"],
        text=True,
        capture_output=True
    )

    test_output = test_result.stdout + "\n" + test_result.stderr

    if test_result.returncode == 0:
        print("\nAll tests already pass.")
        return

    print("\nGenerating fix with Qwen...")

    fixed_code = generate_fix(
        source_file,
        code,
        test_output
    )

    fixed_code = clean_code(fixed_code)

    print("\nApplying fix...")

    source_file.write_text(
        fixed_code,
        encoding="utf-8"
    )

    print(f"Fix written to: {source_file}")

    print("\nRunning tests after fix...")

    if run_tests(repository):
        print("\n" + "=" * 70)
        print("AUTO-FIX SUCCESSFUL")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("AUTO-FIX DID NOT PASS ALL TESTS")
        print("=" * 70)


if __name__ == "__main__":
    main()