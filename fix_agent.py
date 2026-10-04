from ollama import chat


MODEL = "qwen2.5-coder:7b"


def analyze_failure(file_path, code, test_output):

    prompt = f"""
You are an expert software debugging agent.

A test suite has failed for the following source file.

SOURCE FILE:
{file_path}

SOURCE CODE:
{code}

TEST OUTPUT:
{test_output}

Analyze the failure carefully.

Provide:

1. ROOT CAUSE
Explain exactly why the test failed.

2. EVIDENCE
Point to the relevant code and test behavior.

3. PROPOSED FIX
Describe the smallest safe change needed.

4. CORRECTED CODE
Provide the complete corrected source file.

5. VERIFICATION
Explain why the proposed change should make the failing tests pass.

IMPORTANT:
- Do not invent problems.
- Do not modify unrelated code.
- Preserve existing behavior that is already correct.
- Do not execute or modify files yourself.
- This is a proposed fix only.
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


if __name__ == "__main__":

    file_path = input("Source file path: ").strip()

    print("\nPaste the source code.")
    print("Type END on a new line when finished.\n")

    code_lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        code_lines.append(line)

    code = "\n".join(code_lines)

    print("\nPaste the pytest failure output.")
    print("Type END on a new line when finished.\n")

    output_lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        output_lines.append(line)

    test_output = "\n".join(output_lines)

    print("\n" + "=" * 70)
    print("AI DEBUGGING ANALYSIS")
    print("=" * 70)

    result = analyze_failure(
        file_path,
        code,
        test_output
    )

    print(result)