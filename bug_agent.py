from ollama import chat
from repository import find_source_files, read_file


MODEL = "qwen2.5-coder:7b"


def analyze_bug(file_path, code):
    prompt = f"""
You are a professional software bug detection agent.

Analyze the following source file for REAL and POTENTIAL bugs.

FILE:
{file_path}

CODE:
{code}

Look for:

1. Logic errors
2. Incorrect conditions
3. Null/None handling problems
4. Exception handling problems
5. Resource management problems
6. Incorrect API usage
7. Edge cases
8. Type-related problems
9. Concurrency problems
10. Other correctness issues

For every finding provide:

Severity: Critical / High / Medium / Low
File:
Location:
Bug:
Root Cause:
Impact:
Suggested Fix:

IMPORTANT:
- Do not invent bugs.
- If the code appears correct, say so.
- Distinguish confirmed problems from potential risks.
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

    return response["message"]["content"]


def analyze_repository(repository_path):

    files = find_source_files(repository_path)

    if not files:
        print("No supported source files found.")
        return

    print(f"\nFound {len(files)} source file(s).")
    print("Starting bug detection...\n")

    for file in files:

        code = read_file(file)

        print("=" * 70)
        print(f"ANALYZING: {file}")
        print("=" * 70)

        result = analyze_bug(file, code)

        print(result)
        print()


if __name__ == "__main__":

    repository_path = input(
        "Enter repository path: "
    ).strip()

    analyze_repository(repository_path)