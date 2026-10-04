from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
}


SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".go",
    ".rs",
    ".php",
}


def find_source_files(repository_path):
    repository = Path(repository_path)

    files = []

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        if any(
            ignored in file.parts
            for ignored in IGNORED_DIRECTORIES
        ):
            continue

        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(file)

    return files


def read_file(file_path):
    try:
        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception as error:
        return f"[Unable to read file: {error}]"


if __name__ == "__main__":

    repository = input("Enter repository path: ")

    files = find_source_files(repository)

    print("\nRepository Analysis")
    print("=" * 60)

    print(f"Source files found: {len(files)}\n")

    for file in files:
        print(file)