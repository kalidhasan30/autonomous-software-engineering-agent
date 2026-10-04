from ollama import chat
from repository import find_source_files, read_file


MODEL = "qwen2.5-coder:7b"


def analyze_security(file_path, code):

    prompt = f"""
You are a professional application security analysis agent.

Analyze this source file for security vulnerabilities.

FILE:
{file_path}

CODE:
{code}

Look specifically for:

1. SQL Injection
2. Command Injection
3. Cross-Site Scripting (XSS)
4. Path Traversal
5. Hardcoded passwords, API keys, or secrets
6. Insecure authentication
7. Broken authorization
8. Unsafe file operations
9. Insecure deserialization
10. Sensitive information exposure
11. Weak cryptography
12. Server-side request forgery
13. Unsafe input handling
14. Dependency or configuration risks visible in the code

For every finding provide:

Severity: Critical / High / Medium / Low
File:
Location:
Vulnerability:
Root Cause:
Potential Impact:
Suggested Fix:

IMPORTANT:
- Do not invent vulnerabilities.
- Only report issues supported by the code.
- Clearly distinguish confirmed vulnerabilities from potential risks.
- If no security problems are found, say so.
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
    print("Starting security analysis...\n")

    for file in files:

        code = read_file(file)

        print("=" * 70)
        print(f"SECURITY ANALYSIS: {file}")
        print("=" * 70)

        result = analyze_security(file, code)

        print(result)
        print()


if __name__ == "__main__":

    repository_path = input(
        "Enter repository path: "
    ).strip()

    analyze_repository(repository_path)