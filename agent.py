from ollama import chat
from repository import find_source_files, read_file


MODEL = "qwen2.5-coder:7b"


def ask_agent(prompt):
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


def build_repository_context(repository_path):
    files = find_source_files(repository_path)

    context = ""

    for file in files:
        content = read_file(file)

        context += f"""
==================================================
FILE: {file}
==================================================

{content}

"""

    return context, files


def analyze_repository(repository_path):

    context, files = build_repository_context(repository_path)

    if not files:
        print("No supported source files found.")
        return

    prompt = f"""
You are an expert software engineering AI.

You are analyzing a software repository.

Your first task is to understand the repository architecture.

Analyze the source code below and provide:

1. Project overview
2. Programming languages used
3. Important files
4. Main functions/classes
5. How the components interact
6. Potential architectural problems
7. Areas that should be investigated for bugs
8. Areas that should be investigated for security issues
9. Testing observations

Do NOT invent files or functionality that are not present.

Clearly distinguish between confirmed observations and areas requiring further investigation.

Repository source:

{context}
"""

    print("\nAnalyzing repository with Qwen...\n")

    result = ask_agent(prompt)

    print("=" * 70)
    print("REPOSITORY UNDERSTANDING REPORT")
    print("=" * 70)
    print(result)


if __name__ == "__main__":

    repository_path = input(
        "Enter repository path: "
    ).strip()

    analyze_repository(repository_path)