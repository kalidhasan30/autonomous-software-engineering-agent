from ollama import chat
from repository import find_source_files, read_file


MODEL = "qwen2.5-coder:7b"


def generate_tests(file_path, code):

    prompt = f"""
You are an expert Python test-generation agent.

Analyze this source file:

FILE:
{file_path}

CODE:
{code}

Generate useful pytest tests for the code.

Your tests should cover:

1. Normal/expected behavior
2. Edge cases
3. Invalid inputs
4. Boundary conditions
5. Exception handling
6. Important business logic

Rules:

- Generate only tests that are relevant to the actual code.
- Do not invent functions or classes.
- Use pytest.
- Clearly explain what each test checks.
- Return the complete test code in a Python code block.
- If the file does not contain testable logic, explain why.

Structure your response as:

TEST PLAN
-----------
Brief explanation.

GENERATED TESTS
---------------
Complete pytest code.
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
    print("Starting test generation...\n")

    for file in files:

        code = read_file(file)

        print("=" * 70)
        print(f"TEST GENERATION: {file}")
        print("=" * 70)

        result = generate_tests(file, code)

        print(result)
        print()


if __name__ == "__main__":

    repository_path = input(
        "Enter repository path: "
    ).strip()

    analyze_repository(repository_path)